---
name: make-pdfs
description: Read, create, modify, and visually verify PDFs — extraction with the right tool per document type, source-format rendering, image-level verification before delivery. Use when the user asks to read, make, merge, fill, or check PDF files.
metadata:
  tool_categories: coding
---

# make-pdfs — PDF: read, create, modify, visually verify

## Core stance

PDFs are an output medium, not a working format. The reliable pattern: work in a source format (HTML, LaTeX, docx), render to PDF, then verify visually. Never hand-edit PDFs when you can regenerate from source. Reading PDFs is a different skill from making them — separate toolchains, separate failure modes.

## Reading

- Extract text with pdftotext (poppler) for prose; use layout mode (`-layout`) for tables and columns.
- Structured extraction: pdfplumber for tables (returns real cell grids), PyMuPDF (fitz) for text+position metadata and images.
- **Scanned PDFs have no text layer** — detect this (empty extraction on non-empty pages) and OCR (tesseract) or report the limitation. Never silently return empty.
- Forms: pdftk or pypdf to read field names; fill with the same.
- Verify extraction completeness: page count of extracted text vs. page count of the document. Gaps mean scanned pages, images-as-text, or failure — say which.

## Creating

- **From HTML:** generate HTML+CSS, render with weasyprint (or wkhtmltopdf). Best for styled documents, letters, reports. Full CSS: page size, margins via @page, page numbers via CSS counters.
- **From LaTeX:** for technical/academic documents needing typeset math and precise layout. pdflatex/tectonic.
- **From docx:** generate with python-docx, convert with libreoffice --headless --convert-to pdf. Best when the user wants an editable companion file.
- **Programmatic:** reportlab for precise layout control (tables, exact positioning).
- **Merge/split/pages:** pypdf. Never reconstruct pages you can manipulate directly.

## Visual verification

PDF rendering fails silently: fonts substitute, tables overflow, images drop. Before delivering:

1. Render pages to images: `pdftoppm -png -r 100 output.pdf page` (poppler).
2. Look at the images — every page for short docs, sample pages for long ones.
3. Check: text overflow past margins, truncated table columns, missing/shifted glyphs, image placement, page breaks in the wrong place.
4. Fix at the source, re-render, re-verify. Never deliver an unverified PDF.

## Modifying existing PDFs

- Identify the modification type first: form fill (pypdf/pdftk), page ops (pypdf), content edits (regenerate from source when possible; direct edit is fragile and last resort).
- After any modification, re-verify visually — page ops can silently drop or duplicate pages.
- State the provenance of the output: which source file, which pages, which operations.

## Failure modes to check for

- Text extraction returns empty/garbled → scanned PDF, try OCR.
- Fonts substituting → embed fonts at creation; check after render.
- Tables extracted as linear text → use pdfplumber, not pdftotext.
- Page count mismatch after merge → silent page drop, re-do.
