# Import required libraries
import json      # For loading the ingestion specification from a JSON file
import requests  # For sending HTTP requests to Druid's Overlord API

# Load the ingestion specification from file
with open("csv_ingestion_2k.json") as f:
    spec = json.load(f)  # Reads and parses the JSON ingestion spec

# Submit the ingestion spec to Druid's Overlord endpoint
res = requests.post(
    "http://localhost:8081/druid/indexer/v1/task",  # Overlord API endpoint for submitting ingestion tasks
    headers={"Content-Type": "application/json"},   # Tell server we're sending JSON
    data=json.dumps(spec)                           # Convert Python dict to JSON string for sending
)

# Print the response which includes the task ID
# The response JSON will typically be: {"task": "<task-id>"}
print(res.json())
