# IoT Time-Series Database Benchmarking Framework

The Internet of Things (IoT) connects a vast network of devices that continuously generate large volumes of time-stamped data. Extracting value from such data requires storage systems optimized for high-frequency, append-only workloads. This study compares five Time-Series Databases (TSDBs) – InfluxDB, TimescaleDB, QuestDB, Apache Druid, Graphite – alongside one relational SQL system (PostgreSQL) and one NoSQL system (Cassandra). The focus is on data ingestion performance in a private cloud environment using a standardized IoT dataset.

Note: This repository only contains ingestion scripts for each database. Query benchmarking, visualization, and analysis are documented separately in the main thesis but are not part of this code repository.


##  Repository Structure

├── InfluxDB/
│   ├── ingest_influxdb.py
│   └── README.md
├── TimescaleDB/
│   ├── ingest_timescaledb.py
│   └── README.md
├── PostgreSQL/
│   ├── ingest_postgres.py
│   └── README.md
├── QuestDB/
│   ├── ingest_questdb.py
│   └── README.md
├── Cassandra/
│   ├── ingest_cassandra.py
│   └── README.md
├── Druid/
│   ├── ingest_druid.py
│   └── README.md
├── Graphite/
│   ├── ingest_graphite.py
│   └── README.md


## 🚀 How to Use

1. **Prepare datasets** – CSV files in the `data/` folder.
2. **Start your database service** – Local or VM instance.
3. **Choose the database folder** and follow its `README.md`.
4. **Run ingestion scripts** to insert data.
5. **Run query scripts** to measure query latency.
6. **Record results** for comparison.

## 📊 Benchmarked Databases

- PostgreSQL  
- TimescaleDB (PostgreSQL extension for time-series)  
- InfluxDB v2  
- QuestDB  
- Apache Druid  
- Apache Cassandra  
- Graphite (excluded from some results due to disk usage limits)


