from src.enumerateDices import Pips

class Yatzy:
    
    @staticmethod
    def chance(*rolls_dice):
        score = 0
        for number in rolls_dice:
            score += number
        return score
    
    @staticmethod
    def yatzy(*rolls_dice):
        for number in rolls_dice:
            if number != rolls_dice[0]: 
                return 0
        return 50     
    
    @staticmethod
    def ones(*rolls_dice):
        one = Pips.one.value
        return rolls_dice.count(one) * one
    
    @staticmethod
    def twos(*rolls_dice):
        two = Pips.two.value
        return rolls_dice.count(two) * two
    
    @staticmethod
    def threes(*rolls_dice):
        three = Pips.three.value
        return rolls_dice.count(three) * three
    
    @staticmethod
    def fours(*rolls_dice):
        four = Pips.four.value
        return rolls_dice.count(four) * four
    
    @staticmethod
    def fives(*rolls_dice):
        five = Pips.five.value
        return rolls_dice.count(five) * five

    @staticmethod
    def sixes(*rolls_dice):
        six = Pips.six.value
        return rolls_dice.count(six) * six
    
    @staticmethod
    def score_pair(*rolls_dice):
        pair = 2
        for pip in Pips.reversedValues():
            if rolls_dice.count(pip) >= pair:
                return pair * pip
        return 0
    
    @classmethod
    def __biggest_pip_repeated(cls, rolls_dice, times):
        pips = cls.__filter_pips_repeated(rolls_dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, rolls_dice, times):
        return list(filter(lambda pip: rolls_dice.count(pip) >= times, Pips.reversedValues()))
    
    @classmethod
    def score_double_pair(cls, *rolls_dice):
        PAIR = 2
        pips_pairs = cls.__filter_pips_repeated(rolls_dice, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == 2 else 0

    @classmethod
    def three_of_a_kind(cls, *rolls_dice):
        THREE = 3
        pip = cls.__biggest_pip_repeated(rolls_dice, THREE)
        return pip * THREE if pip else 0

    @classmethod
    def four_of_a_kind(cls, *rolls_dice):
        FOUR = 4
        pip = cls.__biggest_pip_repeated(rolls_dice, FOUR)
        return pip * FOUR if pip else 0

    @classmethod
    def small_straight(cls, *rolls_dice):
        return cls.chance(*rolls_dice) if not Pips.minus(Pips.six) - set(rolls_dice) else 0
        
    @classmethod
    def large_straight(cls, *rolls_dice):
        return cls.chance(*rolls_dice) if not Pips.minus(Pips.one) - set(rolls_dice) else 0

    @classmethod
    def full_house(cls, *rolls_dice):
        if cls.two_of_a_kind(*rolls_dice) and cls.three_of_a_kind(*rolls_dice):
            return cls.two_of_a_kind(*rolls_dice) + cls.three_of_a_kind(*rolls_dice)
        return 0
    
    @classmethod
    def two_of_a_kind(cls, *dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0