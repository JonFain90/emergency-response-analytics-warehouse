# OpenFEMA – DisasterDeclarationsSummaries Source Profile

## Source Information

**Source:** OpenFEMA API

**Endpoint:** `DisasterDeclarationsSummaries`

---

## Table Grain

One record represents a **single disaster declaration for a designated geographic area**.

A disaster may appear in multiple rows because declarations are issued for different counties or designated areas.

Example:

| Disaster Number | Designated Area      |
| --------------- | -------------------- |
| 3610            | Adjuntas (Municipio) |
| 3610            | Arecibo (Municipio)  |
| 3610            | Bayamón (Municipio)  |

Therefore:

* `disasterNumber` is **not unique**
* FEMA's `id` field is expected to uniquely identify each record and is the preferred primary key.

---

## Source Data Types

| Field                    | Python Types | SQL Type     | Nullable |
| ------------------------ | ------------ | ------------ | -------- |
| id                       | str          | UUID         | No       |
| disasterNumber           | int          | INTEGER      | No       |
| femaDeclarationString    | str          | VARCHAR(20)  | No       |
| state                    | str          | VARCHAR(2)   | No       |
| declarationType          | str          | VARCHAR(5)   | No       |
| declarationDate          | str          | TIMESTAMP    | No       |
| fyDeclared               | int          | INTEGER      | No       |
| incidentType             | str          | VARCHAR(50)  | No       |
| declarationTitle         | str          | TEXT         | No       |
| ihProgramDeclared        | bool         | BOOLEAN      | No       |
| iaProgramDeclared        | bool         | BOOLEAN      | No       |
| paProgramDeclared        | bool         | BOOLEAN      | No       |
| hmProgramDeclared        | bool         | BOOLEAN      | No       |
| incidentBeginDate        | str          | TIMESTAMP    | No       |
| incidentEndDate          | str / None   | TIMESTAMP    | Yes      |
| disasterCloseoutDate     | str / None   | TIMESTAMP    | Yes      |
| tribalRequest            | bool         | BOOLEAN      | No       |
| fipsStateCode            | str          | VARCHAR(2)   | No       |
| fipsCountyCode           | str          | VARCHAR(3)   | No       |
| placeCode                | str          | VARCHAR(10)  | No       |
| designatedArea           | str          | VARCHAR(100) | No       |
| declarationRequestNumber | str          | VARCHAR(10)  | No       |
| lastIAFilingDate         | None         | TIMESTAMP    | Yes      |
| incidentId               | str          | VARCHAR(20)  | No       |
| region                   | int          | INTEGER      | No       |
| designatedIncidentTypes  | str / None   | VARCHAR(50)  | Yes      |
| lastRefresh              | str          | TIMESTAMP    | No       |
| hash                     | str          | VARCHAR(40)  | No       |

---

## Profiling Summary

### Sample Size

1,000 records

### Key Findings

* `disasterNumber` is **not unique** (473 unique values in a sample of 1,000 rows).
* Several date fields are nullable.
* Boolean fields are consistently typed.
* String lengths are small and predictable.
* The endpoint returns a flat JSON structure with no nested objects or arrays.

---

## Raw Layer Design Principles

* Preserve all source fields.
* Maintain one-to-one correspondence with the API.
* Use FEMA's `id` field as the primary key.
* Add an `ingested_at` timestamp for lineage and auditing.
