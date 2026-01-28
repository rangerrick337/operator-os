# SOP: Convert PDFs to Markdown

## Goal
Convert PDF documents to well-structured Markdown files using AI-powered extraction.

## Context
PDFs often contain valuable content locked in an uneditable format. This SOP uses the `pdf-conversion` skill to extract text, preserve structure, and output clean Markdown.

## Inputs
- **PDF Files**: Located in `Drive - ProjectX/PDFs/` or specified directory
- **Configuration**: Optional settings for extraction quality, chunking

## Outputs
- **Markdown Files**: One `.md` file per PDF in `Drive - ProjectX/Markdown/`
- **Metadata**: JSON file with conversion details (page count, processing time)

## Process

### 1. Locate PDFs
- Scan the input directory for `.pdf` files
- Create list of files to process
- Check for existing markdown files to avoid re-processing

### 2. Convert Each PDF
- Use `Operator Team OS/3. Skills/pdf-conversion/` skill
- Extract text while preserving:
  - Headings and hierarchy
  - Lists and tables
  - Links (where possible)
  - Image descriptions

### 3. Post-Processing
- Clean up formatting artifacts
- Normalize heading levels
- Add frontmatter (title, source, date)

### 4. Validation
- Verify markdown file was created
- Check file size is reasonable
- Spot-check content accuracy

### 5. Organization
- Save to output directory
- Generate index file listing all converted documents
- Move processed PDFs to archive (optional)

## Edge Cases
- **Scanned PDFs (images)**: May require OCR - skill will handle this
- **Password-protected PDFs**: Cannot process - skip and log
- **Corrupt PDFs**: Log error and continue with next file
- **Very large PDFs**: May timeout - consider splitting

## Expected Output
- Clean Markdown files preserving document structure
- Metadata file with conversion details
- Processing log with any errors or warnings

## Skills Used
- `Operator Team OS/3. Skills/pdf-conversion/`
