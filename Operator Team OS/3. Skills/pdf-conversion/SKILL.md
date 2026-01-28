---
name: pdf-conversion
description: "Convert PDF documents to well-structured Markdown files. Use when user asks
to convert PDFs, extract text from PDFs, or transform PDF documents to markdown format."
---
# PDF Conversion Skill

## Overview
Converts PDF files to clean, readable Markdown format with proper formatting, image extraction, and table preservation.

## When to Use
- "Convert this PDF to markdown"
- "Extract text from PDF"
- "Transform PDF to MD format"
- "Process PDFs in folder X"

## Related Resources
- **SOP**: `Operator Team OS/1. SOPs/convert_pdfs_to_markdown.md`

## Scripts

| Script | Purpose |
|--------|---------|
| `pdf_to_md.py` | Main PDF to Markdown converter |

## Usage

```bash
python3 scripts/pdf_to_md.py /path/to/input.pdf /path/to/output.md
```

## Features
- Text extraction with OCR fallback
- Image extraction and embedding
- Table detection and formatting
- Heading structure preservation
- Automatic cleanup of formatting artifacts

## Edge Cases
- **Scanned PDFs**: Falls back to OCR
- **Complex tables**: Best-effort conversion
- **Encrypted PDFs**: Will fail (requires password)
