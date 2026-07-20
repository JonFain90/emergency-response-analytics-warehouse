import requests

BASE_URL = (
    "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
)


def get_disaster_declarations(limit=1000, skip=0):
    """
    Retrieve one page of FEMA disaster declarations.

    Parameters
    ----------
    limit : int
        Number of records to retrieve.
    skip : int
        Number of records to skip.

    Returns
    -------
    list
        List of disaster declaration records.
    """

    params = {
        "$top": limit,
        "$skip": skip
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return data["DisasterDeclarationsSummaries"]


def get_all_disaster_declarations(page_size=1000):
    """
    Retrieve all FEMA disaster declarations using pagination.
    """

    all_records = []

    skip = 0

    while True:

        records = get_disaster_declarations(
            limit=page_size,
            skip=skip
        )

        print(f"Retrieved {len(records)} records (skip={skip})")

        if len(records) == 0:
            break

        all_records.extend(records)

        skip += page_size

    return all_records