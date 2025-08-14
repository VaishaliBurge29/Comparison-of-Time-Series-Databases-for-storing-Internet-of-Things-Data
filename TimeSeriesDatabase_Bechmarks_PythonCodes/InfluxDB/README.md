# InfluxDB Data Ingestion Scripts & Configuration

This repository contains two methods to ingest CSV-based time-series data into **InfluxDB v2.x**:

1. **Python script ingestion** – Inserts data row-by-row using the official Python client.
2. **Telegraf ingestion** – Uses the InfluxData Telegraf agent for high-throughput ingestion from CSV files.

---

## File Overview

| File | Description |
|------|-------------|
| `influx_ingestion.py` | Python script to insert CSV data into InfluxDB v2 using synchronous API writes. |
| `influx_telegraf.conf` | Telegraf configuration file for bulk CSV ingestion into InfluxDB v2. Optimized for throughput.|

---

##  Requirements

- **Python 3.x**
- Python dependencies:
  ```bash
  pip install influxdb-client pandas
