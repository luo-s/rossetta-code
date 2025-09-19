from problem.p3_integer_partition import partition

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("partition(5)", 7),
     ("partition(12)", 77),
     ("partition(18)", 385),
     ("partition(23)", 1255),
     ("partition(42)", 53174),
     ("partition(123)", 2552338241)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected