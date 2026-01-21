# List invenio records

Use InvenioRDM API to retrieve all current, **public** records on https://archive.nfdi4plants.org and store them as tables (xlsx and csv).

## Run locally

1. (Install dependencies from `requirements.txt`)
2. Run
```bash
python list-invenio-records.py
```

## Run via GitHub Action

This is done automatically every Monday as defined in the [GH workflow](.github/workflows/run-invenio-download.yml)

To run this in GitHub

1. Click Actions
2. Click “Download Invenio Records”
3. Click “Run workflow” and wait.
4. The files should be committed to repo by github-actions[bot]
