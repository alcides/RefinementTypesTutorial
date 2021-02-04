from typing import Dict

from spryte.core.liquid import (
    LiquidTerm,
    LiquidVar,
    LiquidLiteralBool,
    LiquidLiteralInt,
    LiquidApp,
)
from z3 import Solver, Int, Bool, sat

builtin_functions = {">": lambda x, y: x > y, "==": lambda x, y: x == y}


def translate(ctx: Dict[str, str], lt: LiquidTerm):
    if isinstance(lt, LiquidVar):
        if ctx[lt.name] == "bool":
            return Bool(lt.name)  # There might be a bug here!
        elif ctx[lt.name] == "int":
            return Int(lt.name)  # There might be a bug here!
        else:
            assert False

    elif isinstance(lt, LiquidLiteralInt) or isinstance(lt, LiquidLiteralBool):
        return lt.value
    elif isinstance(lt, LiquidApp):
        f = builtin_functions[lt.name]
        nargs = [translate(ctx, a) for a in lt.arguments]
        return f(*nargs)
    assert False


def is_sat(ctx: Dict[str, str], lt: LiquidTerm) -> bool:
    z3_version_of_lt = translate(ctx, lt)
    s = Solver()
    s.add(z3_version_of_lt)
    return s.check() == sat