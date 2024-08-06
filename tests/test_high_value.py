from lib.high_value import *

def test_get_highest_equal():
    val = HighValue(0,0)
    result = val.get_highest()
    assert result == "Values are equal"

def test_get_highest_first_higher():
    val = HighValue(10,3)
    result = val.get_highest()
    assert result == "First value is higher"

def test_get_highest_add_seven_first():
    val = HighValue(0,0)
    val.add(7,"first")
    assert val.value_first == 7

def test_get_highest_second_higher():
    val = HighValue(2,6)
    result = val.get_highest()
    assert result == "Second value is higher"

def test_get_highest_add_and_check():
    val = HighValue(3,4)
    val.add(3, "first")
    assert val.get_highest() == "First value is higher"

def test_get_highest_second_attribute():
    val = HighValue(5,10)
    assert val.value_second == 10

def test_get_highest_first_attribute():
    val = HighValue(14,5)
    assert val.value_first == 14

def test_get_highest_add_negative():
    val = HighValue(6,11)
    val.add(-12, "second")
    assert val.get_highest() == "First value is higher"