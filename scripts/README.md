# Scripts

This folder contains utility scripts for maintaining the AWS Solution Architect study materials.

## Available Scripts

### 🔍 `validate_mermaid.py`

Validates all Mermaid diagrams in the repository for syntax issues and rendering problems.

**Usage:**
```bash
cd /path/to/AWS-Solution-Architect
python3 scripts/validate_mermaid.py
```

**What it checks:**
- Quoted subgraph syntax (old format)
- Unescaped HTML operators (`<`, `>`)
- Unquoted special characters
- Mismatched quotes
- Old-style `style` statements
- Style statements in sequence diagrams
- Improper indentation
- Floating nodes (warning only)

**Exit codes:**
- `0` - All validations passed
- `1` - Critical errors found

---

### 🔧 `fix_mermaid.py`

Automatically fixes common Mermaid diagram syntax issues.

**Usage:**
```bash
cd /path/to/AWS-Solution-Architect
python3 scripts/fix_mermaid.py
```

**What it fixes:**
- Converts quoted subgraph syntax to ID-based syntax
- Escapes `<` and `>` as HTML entities (preserves `<br/>`)
- Removes style statements from sequence diagrams
- Converts old `style` statements to `classDef`/`class`
- Adds quotes around nodes with special characters

**Note:** Always review changes with `git diff` before committing.

---

### 📋 `fix_diagrams.py`

Legacy script for diagram fixes (superseded by `fix_mermaid.py`).

---

## Quick Start

1. **Validate all diagrams:**
   ```bash
   python3 scripts/validate_mermaid.py
   ```

2. **Auto-fix common issues:**
   ```bash
   python3 scripts/fix_mermaid.py
   ```

3. **Review changes:**
   ```bash
   git diff
   ```

4. **Validate again:**
   ```bash
   python3 scripts/validate_mermaid.py
   ```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Documentation

For detailed information about validation rules, best practices, and troubleshooting, see:
- [Mermaid Validation Guide](../docs/MERMAID-VALIDATION-GUIDE.md)

## CI/CD Integration

Add to your CI pipeline (`.github/workflows/validate.yml`):

```yaml
name: Validate Diagrams

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Validate Mermaid Diagrams
        run: python3 scripts/validate_mermaid.py
```

## Contributing

When adding new validation rules:

1. Update `validate_mermaid.py` with detection logic
2. Update `fix_mermaid.py` with auto-fix logic (if applicable)
3. Add examples to the [Validation Guide](../docs/MERMAID-VALIDATION-GUIDE.md)
4. Test with real diagrams before committing

## License

Same as parent repository (see [LICENSE](../LICENSE))

