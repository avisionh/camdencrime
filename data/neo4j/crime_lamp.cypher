// Data from:
//  - src/make_data/03_graph_crime.py
//  - src/make_data/graph_lamp.py

// Load ward and crime data
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///df_crime.csv" AS csvLine
MATCH (w:Ward {name: csvLine.ward_name, population: csvLine.population})
CREATE (c:Crime {event_date: csvLine.outcome_date,
                 category: csvLine.category,
                 number_of_incidences: csvLine.crime_incidences,
                 rate: csvLine.crime_rate})
CREATE (w)-[:HAS_EVENT]->(c);

// Load ward and lamp data
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///df_lamp.csv" AS csvLine
MATCH (w:Ward {name: csvLine.ward_name})
CREATE (l:Lighting {lamp_type: csvLine.lamp_type,
                    event_date: csvLine.date,
                    number_of_lamps: csvLine.count_lamps,
                    mean_lamp_wattage: csvLine.mean_wattage})
CREATE (w)-[:HAS_FEATURE]->(l);
