
# PostgreSQL & TimescaleDB Data Ingestion Script

This repository contains a **single Python ingestion script** that works for both **PostgreSQL** and **TimescaleDB**.  
The code is identical for both — only the **table setup** differs:

- **PostgreSQL**: Standard table creation
- **TimescaleDB**: Convert table into a hypertable and optionally enable compression


##  File Overview

| File | Description |
|------|-------------|
| `postgres_timescale_ingest.py` | Python script to load CSV sensor data into PostgreSQL or TimescaleDB, with ingestion time measurement. |

