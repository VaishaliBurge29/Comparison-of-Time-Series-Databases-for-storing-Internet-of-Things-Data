# IoT Time-Series Database Benchmarking Framework

This repository contains the full code, configurations, and scripts used in the benchmarking study from the paper:

> **"Performance Evaluation of SQL and NoSQL Time-Series Databases for IoT Data Ingestion and Querying"**  
> Evaluates ingestion speed, query latency, and optimization strategies across multiple database systems using synthetic IoT datasets.

The experiments compare relational, time-series, and NoSQL databases under identical workloads.  
Benchmarks include:
- **Raw ingestion** and **optimized ingestion**
- **Query latency** across six representative queries (Q1–Q6)
- Multiple dataset sizes (5 rows, 2,000 rows, 500,000 rows)

##  Repository Structure


---

## 🗂 Folder & File Details

### **1. Cassandra**
- **`ingestion/`** – Python scripts to insert CSV data into Cassandra for different dataset sizes.
- **`queries/`** – Benchmark queries implemented in Python using the Cassandra driver.
- **`cassandra_schema.cql`** – Schema definition for `sensor_readings` table.

### **2. Druid**
- **`ingestion_specs/`** – JSON specs for batch ingestion tasks via Druid Overlord.
- **`submit_ingestion.py`** – Sends ingestion tasks to Druid.
- Designed for **2k** and **500k** dataset ingestion.

### **3. Graphite**
- **Script 1** – Create `.wsp` Whisper files for backdated data.
- **Script 2** – Inject historical CSV data into existing Whisper files.
- **Script 3** – Real-time ingestion using Carbon plaintext protocol + `netcat`.

### **4. InfluxDB**
- **`influxdb_ingest.py`** – Python ingestion using official InfluxDB v2 client.
- **`telegraf.conf`** – Telegraf-based ingestion from CSV for large datasets.

### **5. PostgreSQL / TimescaleDB**
- **`ingest_csv.py`** – Common ingestion script for both databases (change DB name and table).  
  TimescaleDB requires hypertable creation & optional compression (see README.md inside).

### **6. QuestDB**
- **`5rows_file.py`** – Upload CSV without Symbol indexing.
- **`5rows_file_with_symbol.py`** – Upload CSV with Symbol column for indexing.

### **7. Data**
- Contains the benchmark datasets:  
  - `5_datapoints.csv` (small-scale)  
  - `2k_datapoints.csv` (medium-scale)  
  - `500k_datapoints.csv` (large-scale)

---

## 🚀 How to Use

1. **Prepare datasets** – CSV files in the `data/` folder.
2. **Start your database service** – Local or VM instance.
3. **Choose the database folder** and follow its `README.md`.
4. **Run ingestion scripts** to insert data.
5. **Run query scripts** to measure query latency.
6. **Record results** for comparison.

---

## 📊 Benchmarked Databases

- PostgreSQL  
- TimescaleDB (PostgreSQL extension for time-series)  
- InfluxDB v2  
- QuestDB  
- Apache Druid  
- Apache Cassandra  
- Graphite (excluded from some results due to disk usage limits)


