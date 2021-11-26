import os

import sympy


def updateWihtoutOverWrite(dict1: dict, dict2: dict) -> bool:
    dict2 = dict2.copy()
    for key, value in dict1.items():
        if key in dict2 and value != dict2[key]:
            raise Exception(f"Conflit on fact '{key}'")
        dict2[key] = value

    return dict2


class Rule:
    def __init__(self, head: list, body: dict) -> None:
        self.head = head
        self.body = body

    def __str__(self) -> str:
        return "Rule : " + str(self.head) + " -> " + str(self.body)

    def have_goal(self, goal: dict):
        for key, value in goal.items():
            print(self.body)
            if key in self.body and value == self.body[key]:
                return True

        return False

    def is_trigger(self, facts):
        triggers = []
        for hd in self.head:
            if sympy.sympify(hd).subs(facts):
                pass


class Rules:
    def __init__(self) -> None:
        self.rules = []

    def addRule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def backtrack_chaining(self, goal: dict, facts: dict):
        if goal.items() <= facts.items():
            return goal

        for i, rule in enumerate(self.rules):
            if rule.have_goal(goal):
                print("regle utilisé :", i)
                if self.backtrack_chaining(rule.head, facts) is not None:
                    return goal
        return None


RULES = Rules()
FACTS = {}


def rule_declare(head: list, body: dict):
    for hd in head:
        if not (isinstance(hd, str)) and not (not sympy.sympify(hd) or sympy.sympify(hd).is_Symbol):
            raise Exception(f"Error {hd} is not a boolean or a symbol.")

    new_body = {}
    for key, value in body.items():
        if isinstance(value, dict):
            raise Exception(f"Error {value} dict into dict body rule was forbiden")
        if not (not value or value is None):
            new_body[key] = value

    RULES.addRule(Rule(head, body))


def fact_declare(name, value=True):
    if not value or isinstance(value, dict):
        raise Exception(f"Bad value type of fact '{name}' ")
    if isinstance(value, list):
        for val in value:
            if isinstance(val, dict):
                raise Exception(f"Bad value type of fact '{name}' ")
    FACTS[name] = value


def facts_declare(dict_fact: dict):
    for key, value in dict_fact.items():
        if not value or isinstance(value, dict):
            raise Exception(f"Bad value type in fact '{key}' ")
        if isinstance(value, list):
            for val in value:
                if isinstance(val, dict):
                    raise Exception(f"Bad value type in fact '{key}' ")

    FACTS.update(dict_fact)


def backtrack_chaining(goal):
    return RULES.backtrack_chaining(goal, FACTS)


os.system("python rules.py")
os.system("python facts.py")
