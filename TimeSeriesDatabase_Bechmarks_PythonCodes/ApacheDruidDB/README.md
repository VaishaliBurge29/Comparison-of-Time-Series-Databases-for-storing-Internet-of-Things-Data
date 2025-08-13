# Apache Druid Ingestion and Querying Scripts

This repository contains Python scripts and a JSON ingestion specification for ingesting CSV-based time-series data into [Apache Druid](https://druid.apache.org/) and querying it via the [PyDruid](https://pypi.org/project/pydruid/) SQL client.

---

## 📄 File Overview

### **1. `druid_(script_1).py`**
**Purpose:**  
Submits a batch ingestion task to Druid and monitors its progress until completion.  

**How it works:**  
- Loads the ingestion specification from `csv_ingestion_2k.json`.
- Sends the specification to the Druid Overlord endpoint (`:8081`).
- Retrieves the generated task ID.
- Polls the task status every 2 seconds until it reaches `SUCCESS` or `FAILED`.
- Prints total ingestion time and final status.

**When to use:**  
- When you want to submit an ingestion job **and** track its progress in real-time.

### **2. `druid_(script_2).json`**
**Purpose:**  
Ingestion Specification (JSON).Defines the ingestion configuration for loading a CSV file into Druid.  

**Key configuration elements:**  
- `dataSource`: The name of the Druid table to create (e.g., `sensor_data_2k`).  
- `timestampSpec`: Column and format for parsing timestamps from the CSV.  
- `dimensionsSpec`: Categorical fields to store (e.g., `sensor_id`).  
- `metricsSpec`: Numeric fields to aggregate (`value` as `doubleSum`).  
- `granularitySpec`: Segment and query granularity settings (`day` segments, no rollup).  
- `inputSource`: Path to the CSV file on the local filesystem.  
- `inputFormat`: CSV parsing configuration.

**When to use:**  
- As the ingestion spec file referenced by ingestion scripts.

**Important:**  
- Change `dataSource` and `filter` values to match your dataset.
- Ensure `timestampSpec.format` matches your CSV file’s timestamp format.
- 

### **3. `druid_(script_3).py`**
**Purpose:**  
Python Code to Submit Ingestion Task

**How it works:**  
- Loads `csv_ingestion_2k.json`.
- Sends it to the Overlord API (`:8081`).
- Prints the returned JSON (usually contains the `task` ID).

**When to use:**  
- When you only need to trigger ingestion and don’t require progress tracking.

### **4. `query1_datapoints.py`**
**Purpose:**  
Queries ingested Druid data using the PyDruid SQL client.  

**How it works:**  
- Connects to the Druid Broker service (`:8082`).
- Executes a SQL query with a specified datasource and time range, change the query accordingly.
- Fetches and prints query results.
- Displays the total query execution time.

**When to use:**  
- To retrieve and inspect ingested data from Druid.
- To benchmark query latency for a given time range.

**Important:**  
- Change the datasource name in the `FROM` clause to match your ingested table.
- Adjust timestamps in the `WHERE` clause to suit your dataset.


