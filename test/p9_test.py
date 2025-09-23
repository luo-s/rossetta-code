from problem.p9_amicable_pairs import amicablePairsUpTo

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("amicablePairsUpTo(300)", [[220, 284]]),
     ("amicablePairsUpTo(3000)", [[220,284],[1184,1210],[2620,2924]]),
     ("amicablePairsUpTo(20000)", [[220,284],[1184,1210],[2620,2924],[5020,5564],[6232,6368],[10744,10856],[12285,14595],[17296,18416]])])

def test_eval(test_input, expected):
    assert eval(test_input) == expected