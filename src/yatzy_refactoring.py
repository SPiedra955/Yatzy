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
        else:
            return 50       
    
    @staticmethod
    def ones(*rolls_dice):
        return rolls_dice.count(1)*1
    
    @staticmethod
    def twos(*rolls_dice):
        return rolls_dice.count(2)*2
    
    @staticmethod
    def threes(*rolls_dice):
        return rolls_dice.count(3)*3
    
    @staticmethod
    def fours(*rolls_dice):
        return rolls_dice.count(4)*4
    
    @staticmethod
    def fives(*rolls_dice):
        return rolls_dice.count(5)*5
    
    @staticmethod
    def sixes(*rolls_dice):
        return rolls_dice.count(6)*6
    
    @staticmethod
    def highest_pair(*rolls_dice):
        pair = 2
        for number in rolls_dice:
            if rolls_dice.count(number) >= 2:
                return pair * number
        else:
            return 0
        