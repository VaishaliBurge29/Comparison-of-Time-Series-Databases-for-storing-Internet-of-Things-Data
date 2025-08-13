from pydruid.db import connect  # PyDruid library for connecting to Druid via SQL
import time                     # For measuring query execution time

start = time.time()  # Start timer to measure query latency

# Connect to Druid's SQL endpoint
conn = connect(
    host='localhost',           # Hostname or IP of the Druid Broker (replace with <vm-ip> if remote)
    port=8082,                   # Default Druid SQL/Broker port
    path='/druid/v2/sql/',       # API path for Druid SQL queries
    scheme='http'                # Protocol ('http' or 'https')
)

# Create a cursor to execute SQL queries
curs = conn.cursor()

# Execute the SQL query
# NOTE: Change table name and time range to match your dataset and test scenario
curs.execute("""
    SELECT
      __time AS "timestamp",                 -- Druid's internal time column (aliased for clarity)
      "value",                                -- Numeric value field from ingested data
      "sensor_id"                             -- Dimension column
    FROM "sensor_data_500rows"                -- Table/Datasource name (update for other datasets)
    WHERE __time >= TIMESTAMP '2024-02-01 00:00:00'  -- Start time filter
      AND __time <= TIMESTAMP '2024-02-10 23:59:59'  -- End time filter
""")

# Fetch all query results
rows = curs.fetchall()

# Print results row-by-row
for row in rows:
    print(row)

# Stop timer and print query execution time
end = time.time()
print(f"\n Query time: {end - start:.4f} seconds")
