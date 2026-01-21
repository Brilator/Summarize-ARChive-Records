import requests
import pandas as pd
import datetime
from pathlib import Path

INVENIO_API_URL = "https://archive.nfdi4plants.org/api/records"
PAGE_SIZE = 100

TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
OUT_DIR = Path("data")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_XLSX = OUT_DIR / f"{TODAY}_invenio-records.xlsx"
OUT_CSV = OUT_DIR / f"{TODAY}_invenio-records.csv"

def extract_identifier(identifiers, scheme):
    for i in identifiers or []:
        if i.get("scheme") == scheme:
            return i.get("identifier")
    return ""

def format_creators(creators):
    names = []
    for c in creators or []:
        person = c.get("person_or_org", {})
        name = person.get("name")
        if name:
            names.append(name)
    return " and ".join(names)


all_records = []
page = 1

while True:
    params = {
        "page": page,
        "size": PAGE_SIZE
    }

    r = requests.get(INVENIO_API_URL, params=params)
    r.raise_for_status()
    data = r.json()

    hits = data["hits"]["hits"]
    if not hits:
        break

    for rec in hits:
        metadata = rec.get("metadata", {})

        identifiers = metadata.get("identifiers", [])
        dates = metadata.get("dates", [])

        all_records.append({
            "ID": rec.get("id"),
            "RecordDOI": rec.get("links", {}).get("self_doi"),
            "RecordURL": rec.get("links", {}).get("self_html"),

            "Title": metadata.get("title"),
            "PublicationDate": metadata.get("publication_date"),

            "Authors": format_creators(metadata.get("creators")),
            
            "ARCURL": extract_identifier(identifiers, "url")

        })

    page += 1

df = pd.DataFrame(all_records)

df.to_excel(OUT_XLSX, index=False)
df.to_csv(OUT_CSV, index=False)

print(f"Saved {len(df)} records to {OUT_XLSX} and {OUT_CSV}")

