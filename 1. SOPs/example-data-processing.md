# SOP: Data Processing Template

## Goal
Process CSV data files from the Drive folder, perform transformations, and output results to a specified location.

## Context
This is a template SOP showing how to structure process documentation for data tasks. Replace the specifics with your actual use case.

## Inputs
- **Source File**: `Drive - ProjectX/Data/input.csv`
- **Required Columns**: `name`, `email`, `company`
- **Parameters**: Any filters or transformation rules

## Outputs
- **Processed File**: `Drive - ProjectX/Data/output.csv`
- **Log File**: `z_temp/processing_log.txt`

## Process

### 1. Validation
- Check that source file exists
- Verify required columns are present
- Validate data types and format

### 2. Transformation
- Clean data (remove duplicates, fix formatting)
- Apply business logic (calculations, categorization)
- Enrich data if needed (lookups, API calls)

### 3. Quality Checks
- Verify row counts
- Check for missing critical data
- Validate against business rules

### 4. Output
- Write processed data to output location
- Generate summary statistics
- Log any errors or warnings

### 5. Cleanup
- Move intermediate files to `z_temp/`
- Archive processed files if needed
- Update processing log

## Edge Cases
- **Missing columns**: Halt and notify user
- **Invalid data**: Log errors, skip bad rows, continue processing
- **API failures**: Retry with exponential backoff, max 3 attempts
- **Large files**: Process in chunks to avoid memory issues

## Expected Output
- Clean, validated output file
- Processing log with statistics
- Error report if any issues occurred

## Skills/Tools Used
- `3. Skills/data-processing/` (if exists)
- Python pandas for data manipulation
- Standard logging utilities
