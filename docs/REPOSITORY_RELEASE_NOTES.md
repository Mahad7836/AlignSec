# Repository release notes

## Publication-ready repository pass

This repository layout was rebuilt from the frozen AlignSec technical package without changing the scientific benchmark, final response dataset, primary results, or statistical outputs.

Repository-level cleanup includes:

- current-path model provenance with SHA-256 hashes;
- a current repository manifest and repository checksum list;
- explicit separation of historical technical-package manifests from current repository metadata;
- a data dictionary;
- an attack taxonomy;
- inference and output documentation;
- third-party attribution notes;
- manuscript-to-artifact mapping;
- an expanded integrity verifier;
- explanatory manuscript diagrams and editable SVG sources;
- a lightweight GitHub Actions verification workflow.

Historical generated artifacts that contain the earlier `EAAI` development label are preserved unchanged where editing them would break traceability to the frozen analysis. Publication-facing documentation is journal-neutral and the associated manuscript is being prepared for the *Journal of Information Security and Applications (JISA)*.

## Remaining release metadata

Before creating the archival `v1.0.0` release, synchronize `CITATION.cff` with the final manuscript author order and add the archival DOI after it is assigned. These are publication metadata tasks and do not affect the frozen scientific results.
