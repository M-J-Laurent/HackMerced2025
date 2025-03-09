import sys
import json

# Read input from express server data
data = sys.stdin.read()

# Assuming it's JSON, you can parse and process it
# data = json.loads(input_data)

print(f"Received data: {data}")
print("Python script finished")