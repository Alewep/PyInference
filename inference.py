

def sat(goal, facts):
    for value in goal:
        evaluation = sympy.sympify(value).subs(facts)
        if evaluation.is_Boolean:
            if not evaluation:
                return False
        else:
            return False
    return True

lamda **args :print(args[salut])

class Rule:
    def __init__(self, head: list, body: dict) -> None:
        self.head = head
        self.body = body

    def __str__(self) -> str:
        return "Rule : " + str(self.head) + " -> " + str(self.body)

    def have_as_goal(self, goal: list):
        print("sat :", goal, self.body)
        return sat(goal, self.body)


class Rules:
    def __init__(self) -> None:
        self.rules = []

    def addRule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def backtrack_chaining(self, goal: list, facts: dict) -> bool:
        if sat(goal, facts):
            return True
        for rule in self.rules:
            # print(rule, rule.have_as_goal(goal))
            if rule.have_as_goal(goal):
                print("enter")
                if self.backtrack_chaining(rule.head, facts):
                    return True
        return False


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


def fact(name, value=True):
    if not value or isinstance(value, dict):
        raise Exception(f"Bad value type of fact '{name}' ")
    if isinstance(value, list):
        for val in value:
            if isinstance(val, dict):
                raise Exception(f"Bad value type of fact '{name}' ")
    FACTS[name] = value


def facts(dict_fact: dict):
    for key, value in dict_fact.items():
        if not value or isinstance(value, dict):
            raise Exception(f"Bad value type in fact '{key}' ")
        if isinstance(value, list):
            for val in value:
                if isinstance(val, dict):
                    raise Exception(f"Bad value type in fact '{key}' ")

    FACTS.update(dict_fact)


def variable_declare(name, type):
    return sympy.Symbol(name, )


def backtrack_chaining(goal):
    return RULES.backtrack_chaining(goal, FACTS)


import facts
import rules
