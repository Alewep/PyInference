from inference import *

# facts declaration
fact("sides", ["a", "a", "a", "a"])
fact("angles", [90.0, 90.0, 90.0, 90.0])
fact("parallels_sides_pair", 4)
fact("symmetric_axe")
fact("convex")

# declaration of rules
# 4 cotées -> quadrilatère
rule_declare([
    lambda var: len(var["sides"]) == 4,
    lambda var: len(var["angles"]) == 4,
], {"quadrilateral": True})

# 1 paire de cotes parallel -> trapèze
rule_declare([
    lambda var: var["parallels_sides_pair"] >= 1,
], {"trapezoid": True})

# c'est un trapeze, 2 angles droit -> trapeze rectangle
rule_declare([
    lambda var: var["trapezoid"],
    lambda var: var["angles"].count(90.0) >= 2,
], {"rectangle_trapezoid": True})

# c'est un trapeze, 2 paire de cotees parallel -> trapeze isocèle
rule_declare([
    lambda var: var["trapezoid"],
    lambda var: len(set(var["sides"])) <= 3,
], {"isosceles_trapezoid": True})

# trapèze isocèle, 2 coté identique -> parallelogramme
rule_declare([
    lambda var: var["isosceles_trapezoid"],
    lambda var: var["parallels_sides_pair"] >= 2,
], {"parallelogram": True})

# parallelogram avec 4 angles droit
rule_declare([
    lambda var: var["parallelogram"],
    lambda var: var["angles"].count(90.0) >= 4,
], {"rectangle": True})

rule_declare([
    lambda var: var["rectangle_trapezoid"],
    lambda var: var["angles"].count(90.0) >= 4,
], {"rectangle": True})

rule_declare([
    lambda var: var["rectangle"],
    lambda var: len(set(var["sides"])) == 1,
], {"square": True})


