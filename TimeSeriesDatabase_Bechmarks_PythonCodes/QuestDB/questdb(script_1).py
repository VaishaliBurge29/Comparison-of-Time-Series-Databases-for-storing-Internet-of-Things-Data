# Script 1: Uploading Basic CSV to QuestDB (No Symbol Indexing)

# Import required libraries
import pandas as pd         # For handling CSV and data manipulation
import time                 # For measuring execution time
from questdb.ingress import Sender  # QuestDB Python client for data ingestion

# Step 1: Load the CSV file into a DataFrame
# - '5_datapoints.csv' contains sample IoT time-series data
# - Convert the 'timestamp' column to datetime format for proper ingestion
df = pd.read_csv('5_datapoints.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Step 2: Record the start time for performance measurement
start_time = time.time()

# Step 3: Establish connection and upload to QuestDB
# - Replace <vm-ip> with the actual VM or server IP address where QuestDB is running
# - The table 'sensor_data_5rows' will be created automatically if it doesn't exist
# - 'at' specifies the designated timestamp column
conf = 'http::addr=<vm-ip>:9000;'
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name='sensor_data_5rows', at='timestamp')

# Step 4: Record the end time after upload is complete
end_time = time.time()

# Step 5: Print the total time taken for the upload
print(f"Time taken to upload: {end_time - start_time:.4f} seconds")
