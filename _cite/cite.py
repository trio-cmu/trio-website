"""
cite process to convert sources and metasources into full citations
"""

import traceback
from importlib import import_module
from pathlib import Path
from dotenv import load_dotenv
from util import *


# load environment variables
load_dotenv()


# save errors/warnings for reporting at end
errors = []
warnings = []

# optional custom publication metadata keyed by citation id
publication_metadata = {}


def load_publication_metadata():
    """
    load custom publication metadata that should survive exports
    """

    metadata_file = Path("_data/publication-metadata.yaml")
    if not metadata_file.is_file():
        return {}

    try:
        data = load_data(metadata_file)
        if not list_of_dicts(data):
            raise Exception(f"{metadata_file.name} data file not a list of dicts")
    except Exception as e:
        log(e, indent=2, level="ERROR")
        errors.append(e)
        return {}

    metadata_by_id = {}
    for entry in data:
        metadata_id = get_safe(entry, "id", "").strip()
        if not metadata_id:
            continue
        metadata_by_id[metadata_id] = {
            key: value for key, value in entry.items() if key != "id"
        }

    return metadata_by_id

# output citations file
output_file = "_data/citations.yaml"


log()

log("Compiling sources")

# compiled list of sources
sources = []

# in-order list of plugins to run
plugins = ["google-scholar", "pubmed", "orcid", "sources"]

# loop through plugins
for plugin in plugins:
    # convert into path object
    plugin = Path(f"plugins/{plugin}.py")

    log(f"Running {plugin.stem} plugin")

    # get all data files to process with current plugin
    files = Path.cwd().glob(f"_data/{plugin.stem}*.*")
    files = list(filter(lambda p: p.suffix in [".yaml", ".yml", ".json"], files))

    log(f"Found {len(files)} {plugin.stem}* data file(s)", indent=1)

    # loop through data files
    for file in files:
        log(f"Processing data file {file.name}", indent=1)

        # load data from file
        try:
            data = load_data(file)
            # check if file in correct format
            if not list_of_dicts(data):
                raise Exception(f"{file.name} data file not a list of dicts")
        except Exception as e:
            log(e, indent=2, level="ERROR")
            errors.append(e)
            continue

        # loop through data entries
        for index, entry in enumerate(data):
            log(f"Processing entry {index + 1} of {len(data)}, {label(entry)}", level=2)

            # run plugin on data entry to expand into multiple sources
            try:
                expanded = import_module(f"plugins.{plugin.stem}").main(entry)
                # check that plugin returned correct format
                if not list_of_dicts(expanded):
                    raise Exception(f"{plugin.stem} plugin didn't return list of dicts")
            # catch any plugin error
            except Exception as e:
                # log detailed pre-formatted/colored trace
                print(traceback.format_exc())
                # log high-level error
                log(e, indent=3, level="ERROR")
                errors.append(e)
                continue

            # loop through sources
            for source in expanded:
                if plugin.stem != "sources":
                    log(label(source), level=3)

                # include meta info about source
                source["plugin"] = plugin.name
                source["file"] = file.name

                # add source to compiled list
                sources.append(source)

            if plugin.stem != "sources":
                log(f"{len(expanded)} source(s)", indent=3)


log("Merging sources by id")

# merge sources with matching (non-blank) ids
for a in range(0, len(sources)):
    a_id = get_safe(sources, f"{a}.id", "")
    if not a_id:
        continue
    for b in range(a + 1, len(sources)):
        b_id = get_safe(sources, f"{b}.id", "")
        if b_id == a_id:
            log(f"Found duplicate {b_id}", indent=2)
            sources[a].update(sources[b])
            sources[b] = {}
sources = [entry for entry in sources if entry]


log(f"{len(sources)} total source(s) to cite")


log()

log("Generating citations")

publication_metadata = load_publication_metadata()

# list of new citations
citations = []


# loop through compiled sources
for index, source in enumerate(sources):
    log(f"Processing source {index + 1} of {len(sources)}, {label(source)}")

    # if explicitly flagged, remove/ignore entry
    if get_safe(source, "remove", False) == True:
        continue

    # new citation data for source
    citation = {}

    # source id
    _id = get_safe(source, "id", "").strip()

    # manubot doesn't work without an id
    if _id:
        log("Using Manubot to generate citation", indent=1)

        try:
            # run manubot and set citation
            citation = cite_with_manubot(_id)

        # if manubot cannot cite source
        except Exception as e:
            plugin = get_safe(source, "plugin", "")
            file = get_safe(source, "file", "")
            # if regular source (id entered by user), throw error
            if plugin == "sources.py":
                log(e, indent=3, level="ERROR")
                errors.append(f"Manubot could not generate citation for source {_id}")
            # otherwise, if from metasource (id retrieved from some third-party api), just warn
            else:
                log(e, indent=3, level="WARNING")
                warnings.append(
                    f"Manubot could not generate citation for source {_id} (from {file} with {plugin})"
                )
                # discard source from citations
                continue

    # preserve fields from input source, overriding existing fields
    # but keep source buttons separate to ensure they take priority
    source_buttons = source.pop("buttons", None)
    citation.update(source)
    if source_buttons:
        citation["buttons"] = source_buttons

    # merge any custom metadata stored outside the generated sources file
    # (use direct dict access since _id contains dots which break get_safe)
    custom_meta = publication_metadata.get(_id, {})
    
    # convert code field into a button if present
    if "code" in custom_meta:
        code_link = custom_meta.pop("code")  # remove from metadata
        if "buttons" not in citation:
            citation["buttons"] = []
        # add code button if not already present
        if not any(b.get("type") == "source" for b in citation["buttons"]):
            citation["buttons"].append({"type": "source", "link": code_link})
    
    citation.update(custom_meta)

    # ensure date in proper format for correct date sorting
    if get_safe(citation, "date", ""):
        citation["date"] = format_date(get_safe(citation, "date", ""))

    # remove internal metadata fields not needed in output
    citation.pop("plugin", None)
    citation.pop("file", None)
    citation.pop("projects", None)

    # add new citation to list
    citations.append(citation)


log()

log("Saving updated citations")


# save new citations
try:
    save_data(output_file, citations)
except Exception as e:
    log(e, level="ERROR")
    errors.append(e)


log()


# exit at end, so user can see all errors/warnings in one run
if len(warnings):
    log(f"{len(warnings)} warning(s) occurred above", level="WARNING")
    for warning in warnings:
        log(warning, indent=1, level="WARNING")

if len(errors):
    log(f"{len(errors)} error(s) occurred above", level="ERROR")
    for error in errors:
        log(error, indent=1, level="ERROR")
    log()
    exit(1)

else:
    log("All done!", level="SUCCESS")

log()
