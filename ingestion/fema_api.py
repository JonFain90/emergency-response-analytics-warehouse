import requests

BASE_URL = (
    "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
)


def get_disaster_declarations(limit=5):

    params = {
        "$top": limit
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return data["DisasterDeclarationsSummaries"]