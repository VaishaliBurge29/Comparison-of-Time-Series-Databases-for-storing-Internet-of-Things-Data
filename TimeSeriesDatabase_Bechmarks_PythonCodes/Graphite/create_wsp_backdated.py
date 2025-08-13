import whisper   # Graphite's Whisper library for creating/managing .wsp files
import os        # For file and directory handling
import time      # For manipulating the system clock temporarily

# -------------------------
# CONFIGURATION
# -------------------------

# Backdated start time (UNIX timestamp)
# Example: Feb 7, 2024 11:00:00 UTC = 1707300000
# This will be used as the "creation time" of the Whisper file
backdate_start_unix = 1707300000

# Data retention period (in seconds)
# Here: 365 days * 24 hours * 60 minutes * 60 seconds
retention_seconds = 365 * 24 * 60 * 60

# Archive list defines:
# (secondsPerPoint, retentionPeriodInSeconds)
# Here: store data with 1-second resolution for the full retention period
archive = [(1, retention_seconds)]

# Path to the Whisper file to be created
# Make sure this matches your Graphite data directory structure
path = "graphite_data/whisper/data/sensor_5points/sensor.6.wsp"

# Create parent directories if they do not exist
os.makedirs(os.path.dirname(path), exist_ok=True)

# -------------------------
# WHISPER FILE CREATION
# -------------------------

# Save the original time function
original_time = time.time

# Override time.time() to return our backdated timestamp
# This tricks Whisper into thinking "now" is in the past
time.time = lambda: backdate_start_unix

# Create the Whisper file with the specified retention and aggregation method
whisper.create(
    path=path,
    archiveList=archive,
    xFilesFactor=0,              # Accept datapoints even if previous data is missing
    aggregationMethod='max'      # Aggregate by taking the maximum value
)

# Restore the original time function
time.time = original_time

# -------------------------
# CONFIRMATION
# -------------------------

print(f"✅ Created .wsp file at: {path}")
print(f"   Backdated to UNIX time: {backdate_start_unix}")
