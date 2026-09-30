# Maintained Koinos documentation repository

Date: September 30, 2026. Status: implemented and published; local and CI documentation checks passed.

## Decision

Create `pgarciagon/koinos-docs` as a public, independently maintained community documentation repository, starting with the public-facing content of the local `koinos-docs-consolidated` snapshot at commit `9178aa7`. Preserve the upstream MIT license and record the full source revision in the new repository.

Keep architectural and service references in `docs/architecture/`, and operational procedures in `docs/nodes/`. This coordinator retains inventory, proposals, decisions and links to the maintained documentation. Documentation is written in English.

## Publication scope

Publish the existing documentation pages, assets, examples and their validation tools. Import a fresh snapshot rather than the local project's full history. Unreviewed material under `drafts/` remains local and ignored. Do not import private Knodel files, local paths or project notes.

Identify the documentation as a community edition. The upstream `koinos-docs` README redirects contributions to `koinos/koinos/docs`, but that path returned HTTP 404 on September 30, 2026. This repository supplies an independently maintained home while upstream contribution routing is unresolved.

## Maintenance and verification

Record source provenance and service baselines without claiming a new technical audit. Add an English contribution guide, a detailed service-reference template, repository instructions and CI documentation checks. Verify a documentation build and local links before publishing. Update coordinator links after confirming the public repository and its contents.

Creating and building documentation does not validate a running node or deploy software to a producer. A hosted documentation website is a separate publication step.

## Published result

- Public repository: https://github.com/pgarciagon/koinos-docs; default branch `main`.
- Initial commit: `01c68c5789dc881fcd8e9a68a6b3271538221564`; 217 published files and 11 service reference pages.
- Maintenance files include an English contribution guide, service-reference template, source provenance, baseline records and GitHub Actions checks.
- Existing drafts remain local and ignored; source Git history, private Knodel files, installed dependencies and generated site files were not published.
- Local validation passed: zero internal link errors, 50 documentation/example manifest checks, syntax checks for 22 JavaScript files, 23 existing example tests across seven projects, a strict MkDocs build and `git diff --check`.
- The local rendered homepage and service reference were inspected. Inherited broken navigation and example links were repaired; source and runtime behavior were not re-audited.
- [GitHub Actions run](https://github.com/pgarciagon/koinos-docs/actions/runs/36729924061) completed successfully and produced a `documentation-site` build artifact.
- GitHub's commit matched the local commit; selected files were verified through anonymous raw access. The public tree contained no local drafts, generated site or dependency directories. The consolidated source checkout remained clean.

This publishes a repository and a downloadable site build artifact. A hosted website and new behavioral verification of the inherited documentation remain separate work.
