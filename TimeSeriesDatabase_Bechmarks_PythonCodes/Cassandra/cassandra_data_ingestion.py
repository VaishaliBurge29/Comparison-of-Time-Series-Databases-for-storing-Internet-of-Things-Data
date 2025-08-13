# ------------------------------------------
# Inserting CSV Data into Cassandra 
# ------------------------------------------

from cassandra.cluster import Cluster
import csv
import time

# Connect to Cassandra cluster
# Replace '127.0.0.1' with your VM IP if running remotely
cluster = Cluster(['127.0.0.1'])
# Connect to the target keyspace
session = cluster.connect('sensor_data')  # Change 'sensor_data' to your keyspace

# Prepare the CQL INSERT statement
# Use placeholders (%s) for parameterized queries to avoid manual string formatting
insert_query = """
INSERT INTO sensor_readings (dataset_size, sensor_id, timestamp, value)
VALUES (%s, %s, %s, %s)
"""

# Label for dataset size (helps differentiate datasets in the same table)
dataset_size = "500k_rows"  # Change this to "2k_rows" or "5_rows" for other datasets

# Start timing ingestion
start_time = time.time()

# Read and insert data from CSV file
# CSV must contain columns: sensor_id, timestamp, value
with open('../data/500k_datapoints.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    for row in reader:
        # Execute INSERT with parameters
        session.execute(
            insert_query,
            (
                dataset_size,                  # dataset size label
                int(row['sensor_id']),         # sensor ID as integer
                row['timestamp'],              # timestamp string (Cassandra supports ISO-8601)
                float(row['value'])             # measurement value as float
            )
        )
        count += 1

# Stop timing
end_time = time.time()
elapsed_time = end_time - start_time

# Output ingestion stats
print(f"Inserted {count} rows in {elapsed_time:.3f} seconds.")
