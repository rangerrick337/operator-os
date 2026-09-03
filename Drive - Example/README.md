# Example Drive Folder

This folder represents **Layer 5: Knowledge** in the six-layer architecture.

## What Goes Here

- **Input Data**: CSVs, JSON files, raw data for processing
- **Output Data**: Processed files, reports, generated documents
- **Reference Materials**: PDFs, markdown docs, research notes
- **Artifacts**: Any deliverables the AI generates for you

## Structure

Organize this however makes sense for your project. Examples:

```
Drive - ProjectX/
├── Data/
│   ├── input/
│   └── output/
├── Reports/
├── Documents/
└── Research/
```

## Important Notes

1. **Permission boundary**: Keep restricted knowledge in a separate `Drive - *`
   library and never merge differently permissioned libraries into one index.
2. **Not agent policy**: Agents may read or write authorized files here, but
   instructions, skills, and workflows belong in `Operator Team OS/`.
3. **Excluded from Git**: `.gitignore` excludes `Drive - *` contents by default to
   reduce the chance of publishing business data.
4. **Portable paths**: Use repository-relative paths or explicit configuration;
   never store a named home directory in shared files.

## Example File

See `sample-data.csv` for a simple example of data that might live here.
