# Summarize ARChive Records

Use InvenioRDM API to retrieve all current, **public** records on https://archive.nfdi4plants.org and store them as tables (xlsx and csv).

The tool runs automatically every Monday as defined in the [GH workflow](.github/workflows/run-invenio-download.yml).

👀 Check out [data](./data) for the latest downloads.

## Trigger via GitHub Action

To run this in GitHub

1. Click [Actions](https://github.com/Brilator/Summarize-ARChive-Records/actions)
2. Click “Download Invenio Records”
3. Click “Run workflow” and wait.
4. The files should be committed to repo by github-actions[bot]

## Run locally

1. (Install dependencies from `requirements.txt`)
2. Run

```bash
python list-invenio-records.py
```
