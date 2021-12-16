from inference import *

# ---- declaration of rules -------

error_angle = 15
error_sides = 20

# 1
rule_declare([
    lambda var: len(var["points"]) == 0,
], {"nothing": True})

# 2
rule_declare([
    lambda var: len(var["points"]) == 1,
], {"point": True})

# 3
rule_declare([
    lambda var: len(var["points"]) == 2,
], {"trait": True})

# quadrilateral

# 4
rule_declare([
    lambda var: len(var["sides"]) == 4,
    lambda var: len(var["angles"]) == 4,
], {"quadrilateral": True})

# 5
rule_declare([
    lambda var: var["quadrilateral"],
    lambda var: (var["angles"][2] - error_angle) <= var["angles"][0] <= (var["angles"][2] + error_angle),
    lambda var: (var["angles"][3] - error_angle) <= var["angles"][1] <= (var["angles"][3] + error_angle),
], {"parallelogram": True})

# 6
rule_declare([
    lambda var: var["parallelogram"],
    lambda var: [90.0 if ((90.0 - error_angle) <= angle <= (90 + error_angle)) else angle for angle in
                 var["angles"]].count(90.0) >= 1
], {"rectangle": True})

# 7
rule_declare([
    lambda var: var["rectangle"],
    lambda var: [True if abs(i - var["sides"][0]) <= error_sides else False for i in var["sides"]].count(True) == 4
], {"square": True})

# triangle

# 8
rule_declare([
    lambda var: len(var["sides"]) == 3,
    lambda var: len(var["angles"]) == 3
], {"triangle": True})

# 9
rule_declare([
    lambda var: var["triangle"],
    lambda var: [90.0 if ((90.0 - error_angle) <= angle <= (90 + error_angle)) else angle for angle in
                 var["angles"]].count(90.0) == 1
], {"rectangle triangle": True})

# 10
rule_declare([
    lambda var: var["triangle"],
    lambda var: [True if abs(i - var["sides"][0]) <= error_sides else False for i in var["sides"]].count(True) >= 2
], {"isosceles triangle": True})

# 11
rule_declare([
    lambda var: var["triangle"],
    lambda var: [True if abs(i - var["sides"][0]) <= error_sides else False for i in var["sides"]].count(True) == 3
], {"equilateral triangle": True})

# ------ meta rules declaration ----
# hide-1-to-3 allow hiding rule 1 to rule 3 when meta rules is executed (hide rule 1,2,3)
# up-1-to-3 allow prioritizing rule 1 to 3  when meta rules is executed (prioritize rule 1,2,3)
meta_rules_declare([
    lambda var: len(var["sides"]) == 4,
], {"hide-1-to-3": True, "up-4-to-4": True})

meta_rules_declare([
    lambda var: len(var["sides"]) == 3,
], {"hide-1-to-7": True, "up-8-to-8": True})

meta_rules_declare([
    lambda var: len(var["sides"]) < 3,
], {"hide-4-to-8": True})
