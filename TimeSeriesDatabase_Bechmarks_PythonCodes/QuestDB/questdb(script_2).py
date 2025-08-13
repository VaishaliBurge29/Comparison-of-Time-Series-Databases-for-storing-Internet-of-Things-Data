# Script 2: Uploading CSV with Symbol Column for Indexing
# Purpose: Demonstrates QuestDB ingestion using a SYMBOL column for better performance

import pandas as pd         # For reading CSV and data manipulation
import time                 # For measuring execution time
from questdb.ingress import Sender  # QuestDB Python client for ingestion

# Step 1: Load CSV file containing a SYMBOL column
# - '5_datapoints_sym.csv' includes a symbolic column (e.g., sensor_id)
# - SYMBOL type in QuestDB is stored efficiently and indexed automatically
df = pd.read_csv("5_datapoints_sym.csv")

# Step 2: Convert timestamp column to datetime format
# - format='mixed' allows parsing various timestamp formats
# - utc=True ensures all timestamps are stored in UTC
df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed', utc=True)

# Step 3: QuestDB connection configuration
# - 'localhost' for local instance, replace with <vm-ip> if remote
# - Default HTTP ingestion port is 9000
conf = "http::addr=localhost:9000;"

# Step 4: Record start time for performance measurement
start = time.time()

# Step 5: Ingest DataFrame into QuestDB
# - Using Arrow-based ingestion (recommended for speed)
# - WAL (Write-Ahead Logging) is enabled by default for durability
# - 'at' specifies the designated timestamp column
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name="sensor_data_sym_5rows", at="timestamp")

# Step 6: Record end time
end = time.time()

# Step 7: Print number of rows uploaded and time taken
print(f" Uploaded {len(df)} rows in {end - start:.4f} seconds")
