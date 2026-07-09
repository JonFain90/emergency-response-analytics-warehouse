# OpenFEMA DisasterDeclarationsSummaries Endpoint

## Source

OpenFEMA API

Endpoint:
https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries

## Description

Contains FEMA disaster declaration records, including declaration dates, incident types, geographic areas, and declaration metadata.

## Observed Fields

| Field             | Python Type(s) | Nullable | Proposed SQL Type | Notes                           |
| ----------------- | -------------- | -------- | ----------------- | ------------------------------- |
| disasterNumber    | int            | No       | INTEGER           | FEMA disaster identifier        |
| declarationDate   | str            | No       | TIMESTAMP         | ISO-8601 datetime               |
| incidentBeginDate | str, NoneType  | Yes      | TIMESTAMP         | May be null                     |
| incidentEndDate   | str, NoneType  | Yes      | TIMESTAMP         | May be null                     |
| state             | str            | No       | VARCHAR(2)        | State or territory abbreviation |
| incidentType      | str            | No       | VARCHAR(100)      | Disaster category               |
| declarationTitle  | str            | Yes      | TEXT              | Description of declaration      |
| designatedArea    | str            | Yes      | TEXT              | Geographic area                 |
| fyDeclared        | int            | No       | INTEGER           | Fiscal year                     |
| declarationType   | str            | Yes      | VARCHAR(50)       | Type of declaration             |
| fipsStateCode     | str            | Yes      | VARCHAR(10)       | FIPS state code                 |
| fipsCountyCode    | str            | Yes      | VARCHAR(10)       | FIPS county code                |
| placeCode         | str            | Yes      | VARCHAR(20)       | FEMA place code                 |
| hash              | str            | Yes      | TEXT              | Record hash from source         |

## Profiling Notes

* Dates arrive as strings and will need to be cast by PostgreSQL.
* Several fields are nullable.
* This endpoint appears to return flat JSON (no nested arrays or objects).
* Future profiling should evaluate:

  * uniqueness of disasterNumber
  * duplicate records
  * update frequency
  * maximum string lengths
