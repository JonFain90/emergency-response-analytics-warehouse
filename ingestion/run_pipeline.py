from fema_api import get_disaster_declarations
from load_raw import load_disaster_declarations


def main():

    print("Retrieving FEMA data...")

    records = get_disaster_declarations(10)

    print(f"Retrieved {len(records)} records.")

    print("Loading into PostgreSQL...")

    load_disaster_declarations(records)

    print("Pipeline complete.")


if __name__ == "__main__":
    main()