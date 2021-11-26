import json
import re

import sympy


class Rule:
    def __init__(self, head: list, body: dict):
        self.head = head
        self.body = body

    def __str__(self):
        return "Rule : " + str(self.head) + " -> " + str(self.body)


def knowledge(filename):
    with open(filename, "r") as file:
        return json.load(file)


def creates_rules(filename):
    rules = []
    with open(filename, "r") as file:
        res = file.read().replace(" ", "")
        res = res.split("\n")
        res = list(set(res))
        for rule in res:
            temp = rule.split("->")
            # for body of the rule
            body = {}
            for inst in temp[1].split(","):
                if not "=" in inst:
                    body[inst] = True
                else:
                    temp = inst.split("=")
                    try:
                        if not sympy.sympify(temp[0]).is_Symbol:
                            raise Exception(f"Error {temp[1]} was not a symbol")
                    except Exception as e:
                        raise e
                    body[temp[0]] = temp[1]

            # for head of the rule
            head = []
            for hd in temp[0].split(","):
                try:
                    if not (isinstance(sympy.sympify(hd), bool) or sympy.sympify(hd).is_Symbol):
                        raise Exception(f"Error '{hd}' was not a boolean or a symbol")
                except Exception as e:
                    raise e

            rules.append(Rule(head, body))

    return rules


print(knowledge("Knowledge.json"))
print(creates_rules("Rules.txt")[0])
