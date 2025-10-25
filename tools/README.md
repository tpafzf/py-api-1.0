# Developer Tools

This directory contains scripts and utilities for local development.

## Scripts

### `test_nfl_data.py`
Tests the nfl-data-py installation and displays available functionality.

**Usage:**
```bash
python tools/test_nfl_data.py
```

### `export_requirements.py`
Exports the conda environment to `requirements.txt` for containerization.

**Usage:**
```bash
python tools/export_requirements.py
```

This creates a `requirements.txt` file in the project root that can be used with Docker or standard Python virtual environments.

## Containerization Workflow

When you're ready to containerize:

1. **Export requirements:**
   ```bash
   python tools/export_requirements.py
   ```

2. **Rename Dockerfile:**
   ```bash
   mv Dockerfile.example Dockerfile
   ```

3. **Build the image:**
   ```bash
   docker build -t madden-api .
   ```

4. **Run the container:**
   ```bash
   docker run -p 5000:5000 madden-api
   ```

## Notes

- These tools are for **local development only** and should not be included in production builds
- The `.dockerignore` file already excludes this directory from Docker builds

