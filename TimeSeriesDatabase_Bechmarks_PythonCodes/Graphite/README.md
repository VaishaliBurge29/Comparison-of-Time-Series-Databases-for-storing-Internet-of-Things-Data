# Graphite / Whisper: Backdated + Real-Time Injection

This folder contains three small Python/CLI utilities for working with **Graphite** and its **Whisper** storage engine. These scripts cover both **historical backfilling** and **real-time ingestion** of time-series data.

---

##  File Overview

| File                        | Description |
|-----------------------------|-------------|
| `create_wsp_backdated.py` | **Script 1:** Creates backdated `.wsp` files so that historical data is not dropped by Whisper’s retention ring buffer. |
| `send_to_graphite_5points.py` | **Script 2:** Reads timestamped sensor values from a CSV file and injects them into the corresponding Whisper files created by Script 1. |
| `send_realtime_graphite_netcat`   | **Script 3:** Sends real-time datapoints directly to Graphite using the Carbon plaintext protocol (`netcat`). |

---

##  Requirements

- Python 3.x (for Scripts 1 & 2)
- `whisper` Python package (ships with Graphite)
- Access to `.wsp` file storage location
- For Script 3:
  - `netcat` (`nc`) installed on your system
- Graphite/Carbon + Whisper installed and running.
- Your `storage-schemas.conf` and `storage-aggregation.conf` set appropriately.
- Python 3.8+ with `whisper` and `pytz` (for Script 2):
  ```bash
  pip install whisper-graphite pytz

---

## Usage

### Creating Backdated Whisper Files (Script 1)
Use this **once per metric** to create `.wsp` files with a **fake "now" timestamp** so older historical data won’t be discarded.
```bash
python graphite_backdate_whisper.py
