from inference import rule_declare, RULES

rule_declare(["je_tient_une_fourchette", "nombre_de_couvert == 2"], {'je_tient_un_couteau': 1})
rule_declare(["not(nombre_de_couvert == 0)"], {"je_mange": True})

print(RULES.rules[1])
