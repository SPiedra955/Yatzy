from src.yatzy_refactoring import Yatzy
import pytest

@pytest.mark.chance
def test_sum_all_rolls():
    assert 16 == Yatzy.chance(1,2,3,4,6)
    assert 14 == Yatzy.chance(1,1,3,3,6)
    assert 15 == Yatzy.chance(2,3,4,5,1)
    
@pytest.mark.yatzy
def test_dice_with_same_number():
    assert 50 == Yatzy.yatzy(1,1,1,1,1)
    assert 50 == Yatzy.yatzy(2,2,2,2,2)
    assert 50 == Yatzy.yatzy(3,3,3,3,3)
    assert 50 == Yatzy.yatzy(4,4,4,4,4)
    assert 50 == Yatzy.yatzy(5,5,5,5,5)
    assert 50 == Yatzy.yatzy(6,6,6,6,6)
    assert 0 == Yatzy.yatzy(1,2,5,4,3)
    assert 0 == Yatzy.yatzy(2,1,1,1,2)

@pytest.markm