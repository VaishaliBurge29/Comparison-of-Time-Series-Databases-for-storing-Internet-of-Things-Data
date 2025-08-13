# ------------------------------------------
# Query 6: Hourly Aggregation in Pandas
# ------------------------------------------

import time
import pandas as pd
from cassandra.cluster import Cluster

# Start timing for performance measurement
start_time = time.time()

# Connect to Cassandra
cluster = Cluster()
session = cluster.connect('sensor_data')  # Replace with your keyspace name if different

# Query: Fetch all timestamped values for a given day for sensor_id=6 in '5_rows' dataset
rows = session.execute("""
    SELECT timestamp, value FROM sensor_readings
    WHERE dataset_size = '5_rows'
    AND sensor_id = 6
    AND timestamp >= '2024-02-07 00:00:00'
    AND timestamp <  '2024-02-08 00:00:00';
""")

# Convert query results to a Pandas DataFrame
df = pd.DataFrame(rows)

# Ensure 'timestamp' column is treated as a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the hour component (rounded down) for grouping
df['hour'] = df['timestamp'].dt.floor('H')

# Group by hour and compute the average value per hour
hourly_avg = df.groupby('hour')['value'].mean()

# Stop timing
end_time = time.time()
elapsed = end_time - start_time

# Output results
print("Hourly average values:")
print(hourly_avg)
print(f"\nQuery executed in {elapsed:.4f} seconds")
