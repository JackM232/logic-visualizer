# Expression builder
import json
import os


def strOr(a, b):
    return ("" + a + " + " + b)

def strAnd(a, b):
    return ("" + a + " * " + b)

def strNot(a):
    return ( "!" + a)

j = 0

with open("example.json", encoding="utf-8") as f:
    circuit = json.load(f)

for i in circuit.get("gates"):
    if ((circuit.get("gates")[j]["type"]) == "NOT"):
        print ( "!" + circuit.get("gates")[2]["in"][0])
    j = j+1

