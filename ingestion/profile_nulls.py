from fema_api import get_disaster_declarations
import pandas as pd

records = get_disaster_declarations(1000)

df = pd.DataFrame(records)

null_pct = (
    df.isnull()
      .mean()
      .sort_values(ascending=False)
      * 100
)

print(null_pct)