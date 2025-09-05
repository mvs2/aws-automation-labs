# AWS Automation Labs

![Learning in Public](https://img.shields.io/badge/Learning%20in%20Public-🚀-orange)

Learning project for practicing Python + AWS automation using the Free Tier.

## Phase 1 — Warm-Up (Automation Basics → AWS Glue)

- [x] **S3 Uploader/Downloader**
  - [x] Upload
  - [x] Verify via `head_object`
  - [x] Download + size check
  - [x] Retries
 
  
- [ ] **EC2 Inventory**
  - [ ] List EC2 instances (ID, type, state, region, tags)
  - [ ] Export to JSON/CSV
  - [ ] Flag “stale” instances and store report in S3

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
## Quickstart
1. Clone repo
2. Copy `config/default.yaml.example` → `config/default.yaml` and set your bucket + region
3. Run: `python -m aws_automation_labs.s3io`  
