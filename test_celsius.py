import sys
from temp_convert import celsius_to_fahrenheit

def test_zero_celsius():
    sys.argv = ["temp_convert.py", "0"]
    assert celsius_to_fahrenheit(float(sys.argv[1])) == 32

def test_boiling_point():
    sys.argv = ["temp_convert.py", "100"]
    assert celsius_to_fahrenheit(float(sys.argv[1])) == 212

def test_negative_value():
    sys.argv = ["temp_convert.py", "-40"]
    assert celsius_to_fahrenheit(float(sys.argv[1])) == -40
