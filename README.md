# IoT Time-Series Database Benchmarking Framework

The Internet of Things (IoT) connects a vast network of devices that continuously generate large volumes of time-stamped data. Extracting value from such data requires storage systems optimized for high-frequency, append-only workloads. This study compares five Time-Series Databases (TSDBs) – InfluxDB, TimescaleDB, QuestDB, Apache Druid, Graphite – alongside one relational SQL system (PostgreSQL) and one NoSQL system (Cassandra). The focus is on data ingestion performance in a private cloud environment using a standardized IoT dataset.


The experiments compare relational, time-series, and NoSQL databases under identical workloads.  
Benchmarks include:
- **Raw ingestion** and **optimized ingestion** codes
- **Query latency** across six representative queries (Q1–Q6)
- Multiple dataset sizes (5 rows, 2,000 rows, 500,000 rows)

Note: This repository only contains ingestion scripts for each database. Query benchmarking, visualization, and analysis are documented separately in the main thesis but are not part of this code repository.

##  Repository Structure

- The folder `TimeSeriesDatabase_Bechmarks_PythonCodes` contains a folders with a `<Database name>`, each folder contains `Python scripts, configuration files, README.md`, and usage instructions for benchmarking  as part of the time-series database performance evaluation for IoT data.
- The folder `Data` has the dataset used for this benchmarking
  
## 🚀 How to Use

1. **Prepare datasets** – CSV files in the `data/` folder.
2. **Start your database service** – Local or VM instance.
3. **Choose the database folder** and follow its `README.md`.
4. **Run ingestion scripts** to insert data.
5. **Run query scripts** to measure query latency.
6. **Record results** for comparison.

## 📊 Benchmarked Databases

- InfluxDB v2 
- PostgreSQL  
- TimescaleDB (PostgreSQL extension for time-series)  
 - QuestDB  
- Apache Druid  
- Graphite (excluded from some results due to disk usage limits)
- Apache Cassandra  

For information on my thesis paper : link 
