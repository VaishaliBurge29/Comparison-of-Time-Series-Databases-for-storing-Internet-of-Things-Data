#Loads CSV to PostgreSQL
import pandas as pd
from sqlalchemy import create_engine
import time

# DB config
db_user = "<username>"
db_password = "<password>"
db_host = "localhost"
db_port = 5432
db_name = "<database name>" #just need to change TSDB table name, rest all remains the  same, just creation of hypertable and compression is different, which is explained in Overview
table_name = "sensor_data" 

# CSV path
csv_path = "/home/vburge/data/1k_datapoints.csv"

# Load CSV
df = pd.read_csv(csv_path)

# Clean and cast data
df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True, format='mixed')
df['value'] = df['value'].astype(float)
df['sensor_id'] = df['sensor_id'].astype(int)

# Create DB engine
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Measure insert time
start = time.time()
df.to_sql(table_name, engine, if_exists='append', index=False)
end = time.time()

print(f"Inserted {len(df)} rows into '{table_name}' in {end - start:.3f} seconds")
