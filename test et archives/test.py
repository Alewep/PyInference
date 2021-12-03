class Var(object):
    VARS = {}

    def __new__(cls, name, type=bool, *args, **kwargs):
        if name in Var.VARS:
            raise Exception("A variable was already declare with the same name ")
        Var.VARS[name] = super(Var, cls).__new__(cls, *args, **kwargs)
        return Var.VARS[name]

    def __init__(self, name, type=bool):
        self.name = name
        self.type = type
        self.value = None

    def __repr__(self):
        return self.name


x = Var("x", int)

print({x: 1})
