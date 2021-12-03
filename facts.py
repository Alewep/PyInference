
from inference import variable_declare as vd
from inference import *

# --- declaration of variable ---
cotes = vd("cotes", list)
angles = vd("angles", list)
diagonals = vd("diagonals", list)
form = vd("form", str)
# --declaration of facts --------
fact(cotes, ["a", "a", "a", "a"])
fact(angles, [90.0, 90.0, 90.0])
fact(diagonals, ["a", "a"])
