# Project context

Read `README.md` before starting work in this directory.

This project coordinates improvements and updates to the base software for running Koinos producer nodes. The main references are the organization https://github.com/koinos and the Docker integration repository https://github.com/koinos/koinos.

## Work continuity

- Write all repository documentation in English, including local notes maintained for this project.
- Keep analysis, decisions and references to changes in the affected repositories here.
- Before modifying software, identify the relevant repository, version and dependencies; check their current state.
- Document the analysis in Markdown before implementing an improvement.
- Distinguish proposals, implementations, tests and actual deployments when reporting status.
- The project's general purpose does not itself authorize deploying changes to producer nodes.

## Continuation point

- Maintain shared architectural and operator documentation in https://github.com/pgarciagon/koinos-docs; the local checkout is recorded in ignored `LOCAL_REFERENCES.md`. Keep this coordinator focused on inventory, proposals, decisions and change references. Consult the documentation repository's own instructions before editing it and distinguish its source baseline from this inventory's baseline.
- Consult the public references in the README. If present, `LOCAL_REFERENCES.md` contains local environment references excluded from Git, including additional Knodel documentation.
- Keep local files and analysis that depends on private project information out of publication. When reusing historical documentation, verify options and data against the target version.
- Initial inventory: `docs/inventory/2026-09-30-inventory.md`; evidence in `docs/inventory/evidence/`.
- The clones in `upstream/` are independent public references. Read their own instructions before modifying software there.
- The inventory proposes validating versions and preventing silent fallback to `latest` as the first scoped contribution to the integration repository; chain PR #862 deserves priority investigation. Both remain pending implementation or validation in this project.
- For any update, distinguish Git tags, releases, Docker digests and versions actually installed on a node. Refresh public data before selecting artifacts.
