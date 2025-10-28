#  Data

This folder contains the dataset files used for the benchmarking experiments in the thesis *"Comparison of Time-Series Databases for Storing Internet-of-Things Data"*.

## Raw Data
The full 5 GB dataset used in this thesis is stored in the UniConnect folder
(access available upon request or via Prof. Blazevic).

## 📄 Files

| File Name              | Description |
|------------------------|-------------|
| **5rows_datapoints.csv**   | Small dataset (5 rows) for quick ingestion and query testing. |
| **2k_datapoints.csv**      | Medium dataset (2,000 rows) representing typical IoT workloads. |
| **500k_datapoints.csv**    | Large dataset (500,000 rows) for high-scale ingestion and performance testing. |


##  Notes

- All datasets contain **synthetic IoT sensor readings** with columns:
  1. `sensor_id` – Identifier for the sensor
  2. `timestamp` – Time when the measurement was recorded (UTC)
  3. `value` – Recorded sensor value (e.g., temperature)
- The datasets are used consistently across all database benchmarks to ensure comparability.
- Larger datasets (2k and 500k) are designed to test database scalability and throughput under increasing load.


