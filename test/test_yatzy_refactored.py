from src.yatzy_refactored import Yatzy
from src.yatzyEnums import Yatzy
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

@pytest.mark.ones
def test_dice_with_ones():
    assert 2 == Yatzy.ones(1,2,5,6,1)
    assert 3 == Yatzy.ones(1,3,1,5,1)
    assert 4 == Yatzy.ones(1,6,1,1,1)

@pytest.mark.twos
def test_dice_with_twos():
    assert 4 == Yatzy.twos(2,2,3,4,5)
    assert 6 == Yatzy.twos(2,3,6,2,2)
    assert 8 == Yatzy.twos(2,2,5,2,2)

@pytest.mark.threes
def test_with_threes():
    assert 6 == Yatzy.threes(3,1,2,5,3)
    assert 9 == Yatzy.threes(3,3,3,4,1)
    assert 12 == Yatzy.threes(3,3,3,3,2)
    
@pytest.mark.fours
def test_with_fours():
    assert 8 == Yatzy.fours(3,4,2,4,3)
    assert 12 == Yatzy.fours(4,2,4,4,1)
    assert 16 == Yatzy.fours(4,2,4,4,4)

@pytest.mark.fives
def test_with_fives():
    assert 10 == Yatzy.fives(5,2,1,3,5)
    assert 15 == Yatzy.fives(5,3,5,4,5)
    assert 20 == Yatzy.fives(5,2,5,5,5)
    
@pytest.mark.sixes
def test_with_sixes():
    assert 12 == Yatzy.sixes(6,5,1,5,6)
    assert 18 == Yatzy.sixes(6,6,6,1,1)
    assert 24 == Yatzy.sixes(6,6,1,6,6)

@pytest.mark.pair
def test_pair_of_dices():
    assert 0 == Yatzy.score_pair(1,3,2,4,6)
    assert 10 == Yatzy.score_pair(5,1,1,2,5)
    assert 12 == Yatzy.score_pair(6,4,4,1,6)

@pytest.mark.double_pair
def test_double_pairs():
    assert 0 == Yatzy.score_double_pair(1,1,2,3,4)
    assert 6 == Yatzy.score_double_pair(1,1,2,2,2)
    assert 8 == Yatzy.score_double_pair(3,3,2,1,1)
    
@pytest.mark.three_of_a_kind
def test_three_of_a_kind():
    assert 0 == Yatzy.three_of_a_kind(1,2,2,1,5)
    assert 3 == Yatzy.three_of_a_kind(1,2,1,1,4)
    assert 9 == Yatzy.three_of_a_kind(5,3,1,3,3)

@pytest.mark.four_of_a_kind
def test_four_of_a_kind():
    assert 0 == Yatzy.four_of_a_kind(1,1,2,1,5)
    assert 20 == Yatzy.four_of_a_kind(5,2,5,5,5)
    assert 24 == Yatzy.four_of_a_kind(6,3,6,6,6)

@pytest.mark.small_straight
def test_small_straight():
    assert 0 == Yatzy.small_straight(1,2,3,4,6)
    assert 15 == Yatzy.small_straight(1,2,3,4,5)
    assert 15 == Yatzy.small_straight(5,4,3,2,1)

@pytest.mark.large_straight
def test_large_straight():
    assert 0 == Yatzy.large_straight(1,2,3,4,5)
    assert 20 == Yatzy.large_straight(2,3,4,5,6)
    assert 20 == Yatzy.large_straight(6,4,5,2,3)

@pytest.mark.full_house
def test_full_house():
    assert 0 == Yatzy.full_house(2,2,2,1,5)
    assert 8 == Yatzy.full_house(1,1,2,2,2)
    assert 15 == Yatzy.full_house(6,6,1,1,1)