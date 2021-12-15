from inference import *
import rules
# facts declaration

# declaration of rules

error_angle = 15
error_sides = 20
rule_declare([
    lambda var: len(var["points"]) == 0,
], {"nothing": True})

rule_declare([
    lambda var: len(var["points"]) == 1,
], {"point": True})

rule_declare([
    lambda var: len(var["points"]) == 2,
], {"trait": True})

# quadrilateral
rule_declare([
    lambda var: len(var["sides"]) == 4,
    lambda var: len(var["angles"]) == 4,
], {"quadrilateral": True})

rule_declare([
    lambda var: var["quadrilateral"],
    lambda var: (var["angles"][2] - error_angle) <= var["angles"][0] <= (var["angles"][2] + error_angle),
    lambda var: (var["angles"][3] - error_angle) <= var["angles"][1] <= (var["angles"][3] + error_angle),
], {"parallelogram": True})

rule_declare([
    lambda var: var["parallelogram"],
    lambda var: [90.0 if ((90.0 - error_angle) <= angle <= (90 + error_angle)) else angle for angle in var["angles"]].count(90.0) >= 1
], {"rectangle": True})

rule_declare([
    lambda var: var["rectangle"],
    lambda var: [True if abs(i-var["sides"][0]) <= error_sides else False for i in var["sides"]].count(True) == 4
], {"square": True})


# triangle
rule_declare([
    lambda var: len(var["sides"]) == 3,
    lambda var: len(var["angles"]) == 3
], {"triangle": True})

rule_declare([
    lambda var:var["triangle"],
    lambda var:[90.0 if ((90.0 - error_angle) <= angle <= (90 + error_angle)) else angle for angle in var["angles"]].count(90.0) == 1
], {"rectangle triangle": True})

rule_declare([
    lambda var:var["triangle"],
    lambda var:[True if abs(i-var["sides"][0]) <= error_sides else False for i in var["sides"]].count(True) >= 2
], {"isosceles triangle": True})

rule_declare([
    lambda var:var["triangle"],
    lambda var:[True if abs(i-var["sides"][0]) <= error_sides else False for i in var["sides"]].count(True) == 3
], {"equilateral triangle": True})