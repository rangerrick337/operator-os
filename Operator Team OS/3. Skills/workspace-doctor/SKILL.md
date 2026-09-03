---
name: workspace-doctor
description: Run a read-only health check of Operator OS structure, canonical pointers, release metadata, memory folders, unsafe symlinks, and machine-specific paths.
allowed-tools: [read_file, list_directory, shell]
---

# Workspace Doctor

Run from the repository root:

```bash
python3 "Operator Team OS/3. Skills/workspace-doctor/scripts/operator_doctor.py"
```

The doctor is read-only. A failure is a punch list, not authorization to fix or
delete anything. Report every failed check and the exact remediation path.
