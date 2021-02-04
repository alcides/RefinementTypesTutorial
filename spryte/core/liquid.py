from typing import List


class LiquidTerm(object):
    pass


class LiquidLiteralInt(LiquidTerm):
    value: int

    def __init__(self, v: int):
        self.value = v


class LiquidLiteralBool(LiquidTerm):
    value: bool

    def __init__(self, v: bool):
        self.value = v


class LiquidVar(LiquidTerm):
    name: str

    def __init__(self, name: str):
        self.name = name


class LiquidApp(LiquidTerm):
    name: str
    arguments: List[LiquidTerm]

    def __init__(self, name: str, args: List[LiquidTerm]):
        self.name = name
        self.arguments = args
