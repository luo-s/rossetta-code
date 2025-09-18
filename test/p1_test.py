from problem.p1_100_doors import getFinalOpenedDoors

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("getFinalOpenedDoors()", [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])])

def test_eval(test_input, expected):
    assert eval(test_input) == expected