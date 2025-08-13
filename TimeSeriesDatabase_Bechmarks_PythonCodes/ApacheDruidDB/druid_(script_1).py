import json
import requests
import time

# Load ingestion spec JSON (contains all settings for Druid ingestion)
with open("/home/vburge/csv_ingestion_2k.json") as f:
    spec = json.load(f)

# Define the Druid Overlord API endpoint for submitting tasks
url = "http://localhost:8081/druid/indexer/v1/task"
headers = {"Content-Type": "application/json"}

print("Submitting ingestion task...")
start = time.time()  # Record start time for measuring ingestion duration

# Submit the ingestion task to Druid
res = requests.post(url, headers=headers, data=json.dumps(spec))

# Check if submission was successful
if res.status_code != 200:
    print("Failed to submit task:", res.text)
    exit(1)

# Extract the assigned task ID from the response
task_id = res.json()["task"]
print(f"Task submitted! Task ID: {task_id}")

# Poll Druid for task status until it completes
status_url = f"http://localhost:8081/druid/indexer/v1/task/{task_id}/status"
while True:
    time.sleep(2)  # Wait before checking again to reduce API calls
    status_res = requests.get(status_url)

    # If unable to fetch status, stop execution
    if status_res.status_code != 200:
        print("Failed to fetch task status:", status_res.text)
        exit(1)

    # Extract the "status" fi
