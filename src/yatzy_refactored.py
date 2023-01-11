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
    def  ones(*rolls_dice):
        ONE = Pips.ONE.values()
        return rolls_dice.count(ONE) * ONE
    
    @staticmethod
    def twos(*rolls_dice):
        TWO = Pips.TWO.values()
        return rolls_dice.count(TWO) * TWO
    
    @staticmethod
    def threes(*rolls_dice):
        THREE = Pips.THREE.values()
        return rolls_dice.count(THREE) * THREE
    
    @staticmethod
    def fours(*rolls_dice):
        FOUR = Pips.FOUR.values()
        return rolls_dice.count(FOUR) * FOUR
    
    @staticmethod
    def fives(*rolls_dice):
        FIVE = Pips.FIVE.values()
        return rolls_dice.count(FIVE) * FIVE
    
    @staticmethod
    def sixes(*rolls_dice):
        SIX = Pips.SIX.values()
        return rolls_dice.count(SIX) * SIX
    
    @staticmethod
    def score_pair(*rolls_dice):
        pair = 2
        for number in rolls_dice:
            if rolls_dice.count(number) >= pair:
                return pair * number
        else:
            return 0
    
    @staticmethod
    def score_double_pair(*rolls_dice):
        score = 0
        pairsFound = 0
        for number in range(7):
            if pairsFound == 2:
                return score
            if rolls_dice.count(number) >= 2:
                score += number * 2
                pairsFound += 1
        else:
            return 0
    
    @staticmethod
    def three_of_a_kind(*rolls_dice):
        for number in rolls_dice:
            if rolls_dice.count(number) >= 3:
                return number * 3
        else:
            return 0

    @staticmethod
    def four_of_a_kind(*rolls_dice):
        for number in rolls_dice:
            if rolls_dice.count(number) >= 4:
                return number * 4
        else:
            return 0
    
    @staticmethod
    def small_straight(*rolls_dice):
        for number in range(1, 6):
            if rolls_dice.count(number) != 1:
                return 0
        else:
            return sum(rolls_dice)
        
    @staticmethod
    def large_straight(*rolls_dice):
        for number in range (2, 7):
            if rolls_dice.count(number) != 1:
                return 0
        else:
            return sum(rolls_dice)
    
    @staticmethod
    def full_house(*rolls_dice): 
        
        score = 0
        pairFound = 0
        threeFound = 0     
        
        for number in range(7):
            if rolls_dice.count(number) == 3:
                score += number * 3
                threeFound = 1
            elif rolls_dice.count(number) == 2:
                score += number * 2
                pairFound += 1
        if threeFound == 1 and pairFound == 1:
            return score
        else:
            return 0