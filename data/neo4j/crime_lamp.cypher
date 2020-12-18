// Data from:
//  - src/make_data/graph_ward.py
//  - src/make_data/03_graph_crime.py
//  - src/make_data/graph_lamp.py

CREATE INDEX ON :Ward(name)

// Create wards to join later
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/avisionh/camdencrime/feature/graph-represent/outputs/wards.csv" AS csvLine
CREATE (w:Ward {name: csvLine.ward_name});

// Load population data
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/avisionh/camdencrime/feature/graph-represent/outputs/df_pop.csv" AS csvLine
MATCH (w:Ward {name: csvLine.ward_name})
CREATE (p: Population {population_year: csvLine.outcome_year,
                       population: csvLine.population,
                       type: "projection"})
CREATE (w)-[:HAS_POPULATION_COUNT]->(p);

// Load ward and crime data
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/avisionh/camdencrime/feature/graph-represent/outputs/df_crime.csv" AS csvLine
MATCH (w:Ward {name: csvLine.ward_name})
CREATE (c:Crime {category: csvLine.category,
                 event_date: csvLine.outcome_date,
                 number_of_incidences: csvLine.crime_incidences,
                 rate: csvLine.crime_rate})
CREATE (w)-[:HAS_EVENT]->(c);

// Load ward and lamp data
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/avisionh/camdencrime/feature/graph-represent/outputs/df_lamp.csv" AS csvLine
MATCH (w:Ward {name: csvLine.ward_name})
CREATE (l:Lighting {lamp_type: csvLine.lamp_type,
                    event_date: csvLine.date,
                    number_of_lamps: csvLine.count_lamps,
                    mean_lamp_wattage: csvLine.mean_wattage})
CREATE (w)-[:HAS_FEATURE]->(l);
