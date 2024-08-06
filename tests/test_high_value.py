from lib.high_value import *

def test_get_highest_equal():
    val = HighValue(0,0)
    result = val.get_highest()
    assert result == "Values are equal"

def test_get_highest_first_higher():
    val = HighValue(10,3)
    result = val.get_highest()
    assert result == "First value is higher"