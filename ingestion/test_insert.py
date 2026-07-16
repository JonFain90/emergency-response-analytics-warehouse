from fema_api import get_disaster_declarations
from load_raw import insert_one_disaster

records = get_disaster_declarations(1)

insert_one_disaster(records[0])

print("Insert successful!")