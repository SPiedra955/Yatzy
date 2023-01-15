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
        return rolls_dice.count(1) * 1
    
    @staticmethod
    def twos(*rolls_dice):
        return rolls_dice.count(2) * 2
    
    @staticmethod
    def threes(*rolls_dice):
        return rolls_dice.count(3) * 3
    
    @staticmethod
    def fours(*rolls_dice):
        return rolls_dice.count(4) * 4
    
    @staticmethod
    def fives(*rolls_dice):
        return rolls_dice.count(5) * 5
    
    @staticmethod
    def sixes(*rolls_dice):
        return rolls_dice.count(6) * 6
    
    @staticmethod
    def score_pair(*rolls_dice):
        pair = 2
        for number in rolls_dice:
            if rolls_dice.count(number) >= pair:
                return pair * number
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
        return 0
 
    @staticmethod
    def three_of_a_kind(*rolls_dice):
        for number in rolls_dice:
            if rolls_dice.count(number) >= 3:
                return number * 3
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