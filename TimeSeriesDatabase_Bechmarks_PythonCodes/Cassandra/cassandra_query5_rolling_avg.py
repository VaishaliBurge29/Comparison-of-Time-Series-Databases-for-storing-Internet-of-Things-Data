# ------------------------------------------
# Query 5: Rolling Average with Full Output and Timing
# ------------------------------------------

import time
from cassandra.cluster import Cluster

# Start timing for performance measurement
start_time = time.time()

# Connect to Cassandra (defaults to localhost)
cluster = Cluster()
session = cluster.connect('sensor_data')  # Replace with your keyspace name if different

# Query: Retrieve the last 5 values for sensor_id=6 in the '5_rows' dataset
rows = session.execute("""
    SELECT value FROM sensor_readings
    WHERE dataset_size = '5_rows'
    AND sensor_id = 6
    ORDER BY timestamp DESC
    LIMIT 5;
""")

# Extract values into a list
values = [row.value for row in rows]

# Calculate rolling average
rolling_avg = sum(values) / len(values)

# Stop timing
end_time = time.time()
elapsed = end_time - start_time

# Output results
print(f"Values: {values}")
print(f"5-point rolling average: {rolling_avg:.2f}")
print(f"Query executed in {elapsed:.4f} seconds")
