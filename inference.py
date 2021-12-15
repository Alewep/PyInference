import inspect
import os


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def str_head(head):
    return inspect.getsource(head).replace("\n", "").strip()[:-1]


def evaluate(expr, facts: dict):
    try:
        result = expr(facts)
    except KeyError as e:
        return False
    except Exception as e:
        print("\033[93m", f"Warning in expression {str_head(expr)} :{e}", "\033[0m")
        return False
    if not isinstance(result, bool):
        print("Warning ! An expression do not return boolean")
        return False
    return result


def sat(goal, facts):
    return evaluate(goal, facts)


def update_fact(facts1: dict, facts2: dict):
    for fact in facts1:
        if fact in facts2 and facts1[fact] != facts2[fact]:
            raise Exception(f"Conflicts between fact value : {fact} have {facts1[fact]} and {facts2[fact]}")
    facts1.update(facts2)
    return facts1


class Rule:
    def __init__(self, head: list, body: dict) -> None:
        self.head = head
        self.body = body

    def __str__(self) -> str:
        str_rule = ""
        for part in self.head:
            str_rule += str_head(part) + " , "
        return "% { " + str_rule[:-2] + " } ==> " + str(self.body)

    def have_as_goal(self, goal):
        return sat(goal, self.body)

    def sat(self, facts):
        for h in self.head:
            if not sat(h, facts):
                return False
        return True


class Rules:
    def __init__(self) -> None:
        self.rules = []

    def addRule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def backward_chaining(self, goals: list, facts: dict, trace=True, details=True) -> bool:
        if trace:print("---------- backward_chaining ---------")
        rules = self.rules.copy()
        facts = facts.copy()
        number_rules = 0
        while goals:
            goal = goals.pop(0)
            if sat(goal, facts):
                continue

            never = True
            for rule in rules:
                number_rules += 1
                if rule.have_as_goal(goal):
                    never = False
                    if trace: print("\033[92m", "Take ", rule, "\033[0m", sep="")
                    rules.remove(rule)
                    for h in rule.head:
                        goals.insert(0, h)
                    break
                if trace and details: print(rule)

            if never:
                if trace:print("\033[91m", "Cannot be satisfied ", str_head(goal), "\033[0m", sep="")
                if trace:print("\033[93m","Number of rules tested : ",number_rules,"\033[0m", sep="")
                return False
        return True

    def foward_chaining_deepth(self, facts: dict, trace=True, details=True):
        number_rules = 0
        if trace: print("---------- foward_chaining (in deepth) ---------")
        facts = facts.copy()
        rules = self.rules.copy()
        facts_start = facts.copy()
        can_deduct = True
        while can_deduct:
            can_deduct = False
            facts_size = len(facts)
            rules_del = rules.copy()
            for rule in rules:
                number_rules += 1
                if rule.sat(facts):
                    if trace: print("-")
                    if trace: print("\033[92m", "Take ", rule, "\033[0m", sep="")
                    if trace: print(facts)
                    if trace: print("-")
                    facts = update_fact(facts, rule.body)
                    rules_del.remove(rule)
                elif trace and details: print(rule)
            rules = rules_del

            if facts_size < len(facts):
                can_deduct = True

        if trace: print("\033[91m", "Cannot deduct anymore", "\033[0m", sep="")
        if trace: print("\033[93m", "Number of rules tested : ", number_rules, "\033[0m", sep="")
        if trace: print(facts)
        return {key: facts[key] for key in facts.keys() - facts_start.keys()}

    def forward_chaining_width(self, facts: dict, trace=True, details=True):
        if trace: print("---------- foward_chaining (in deepth) ---------")
        facts = facts.copy()
        rules = self.rules.copy()
        facts_start = facts.copy()
        number_rules = 0
        can_deduct = True
        while can_deduct:
            can_deduct = False
            facts_size = len(facts)
            facts_deduct = facts.copy()
            for rule in rules:
                number_rules += 1
                if rule.sat(facts):
                    if trace: print("-")
                    if trace: print("\033[92m", "Take ", rule, "\033[0m", sep="")
                    if trace: print(facts)
                    if trace: print("-")
                    facts_deduct = update_fact(facts_deduct, rule.body)
                    rules.remove(rule)
                elif trace and details: print(rule)

            facts = facts_deduct
            if facts_size < len(facts):
                can_deduct = True

        if trace: print("\033[91m", "Cannot deduct anymore", "\033[0m", sep="")
        if trace:print("\033[93m","Number of rules tested : ",number_rules,"\033[0m", sep="")
        if trace: print(facts)
        return {key: facts[key] for key in facts.keys() - facts_start.keys()}


RULES = Rules()
FACTS = {}


def rule_declare(head: list, body: dict):
    for hd in head:
        if not callable(hd):
            raise Exception(f"Error '{hd}' clause was not declared has a callable")
    new_body = {}
    for key, value in body.items():
        if isinstance(value, dict):
            raise Exception(f"Error '{value}' dict into dict body rule was forbiden")
        if not (not value or value is None):
            new_body[key] = value

    RULES.addRule(Rule(head, body))


def fact(name, value=True):
    name = str(name)
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


def backtrack_chaining(goal, verbose=False):
    if verbose:
        return RULES.backward_chaining(goal, FACTS, verbose=verbose)


def foward_chaining():
    return RULES.foward_chaining(FACTS)
