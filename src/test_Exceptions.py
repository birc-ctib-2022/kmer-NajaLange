

from Exceptions import (
    count
)

def count():
    assert count('agtagtcg') == {'A': 2, 'C': 1, 'G': 3, 'T': 2}
