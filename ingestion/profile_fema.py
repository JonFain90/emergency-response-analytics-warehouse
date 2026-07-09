from fema_api import get_disaster_declarations
from collections import defaultdict

records = get_disaster_declarations(1000)

field_types = defaultdict(set)

for row in records:
    for key, value in row.items():
        field_types[key].add(type(value).__name__)

for key in sorted(field_types):
    print(f"{key}: {field_types[key]}")