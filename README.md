
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

## Adding Publication Thumbnails and Links

Keep custom publication metadata out of `_data/sources.yaml` so it does not get overwritten by the export scripts.

1. **Add a record** in `_data/publication-metadata.yaml` with the publication `id` and any extra fields you want to keep, such as `image`, `code`, or custom `buttons`.
   - `image`: Path to a thumbnail image for the publication
   - `code`: URL to code repository (automatically creates a "Source" button)
   - `buttons`: Custom buttons with `type` and `link` (e.g., `type: source`, `type: docs`)
2. **Regenerate the citations** so the metadata is merged into `_data/citations.yaml`.
3. **Add the publication ID** to the project page front matter under `publications:` so the page renders it in the Related Publications section.

Example:

```yaml
# _data/publication-metadata.yaml
- id: doi:10.48550/arXiv.2206.05082
  image: images/example-publication-thumbnail.jpg
  code: https://github.com/example/repo
  buttons:
    - type: docs
      link: https://example.com/docs
```

```yaml
# _projects/cool-dataset.md
publications:
  - doi:10.48550/arXiv.2206.05082
```

  ## Testing Locally

  To preview your changes before submitting a pull request, you'll need to build and run the site locally:

  1. **Install dependencies** — Follow the [Lab Website Template installation guide](https://greene-lab.gitbook.io/lab-website-template-docs/getting-started)
  2. **Build and serve** — Run `bundle exec jekyll serve` from the project root
  3. **View in your browser** — Open `http://localhost:4000` to see your changes
  4. **Submit a pull request** once you're happy with how your profile looks!

