# AWS Automation Labs

Learning project for practicing Python + AWS automation using the Free Tier.

## Phase 1 — Warm-Up (Automation Basics → AWS Glue)

- [ ] **S3 Uploader/Downloader**
  - Upload, list, and download files from S3
  - Add retries, progress bars, and checksum validation

- [ ] **EC2 Inventory**
  - List EC2 instances (ID, type, state, region, tags)
  - Export to JSON/CSV
  - Flag “stale” instances and store report in S3

## Planned Phases

- Phase 2: (to be defined)
- Phase 3: (to be defined)

## Repo Layout

- `src/` — source code for each task (`s3_tools`, `ec2_inventory`, etc.)
- `config/` — YAML configs (default + optional profiles)
- `docs/` — decisions, notes, and phase documentation
- `reports/` — local output artifacts before pushing to S3
- `tests/` — test files for validation

---

*This repo is part of my AWS Cloud + Python learning journey.*
