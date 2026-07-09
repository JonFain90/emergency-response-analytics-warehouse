from fema_api import get_disaster_declarations
import pandas as pd

records = get_disaster_declarations(1000)

df = pd.DataFrame(records)

candidate_keys = [
    ["disasterNumber"],
    ["disasterNumber", "designatedArea"],
    ["disasterNumber", "placeCode"],
    ["disasterNumber", "fipsCountyCode"],
    ["id"]
]

for cols in candidate_keys:
    unique_rows = df[cols].drop_duplicates().shape[0]
    print(
        f"{cols}: "
        f"{unique_rows} unique of {len(df)} rows"
    )