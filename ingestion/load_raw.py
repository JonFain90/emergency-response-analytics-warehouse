from database import get_connection

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
VALUES (
    %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s
)
ON CONFLICT (id)
DO NOTHING;
"""


def load_disaster_declarations(records):
    """
    Loads FEMA disaster declaration records into the
    raw.disaster_declarations table.

    Existing records (based on the primary key 'id')
    are skipped automatically.
    """

    conn = get_connection()
    cur = conn.cursor()

    inserted = 0
    skipped = 0

    try:

        for record in records:

            cur.execute(
                INSERT_SQL,
                (
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
            )

            if cur.rowcount == 1:
                inserted += 1
            else:
                skipped += 1

        conn.commit()

        print()
        print("Load Summary")
        print("----------------------")
        print(f"Records received : {len(records)}")
        print(f"Inserted         : {inserted}")
        print(f"Skipped          : {skipped}")
        print()

    except Exception as e:

        conn.rollback()

        print("ERROR loading records.")
        raise e

    finally:

        cur.close()
        conn.close()