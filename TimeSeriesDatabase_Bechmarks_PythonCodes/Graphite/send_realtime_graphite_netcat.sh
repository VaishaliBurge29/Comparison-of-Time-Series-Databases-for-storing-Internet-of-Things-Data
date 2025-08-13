# Send one data point per metric per minute to Graphite via Carbon's plaintext protocol.
# Format: <metric_path> <value> <timestamp_unix>

# Metric: 5datapoints.sensor.6
# Value: 15.6
# Timestamp: 1740001260 (corresponds to 21:41 UTC)
echo "5datapoints.sensor.6 15.6 1740001260" | nc -q 0 localhost 2003

# Metric: 5datapoints.sensor.7
# Value: 9.8
# Timestamp: 1740001320 (21:42 UTC)
echo "5datapoints.sensor.7 9.8 1740001320" | nc -q 0 localhost 2003

# Metric: 5datapoints.sensor.7 (same sensor as above, later timestamp)
# Value: 10.2
# Timestamp: 1740001380 (21:43 UTC)
echo "5datapoints.sensor.7 10.2 1740001380" | nc -q 0 localhost 2003

# Metric: 5datapoints.sensor.8
# Value: 7.4
# Timestamp: 1740001440 (21:44 UTC)
echo "5datapoints.sensor.8 7.4 1740001440" | nc -q 0 localhost 2003
