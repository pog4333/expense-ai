# Project Status

Project

AI Expense Assistant

Status

Sprint 1

---

# Current Goal

Build the project foundation before introducing AI.

---

# Sprint Backlog

## Completed

- Selected uv as the package/project manager.
- Initialized Git repository.
- Created the project.
- Configured virtual environment.
- Discussed deterministic pipelines.
- Designed the first document-processing pipeline.

---

## In Progress
## Current Assignment

Issue #4

Status: In Progress

Deliverable:
A working PDFExtractor.

Definition of Done:

- [ ] Opens PDF
- [ ] Reads page count
- [ ] Reads first page
- [ ] Handles errors
- [ ] Code reviewed



---

## Next Tasks

1. Review project structure.
2. Decide between `src/` and `app/`.
3. Install project dependencies.
4. Read the first PDF using PyMuPDF.
5. Detect whether a PDF is scanned or digital.
6. Write the first automated test.

---

# Acceptance Criteria

Sprint 1 is complete when:

- The project builds successfully.
- Dependencies are managed with uv.
- A PDF can be opened.
- The number of pages can be read.
- Text can be extracted from a digital PDF.

---

# Open Questions

- Keep `src/`?
- Remove `requirements.txt`?
- Final folder structure?

---

# Session Notes

Session 1

- Learned deterministic vs AI.
- Learned digital PDF vs scanned PDF.
- Learned why OCR exists.
- Learned why pipelines matter.

---

# Next Session

Start implementing PDF extraction.