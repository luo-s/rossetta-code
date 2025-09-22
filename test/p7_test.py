from problem.p7_ackermann_function import ack

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("ack(0,0)", 1),
     ("ack(1,1)", 3),
     ("ack(2,5)", 13),
     ("ack(3,3)", 61)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected