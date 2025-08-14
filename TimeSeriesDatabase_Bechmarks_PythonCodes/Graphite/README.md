# Graphite / Whisper: Backdated + Real‑Time Injection

This folder contains three small utilities for working with **Graphite + Whisper**:

- Create **backdated** `.wsp` files (so older data won’t be dropped)
- Inject **historical** datapoints from a CSV
- Send **real‑time** datapoints via Carbon’s plaintext protocol
---
 **When to use what?**  
 - Use **Script 1**: *once* per metric to create a backdated Whisper file.  
 - Use **Script 2**: to inject **historical CSV** data into those files.  
 - Use **Script 3**: to send **live** datapoints as they arrive via command line.
---
## Prerequisites

- Graphite/Carbon + Whisper installed and running.
- Your `storage-schemas.conf` and `storage-aggregation.conf` set appropriately.
- Python 3.8+ with `whisper` and `pytz` (for Script 2):
  ```bash
  pip install whisper-graphite pytz
