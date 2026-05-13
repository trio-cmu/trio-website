"""
Convert a BibTeX file (Zotero export) into `_data/sources.yaml` expected
by the project's citation tooling.

Run from repository root as:

    python _cite/bib2sources.py

This script imports the project's `util.save_data` to write the YAML file
so the same header/comment behavior is used as the rest of the tooling.
"""
from pathlib import Path
import bibtexparser
import re
import unicodedata

# import save_data from the project's _cite util (works when running
# `python _cite/bib2sources.py` from repo root)
from util import save_data, log


def latex_to_unicode(text):
    """
    Convert LaTeX special characters to their proper Unicode equivalents.
    Preserves accented characters instead of transliterating them.
    """
    if not text:
        return text
    
    # LaTeX accent commands to Unicode mappings
    # Diaeresis/umlaut - ä, ë, ï, ö, ü
    text = re.sub(r'{\\\"a}', 'ä', text, flags=re.IGNORECASE)
    text = re.sub(r'\\\"a', 'ä', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\\"e}', 'ë', text, flags=re.IGNORECASE)
    text = re.sub(r'\\\"e', 'ë', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\\"i}', 'ï', text, flags=re.IGNORECASE)
    text = re.sub(r'\\\"i', 'ï', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\\"o}', 'ö', text, flags=re.IGNORECASE)
    text = re.sub(r'\\\"o', 'ö', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\\"u}', 'ü', text, flags=re.IGNORECASE)
    text = re.sub(r'\\\"u', 'ü', text, flags=re.IGNORECASE)
    
    # Acute accent - á, é, í, ó, ú
    text = re.sub(r"{\\' a}", 'á', text, flags=re.IGNORECASE)
    text = re.sub(r"\\'a", 'á', text, flags=re.IGNORECASE)
    text = re.sub(r"{\\' e}", 'é', text, flags=re.IGNORECASE)
    text = re.sub(r"\\'e", 'é', text, flags=re.IGNORECASE)
    text = re.sub(r"{\\' i}", 'í', text, flags=re.IGNORECASE)
    text = re.sub(r"\\'i", 'í', text, flags=re.IGNORECASE)
    text = re.sub(r"{\\' o}", 'ó', text, flags=re.IGNORECASE)
    text = re.sub(r"\\'o", 'ó', text, flags=re.IGNORECASE)
    text = re.sub(r"{\\' u}", 'ú', text, flags=re.IGNORECASE)
    text = re.sub(r"\\'u", 'ú', text, flags=re.IGNORECASE)
    
    # Grave accent - à, è, ò, ù
    text = re.sub(r'{\\`a}', 'à', text, flags=re.IGNORECASE)
    text = re.sub(r'\\`a', 'à', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\`e}', 'è', text, flags=re.IGNORECASE)
    text = re.sub(r'\\`e', 'è', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\`o}', 'ò', text, flags=re.IGNORECASE)
    text = re.sub(r'\\`o', 'ò', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\`u}', 'ù', text, flags=re.IGNORECASE)
    text = re.sub(r'\\`u', 'ù', text, flags=re.IGNORECASE)
    
    # Circumflex - â, ê, ô, û
    text = re.sub(r'{\\^a}', 'â', text, flags=re.IGNORECASE)
    text = re.sub(r'\\^a', 'â', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\^e}', 'ê', text, flags=re.IGNORECASE)
    text = re.sub(r'\\^e', 'ê', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\^o}', 'ô', text, flags=re.IGNORECASE)
    text = re.sub(r'\\^o', 'ô', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\^u}', 'û', text, flags=re.IGNORECASE)
    text = re.sub(r'\\^u', 'û', text, flags=re.IGNORECASE)
    
    # Tilde - ã, ñ, õ
    text = re.sub(r'{\\~a}', 'ã', text, flags=re.IGNORECASE)
    text = re.sub(r'\\~a', 'ã', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\~n}', 'ñ', text, flags=re.IGNORECASE)
    text = re.sub(r'\\~n', 'ñ', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\~o}', 'õ', text, flags=re.IGNORECASE)
    text = re.sub(r'\\~o', 'õ', text, flags=re.IGNORECASE)
    
    # Caron (háček) - č, ž
    text = re.sub(r'{\\v c}', 'č', text, flags=re.IGNORECASE)
    text = re.sub(r'\\v c', 'č', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\v z}', 'ž', text, flags=re.IGNORECASE)
    text = re.sub(r'\\v z', 'ž', text, flags=re.IGNORECASE)
    
    # Ring above - å
    text = re.sub(r'{\\aa}', 'å', text, flags=re.IGNORECASE)
    text = re.sub(r'\\aa', 'å', text, flags=re.IGNORECASE)
    
    # Misc special chars - ø, æ, œ, ß, ı
    text = re.sub(r'{\\o}(?![a-z])', 'ø', text, flags=re.IGNORECASE)
    text = re.sub(r'\\o(?![a-z])', 'ø', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\ae}', 'æ', text, flags=re.IGNORECASE)
    text = re.sub(r'\\ae', 'æ', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\oe}', 'œ', text, flags=re.IGNORECASE)
    text = re.sub(r'\\oe', 'œ', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\ss}', 'ß', text, flags=re.IGNORECASE)
    text = re.sub(r'\\ss', 'ß', text, flags=re.IGNORECASE)
    text = re.sub(r'{\\i}', 'ı', text, flags=re.IGNORECASE)
    text = re.sub(r'\\i', 'ı', text, flags=re.IGNORECASE)
    
    return text


def clean_bibtex(text):
    """
    Clean BibTeX formatting from text:
    - Remove/unescape braces: {{text}} -> text
    - Convert LaTeX special chars to Unicode equivalents
    - Remove stray single accented characters (e.g., ü Bora -> Bora)
    """
    if not text:
        return text

    # Convert LaTeX to Unicode first
    text = latex_to_unicode(text)
    
    # Remove outermost braces, handling nested braces
    text = re.sub(r'^{+|}{1,}$', '', text)  # strip outer braces
    text = re.sub(r'{{(.+?)}}', r'\1', text)  # {{text}} -> text

    # Clean up any remaining braces
    text = re.sub(r'[{}]', '', text)
    
    # Remove stray single accented characters at the beginning
    # (e.g., "ü Bora" -> "Bora", "é Last" -> "Last")
    # Match a single accented character followed by space at the start
    text = re.sub(r'^[àáâãäåæèéêëìíîïðòóôõöøœùúûüýþÿ]\s+', '', text, flags=re.IGNORECASE)

    return text.strip()


def make_id(entry):
    # prefer DOI
    doi = entry.get("doi")
    if doi:
        doi = doi.strip()
        if doi.lower().startswith("doi:"):
            doi_val = doi.split(":", 1)[1].strip()
        else:
            doi_val = doi
        return f"doi:{doi_val}"

    # next prefer url
    url = entry.get("url")
    if url:
        return f"url:{url.strip()}"

    # otherwise fallback to bibtex key
    key = entry.get("ID") or entry.get("id") or ""
    return f"bibtex:{key}"


def format_author_name(raw_name):
    """
    Format a BibTeX author name to "Firstname Lastname" format.
    Handles formats like:
    - "Lastname, Firstname"
    - "Firstname Lastname"
    - "Firstname {von} Lastname"
    - "Firstname Lastname, Jr."
    """
    if not raw_name:
        return ""
    
    # Clean up the name first
    name = raw_name.strip()
    
    # Handle "Lastname, Firstname" format
    if ',' in name:
        parts = name.split(',')
        if len(parts) >= 2:
            lastname = parts[0].strip()
            firstname = parts[1].strip()
            
            # Handle suffixes like "Jr." or "Sr."
            if len(parts) > 2:
                suffix = parts[2].strip()
                # Append suffix if present
                return f"{firstname} {lastname} {suffix}".strip()
            return f"{firstname} {lastname}".strip()
    
    # Already in "Firstname Lastname" format
    return name


def parse_authors(author_string):
    """
    Parse BibTeX author field into list of author names.
    Handles "First Last and Second Author" format and converts to "Firstname Lastname".
    """
    if not author_string:
        return []
    # split by ' and ' (BibTeX separator)
    authors = author_string.split(" and ")
    # Format each author name properly
    formatted_authors = [format_author_name(author) for author in authors]
    return formatted_authors


def parse_bibtex_month(month_string):
    """
    Convert BibTeX month values to a two-digit month number.
    Accepts common abbreviations, full names, or numeric strings.
    """
    if not month_string:
        return ""

    month_string = clean_bibtex(str(month_string)).strip().lower()
    month_map = {
        "jan": "01",
        "january": "01",
        "feb": "02",
        "february": "02",
        "mar": "03",
        "march": "03",
        "apr": "04",
        "april": "04",
        "may": "05",
        "jun": "06",
        "june": "06",
        "jul": "07",
        "july": "07",
        "aug": "08",
        "august": "08",
        "sep": "09",
        "september": "09",
        "oct": "10",
        "october": "10",
        "nov": "11",
        "november": "11",
        "dec": "12",
        "december": "12",
    }
    if month_string in month_map:
        return month_map[month_string]
    if month_string.isdigit():
        return f"{int(month_string):02d}"
    return ""


def main():
    bib_path = Path("_data/zotero-export.bib")
    if not bib_path.is_file():
        log(f"Can't find {bib_path}", level="ERROR")
        raise SystemExit(1)

    with open(bib_path, encoding="utf8") as fh:
        bib_database = bibtexparser.load(fh)

    entries = []
    for entry in bib_database.entries:
        item = {"id": make_id(entry)}

        # Preserve Zotero-maintained metadata fields (cleaned of BibTeX formatting)
        if entry.get("title"):
            item["title"] = clean_bibtex(entry.get("title"))

        # Authors (parsed, formatted, and cleaned)
        if entry.get("author"):
            raw_authors = entry.get("author")
            # First parse and format author names, then clean BibTeX formatting
            formatted_authors = parse_authors(raw_authors)
            cleaned_authors = [clean_bibtex(author) for author in formatted_authors]
            item["authors"] = cleaned_authors

        # Date: prefer year-month-day, fallback to year-only as Jan 1
        year = entry.get("year", "").strip()
        month = entry.get("month", "").strip()
        if year:
            month_number = parse_bibtex_month(month)
            if month_number:
                item["date"] = f"{year}-{month_number}-01"
            else:
                item["date"] = f"{year}-01-01"

        # Abstract (cleaned)
        if entry.get("abstract"):
            item["abstract"] = clean_bibtex(entry.get("abstract"))

        # Create button linking to DOI or URL
        buttons = []
        doi = entry.get("doi", "").strip()
        url = entry.get("url", "").strip()
        
        if doi:
            # Format DOI as URL if needed
            if not doi.lower().startswith("http"):
                doi_url = f"https://doi.org/{doi.replace('doi:', '')}"
            else:
                doi_url = doi
            buttons.append({"type": "paper", "link": doi_url})
        elif url:
            buttons.append({"type": "paper", "link": url})
        
        if buttons:
            item["buttons"] = buttons

        # Notes (cleaned)
        if entry.get("note"):
            item["note"] = clean_bibtex(entry.get("note"))

        # Publisher or journal/booktitle (cleaned)
        publisher = clean_bibtex(entry.get("publisher", ""))
        journal = clean_bibtex(entry.get("journal", ""))
        booktitle = clean_bibtex(entry.get("booktitle", ""))
        if publisher:
            item["publisher"] = publisher
        elif journal:
            item["publisher"] = journal
        elif booktitle:
            item["publisher"] = booktitle

        # Pages (cleaned)
        if entry.get("pages"):
            item["pages"] = clean_bibtex(entry.get("pages"))

        # Volume and number (common in journals, cleaned)
        if entry.get("volume"):
            item["volume"] = clean_bibtex(entry.get("volume"))
        if entry.get("number"):
            item["number"] = clean_bibtex(entry.get("number"))

        # Entry type (article, inproceedings, etc.) for reference
        if entry.get("ENTRYTYPE"):
            item["type"] = entry.get("ENTRYTYPE").lower()

        entries.append(item)

    # save to the expected location
    save_data("_data/sources.yaml", entries)
    log(f"Wrote _data/sources.yaml with {len(entries)} entries")


if __name__ == "__main__":
    main()
    print("\n")
