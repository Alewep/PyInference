from inference import fact, variable_declare as vd, FACTS

# --- declaration of variable ---
cotes = vd("cotes")
angles = vd("angles")
diagonals = vd("diagonals")
form = vd("form")
# --declaration of facts --------
fact(cotes, ("a", "a", "a", "a"))
fact(angles, (90.0, 90.0, 90.0))
fact(diagonals, ("a", "a"))
