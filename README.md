# Koinos node coordination

[Public repository](https://github.com/pgarciagon/koinos_legacy_node)

## Purpose

This project coordinates improvements and updates to the base software required to run Koinos producer nodes.

It centralizes analysis, proposals, decisions and change tracking across the node repositories. The starting point is the set of services launched through Docker.

## Main references

- [Koinos public organization](https://github.com/koinos): hosts the ecosystem repositories; it is not a single code repository.
- [koinos/koinos](https://github.com/koinos/koinos): the integration repository for launching Koinos services through Docker.

## Service documentation

The [public Koinos architecture documentation](https://github.com/koinos/koinos-docs/tree/master/docs/architecture) describes the microservices and their internal communication. This project's [inventory](docs/inventory/2026-09-30-inventory.md) records the specific versions reviewed.

The local environment keeps additional technical references and a comparison with the private Knodel project in `LOCAL_REFERENCES.md` and `docs/comparisons/`. These files are excluded from the public repository.

## Workflow

All repository documentation is maintained in English.

1. Identify the problem or update and the affected components.
2. Document the analysis and proposal before implementation.
3. Make changes in the relevant repositories and record their references here.
4. Verify component compatibility and node behavior with tests appropriate to the change.
5. Record results, limitations and the steps required for adoption.

## Project status

The project purpose was established on September 28, 2026. The Docker deployment's [component, version and dependency inventory](docs/inventory/2026-09-30-inventory.md) was completed on September 30, with evidence from GitHub and Docker Hub.

The analysis identifies 12 services and proposes initial improvements to reproducibility, operational health, builds and ARM64 support. It recommends validating the version set and preventing silent selection of `latest` as the first scoped contribution to the integration repository. It also identifies a WASM memory PR in `chain` for priority review.

The improvements remain proposals. Verification covers source code, image metadata and Compose configuration resolution; no builds or node tests have been run yet. Public reference repositories are kept in `upstream/`, which is excluded from Git.

The state replay fix in [chain #861](https://github.com/koinos/koinos-chain/pull/861) is already included in legacy chain `v1.5.2`. Research into future improvements will cite public sources and explicitly distinguish proposals, implementation and validation.

Upstream source excerpts and manifests retain their original licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
