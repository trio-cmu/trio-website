Project pages
-------------

Project pages are stored as individual markdown files in `_projects/`.
To add or edit a project, update the corresponding file there (front matter fields such
as `title`, `subtitle`, `image`, `description`, `group`, `tags`, and `publications`).

The site will automatically generate pages and the projects index from this collection.

If you previously edited `_data/projects.yaml`, migrate entries into `_projects/*.md` and
remove the YAML file — projects are canonical in `_projects/` now.

Notes:
- Featured projects: add `group: featured` to the project's front matter to include it in the Featured section on the Projects index.
