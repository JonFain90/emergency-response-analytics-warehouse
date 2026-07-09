from fema_api import get_disaster_declarations
import json

records = get_disaster_declarations(5)

print(json.dumps(records[0], indent=4))