import csv                 # For reading CSV data
import whisper              # Graphite's Whisper library to update .wsp files
from datetime import datetime  # For timestamp parsing
import pytz                 # For timezone handling
import os                   # For file path handling

# -------------------------
# CONFIGURATION
# -------------------------

# Path to the CSV file containing sensor data
CSV_FILE = 'data/5_datapoints.csv'

# Base directory containing Whisper files (must match Script 1 output)
WSP_BASE_DIR = 'graphite_data/whisper/data/sensor_5points'

# Timezone of the timestamps in the CSV file
TIMEZONE = pytz.timezone("Europe/Berlin")

# -------------------------
# HELPER FUNCTION
# -------------------------

def to_unix(ts_str):
    """
    Convert timestamp string from CSV into a UNIX epoch integer.
    CSV format: YYYY-MM-DD HH:MM:SS.sss±HHMM
    Example: '2024-02-07 11:00:00.000+0100'
    """
    dt = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S.%f%z")
    return int(dt.timestamp())

# -------------------------
# READ AND GROUP CSV DATA
# -------------------------

sensor_data = {}  # Dictionary to hold sensor_id → list of (timestamp, value)

with open(CSV_FILE, 'r') as f:
    reader = csv.DictReader(f)  # Read CSV into dictionaries per row
    for row in reader:
        sensor_id = row["sensor_id"]  # Unique ID of the sensor
        ts = to_unix(row["timestamp"])  # Convert to UNIX timestamp
        value = float(row["value"])     # Sensor reading value

        # Build the Whisper metric key (sensor.<sensor_id>)
        key = f"sensor.{sensor_id}"

        # Append datapoint to the list for this sensor
        sensor_data.setdefault(key, []).append((ts, value))

# -------------------------
# INJECT DATA INTO WHISPER FILES
# -------------------------

for sensor_key, datapoints in sensor_data.items():
    # Full path to the .wsp file for this sensor
    wsp_path = os.path.join(WSP_BASE_DIR, f"{sensor_key}.wsp")

    # Check if file exists before writing
    if not os.path.exists(wsp_path):
        print(f"❌ File not found: {wsp_path}")
        continue

    # Inject data into the Whisper file
    print(f"📌 Injecting {len(datapoints)} points into {wsp_path}")
    whisper.update_many(wsp_path, datapoints)  # Bulk update for performance
