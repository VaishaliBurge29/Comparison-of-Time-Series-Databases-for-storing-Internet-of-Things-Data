# QuestDB Data Ingestion Scripts

This repository contains Python scripts to upload CSV-based sensor data to **QuestDB** using its high-performance **Arrow-based ingestion API**.

Two ingestion approaches are provided:

1. **Basic ingestion without symbol indexing** – good for quick tests and small datasets.
2. **Ingestion with a symbol column** – optimized for query performance on high-cardinality fields (e.g., `sensor_id`).


## 📂 File Overview

| File | Description |
|------|-------------|
| `questdb(script_1).py` | Uploads a CSV file to QuestDB without using symbol indexing. |
| `questdb(script_2).py` | Uploads a CSV file with `sensor_id` as a symbol column for indexing. |


