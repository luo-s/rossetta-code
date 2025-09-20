from problem.p4_abc_problem import canMakeWord

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("canMakeWord('bark')", True),
     ("canMakeWord('Book')", False),
     ("canMakeWord('TreAT')", True),
     ("canMakeWord('COMMON')", False),
     ("canMakeWord('squAD')", True),
     ("canMakeWord('conFUSE')", True)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected