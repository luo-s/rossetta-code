from problem.p10_mode import mode

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("mode([1, 3, 6, 6, 6, 6, 7, 7, 12, 12, 17])", [6]),
     ("mode([1, 2, 4, 4, 1])", [1, 4])])

def test_eval(test_input, expected):
    assert eval(test_input) == expected