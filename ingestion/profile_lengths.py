from fema_api import get_disaster_declarations
import pandas as pd

records = get_disaster_declarations(1000)

df = pd.DataFrame(records)

for col in df.select_dtypes(include="object"):
    max_len = df[col].astype(str).str.len().max()
    print(f"{col}: {max_len}")