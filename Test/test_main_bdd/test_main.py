import pytest
from pytest_bdd import scenario, given, when, then
from Src.tui import main


@scenario("main.feature", "User inputs the expression 1+1")
def test_main_add_1_1(): pass


@given("A calculator", target_fixture="calc")
def calculator():
    return main


@when("A user inputs the expression 1+1", target_fixture="added_1_1")
def run_calc_add_1_1(calc):
    return calc("1+1")


@then("The response should be 2")
def ensure_add_1_1_is_two(added_1_1):
    assert added_1_1 == 2


@scenario("main.feature", "User inputs the expression 12+20")
def test_main_add_12_20(): pass


@when("A user inputs the expression 12+20", target_fixture="added_12_20")
def run_calc_add_12_20(calc):
    return calc("12+20")


@then("The response should be 32")
def ensure_add_12_20_is_32(added_12_20):
    assert added_12_20 == 32


@scenario("main.feature", "User inputs expression 1.5+2.5")
def test_add_f1_5_f2_5(): pass


@when("A user inputs the expression 1.5+2.5", target_fixture="added_f1_5_f2_5")
def run_calc_f1_5_f2_5(calc):
    return calc("1.5+2.5")


@then("The response should be 4.0")
def ensure_add_f1_5_f2_5(added_f1_5_f2_5):
    assert added_f1_5_f2_5 == 4.0


@scenario("main.feature", "User inputs expression 1/1")
def test_div_1_1(): pass


@when("A user inputs the expression 1/1", target_fixture="divided_1_1")
def run_calc_div_1_1(calc):
    return calc("1/1")


@then("The response should be 1")
def ensure_div_1_1(divided_1_1):
    assert divided_1_1 == 1


@scenario("main.feature", "User inputs expression 1/0")
def test_div_1_1(): pass


@when("A user inputs the expression 1/0")
def run_calc_div_1_1(): pass


@then("A zero division error should appear")
def ensure_div_1_1(calc):
    with pytest.raises(ZeroDivisionError):
        calc("1/0")
