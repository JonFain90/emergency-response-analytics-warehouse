from fema_api import get_disaster_declarations
import pandas as pd

records = get_disaster_declarations(1000)

df = pd.DataFrame(records)

print(f"Rows: {len(df)}")
print(f"Unique disaster numbers: {df['disasterNumber'].nunique()}")