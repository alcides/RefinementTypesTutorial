from spryte.core.liquid import LiquidApp, LiquidVar, LiquidLiteralInt, LiquidLiteralBool
from spryte.vc.sat import is_sat


def test_predicate_is_satisfiable():
    p = LiquidApp(">", [LiquidVar("x"), LiquidLiteralInt(0)])
    assert is_sat({"x": "int"}, p)


def test_predicate_is_satisfiable_bool():
    p = LiquidApp("==", [LiquidVar("x"), LiquidLiteralBool(False)])
    assert is_sat({"x": "bool"}, p)
