import pandas as pd
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB v2 configuration
bucket = "sensor_bucket_5datapoints"
org = "<Organisation>"
token = "your-token-here"
url = "http://localhost:8086"

# CSV path
csv_path = "/etc/telegraf/5_datapoints.csv" #Define path where your files are stored this is just example

# Load CSV
df = pd.read_csv(csv_path)

# Clean and cast data
df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True, format='mixed')
df['value'] = df['value'].astype(float)
df['category'] = df['category'].astype(str)  # tag values must be strings

# Connect to InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Measure insert time
start = time.time()
for _, row in df.iterrows():
    point = (
        Point("sensor_data")
        .tag("sensor_id", row['category'])  # 'category' used as sensor_id
        .field("value", row['value'])
        .time(row['timestamp'], WritePrecision.NS)
    )
    write_api.write(bucket=bucket, org=org, record=point)
end = time.time()

print(f" Inserted {len(df)} rows into '{bucket}' in {end - start:.3f} seconds")
