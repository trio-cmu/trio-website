
  ![on-push](../../actions/workflows/on-push.yaml/badge.svg)
  ![on-pull-request](../../actions/workflows/on-pull-request.yaml/badge.svg)
  ![on-schedule](../../actions/workflows/on-schedule.yaml/badge.svg)

  # trio-cmu's Website

  Visit **[trio-cmu.github.io/trio-website](https://trio-cmu.github.io/trio-website)** 🚀

  _Built with [Lab Website Template](https://greene-lab.gitbook.io/lab-website-template-docs)_

  ## Adding Your Profile

  To add your member profile to the website:

  1. **Create a new file** in the `_members/` folder named `first-last.md` (e.g., `jane-doe.md`)
  2. **Add the following information** at the top of your file (between the `---` lines):
     - `name`: Your full name
     - `image`: Path to your photo (e.g., `images/jane-doe.jpg`)
     - `role`: Your role (`phd`, `ms`, `undergrad`, `visitor`, or `researcher`)
     - `group`: Your status (`current`, `alum`, `staff`, or `collaborator`)
     - `links`: Your social/professional links (github, email, home-page, twitter, orcid, etc.) — optional links can be commented out with `#`
  3. **Write a brief bio** below the frontmatter: a couple of sentences about your research interests and yourself
  4. **Add a photo** to the `images/` folder using the filename you specified above

  See `_members/first-last.md` for a template!

## Managing Publications and Project Associations

Publications are automatically pulled from `_data/sources.yaml` (which is auto-generated) and enriched with metadata from `_data/publication-metadata.yaml`.

### Adding a New Publication

To add a new publication to the site:

1. Add the publication to your Zotero library and export the library as BibTeX to `_data/zotero-export.bib`, or add a BibTeX entry directly to `_data/zotero-export.bib`.
2. Regenerate the machine-readable sources file (this overwrites `_data/sources.yaml`) by running:

```bash
python _cite/bib2sources.py
```

3. Add any custom metadata (thumbnail image, `code` link, `buttons`, `projects`, etc.) to `_data/publication-metadata.yaml` using the publication `id` shown in `_data/sources.yaml` (use `doi:...`, `url:...`, or `bibtex:...` as applicable).
4. Regenerate the final citations (merges sources and metadata into `_data/citations.yaml`) by running:

```bash
python _cite/cite.py
```

5. Commit your changes and open a pull request. The GitHub Actions build will show a preview so you can verify the publication appears correctly.

Note: Do not edit `_data/sources.yaml` directly — it is auto-generated and will be overwritten by exports. Keep persistent custom fields in `_data/publication-metadata.yaml`.

### Adding Publication Thumbnails and Links

Keep custom publication metadata out of `_data/sources.yaml` since it gets overwritten by the export scripts.

1. **Add a record** in `_data/publication-metadata.yaml` with the publication `id` and any extra fields you want to keep:
   - `image`: Path to a thumbnail image for the publication
   - `code`: URL to code repository (automatically creates a "Source" button)
   - `buttons`: Custom buttons with `type` and `link` (e.g., `type: source`, `type: docs`)
   - `projects`: List of project permalinks this publication is affiliated with
2. **Regenerate the citations** so the metadata is merged into `_data/citations.yaml`.

Example:

```yaml
# _data/publication-metadata.yaml
- id: doi:10.48550/arXiv.2206.05082
  image: images/example-publication-thumbnail.jpg
  code: https://github.com/example/repo
  buttons:
    - type: docs
      link: https://example.com/docs
  projects:
    - /projects/cool-project/
    - /projects/another-project/
```

### Linking Publications to Projects

Instead of manually listing publications in each project file, publications are automatically displayed on project pages based on their `projects` array in `publication-metadata.yaml`:

- **On project pages**: Publications listed in `publication-metadata.yaml` with the project's permalink will automatically appear in the "Related Publications" section
- **On publication pages**: Each publication displays links to all projects it's associated with

Example project file:

```yaml
# _projects/cool-project.md
---
layout: project
permalink: /projects/cool-project/
title: Cool Project
---
```

Publications with `/projects/cool-project/` in their `projects` array will automatically appear on this project's page. No need to manually manage the publications list!

## Testing 

If you are making small changes, you probably don't need to test things locally. In fact, once you open a quick pull request, the GitHub Actions workflows will automatically build and deploy a preview of the site with your changes so you can see how it looks before merging. If you make larger changes and want to have faster feedback, you can also build and serve the site locally to see your changes in real time, by following the instructions below.

### Local install

To preview your changes before submitting a pull request, you'll need to build and run the site locally:

1. **Install dependencies** — Follow the [Lab Website Template installation guide](https://greene-lab.gitbook.io/lab-website-template-docs/getting-started)
2. **Build and serve** — Run `bundle exec jekyll serve` from the project root
3. **View in your browser** — Open `http://localhost:4000` to see your changes
4. **Submit a pull request** once you're happy with how your profile looks!