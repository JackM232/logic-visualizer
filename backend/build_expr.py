# Expression builder
import json
import os

def strNot(a):
    if len(a) > 1 and not a.startswith("("): 
        return "!(" + a + ")"
    return "!" + a

def strAnd(a, b):
    if len(a) > 1 and not (a.startswith("(") or a.startswith("!")):
        a = "(" + a + ")"
    if len(b) > 1 and not (b.startswith("(") or b.startswith("!")):
        b = "(" + b + ")"
    return a + " * " + b

def strOr(a, b):
    if len(a) > 1 and not (a.startswith("(") or a.startswith("!")):
        a = "(" + a + ")"
    if len(b) > 1 and not (b.startswith("(") or b.startswith("!")):
        b = "(" + b + ")"
    return a + " + " + b



gateFunctions = {
    "NOT": strNot,
    "AND": strAnd,
    "OR": strOr
}

# Finds the final gate in the logic expression 
def findRoot(gates):

    # Creates list of all gate inputs
    inputs = []
    for i in gates: 
        inputs = inputs + i["in"]

    roots = []
    i = 0
    for gate in gates:
        if gate["id"] not in inputs:
            roots.append(i)
        i+=1
    if len(roots) != 1:
        return "invalid expression"
    return roots[0]


script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "example.json"), encoding="utf-8") as f:
    circuit = json.load(f)

# Build expression recursively
def buildExpr(circuit, index):
    gate = circuit["gates"][index]
    func = gateFunctions[gate["type"]]
    
    expr_inputs = []
    for inp in gate["in"]:
        found = False
        for i in range(len(circuit["gates"])):
            if circuit["gates"][i]["id"] == inp:
                expr_inputs.append(buildExpr(circuit, i))
                found = True
                break
        if not found:
            expr_inputs.append(inp)  # base input like "A", "B", etc.
    
    if gate["type"] == "NOT":
        return func(expr_inputs[0])
    else:
        return func(expr_inputs[0], expr_inputs[1])

root_index = findRoot(circuit["gates"])
if root_index != "invalid expression":
    expr = buildExpr(circuit, root_index)
    print("Final Expression:", expr)
else:
    print("invalid expression")
