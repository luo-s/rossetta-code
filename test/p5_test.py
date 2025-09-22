from problem.p5_number_classifications import getDPA

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("getDPA(5000)", [3758, 3, 1239]),
     ("getDPA(10000)", [7508, 4, 2488]),
     ("getDPA(20000)", [15043, 4, 4953])])

def test_eval(test_input, expected):
    assert eval(test_input) == expected