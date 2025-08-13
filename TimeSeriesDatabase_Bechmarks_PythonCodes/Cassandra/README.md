# Apache Cassandra Data Ingestion & Query Scripts

This folder contains Python scripts for inserting and querying IoT time-series data stored in an Apache Cassandra database.  
They were developed for benchmarking and analytical tasks such as ingestion performance and time-based aggregations.


## Scripts Overview

### 1. `cassandra_data_ingestion.py`
**Purpose:**  
Bulk-inserts CSV-based sensor data into Cassandra.

**Key Features:**
- Reads CSV files (e.g., `500k_datapoints.csv`, `2k_datapoints.csv`, `5_datapoints.csv`).
- Inserts rows into the `sensor_readings` table in the `sensor_data` keyspace.
- Times the insertion process for benchmarking.

**When to Use:**  
Run this script before querying to populate the database with test data.


### 2. `cassandra_query5_rolling_avg.py`
**Purpose:**  
Calculates the **5-point rolling average** for the latest readings of a specified sensor.

**Key Features:**
- Retrieves the most recent 5 values for a given `sensor_id` and `dataset_size`.
- Computes and prints the rolling average.
- Measures query execution time.

**When to Use:**  
For short-term trend monitoring of recent sensor data.


### 3. `cassandra_query6_hourly_avg.py`
**Purpose:**  
Performs **hourly aggregation** of sensor values for a specified day.

**Key Features:**
- Queries all readings for a given day and sensor.
- Uses Pandas to group data by hour and compute the average.
- Measures query execution time.

**When to Use:**  
For analyzing hourly patterns or trends in sensor readings.


