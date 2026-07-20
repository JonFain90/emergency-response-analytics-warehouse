from database import get_connection
from psycopg2.extras import execute_values


INSERT_SQL = """
INSERT INTO raw.disaster_declarations (
    id,
    fema_declaration_string,
    disaster_number,
    state,
    declaration_type,
    declaration_date,
    fy_declared,
    incident_type,
    declaration_title,
    ih_program_declared,
    ia_program_declared,
    pa_program_declared,
    hm_program_declared,
    incident_begin_date,
    incident_end_date,
    disaster_closeout_date,
    tribal_request,
    fips_state_code,
    fips_county_code,
    place_code,
    designated_area,
    declaration_request_number,
    last_ia_filing_date,
    incident_id,
    region,
    designated_incident_types,
    last_refresh,
    hash
)
VALUES %s
ON CONFLICT (id)
DO NOTHING;
"""


def prepare_record(record):

    return (
        record["id"],
        record["femaDeclarationString"],
        record["disasterNumber"],
        record["state"],
        record["declarationType"],
        record["declarationDate"],
        record["fyDeclared"],
        record["incidentType"],
        record["declarationTitle"],
        record["ihProgramDeclared"],
        record["iaProgramDeclared"],
        record["paProgramDeclared"],
        record["hmProgramDeclared"],
        record["incidentBeginDate"],
        record.get("incidentEndDate"),
        record.get("disasterCloseoutDate"),
        record["tribalRequest"],
        record["fipsStateCode"],
        record["fipsCountyCode"],
        record["placeCode"],
        record["designatedArea"],
        record["declarationRequestNumber"],
        record.get("lastIAFilingDate"),
        record["incidentId"],
        record["region"],
        record.get("designatedIncidentTypes"),
        record["lastRefresh"],
        record["hash"]
    )


def load_disaster_declarations(records):

    conn = get_connection()
    cur = conn.cursor()

    try:

        rows = []

        for record in records:
            rows.append(
                prepare_record(record)
            )

        execute_values(
            cur,
            INSERT_SQL,
            rows
        )

        conn.commit()

        print()
        print("-------------------------")
        print("Bulk load complete")
        print(f"Records received: {len(records)}")
        print("-------------------------")

    except Exception as e:

        conn.rollback()
        raise e

    finally:

        cur.close()
        conn.close()