# Expression builder
import json
import os

print(os.getcwd())

with open("example.json") as f:
    circuit = json.load(f)

print(circuit)