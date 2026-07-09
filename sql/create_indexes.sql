CREATE INDEX idx_disaster_number
ON raw.disaster_declarations(disaster_number);

CREATE INDEX idx_state
ON raw.disaster_declarations(state);

CREATE INDEX idx_declaration_date
ON raw.disaster_declarations(declaration_date);

CREATE INDEX idx_incident_type
ON raw.disaster_declarations(incident_type);