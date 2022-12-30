# Content

-   [**Yahtzee**](#yahtzee)
-   [**Goal**](#goal)
-   [**Objects**](#objects)
-   [**Instructions**](#instructions)
-   [**In game**](#in-game)
-   [**The end of the game and winner**](#the-end-of-the-game-and-winner)
- 	[**Yahtzee sheet**](#yahtzee-sheet)

# Yahtzee

This is an [exercise](https://github.com/emilybache/Yatzy-Refactoring-Kata) from [Emily Bache](https://github.com/emilybache) and it's about to refactor a code in Python language also involves TDD (Test Driven Development),the aim of this task is start with the programmation oriented to objects.

# Goal

The goal of the game is to get the highest score by rolling five dice. Each player will roll the dice three times to try to get one of the possible combinations.

# Objects

 -  Five dice
 -  A glass for dice
 -  Yatzy stylesheet to write down the score
 -  Instructions
 
# Instructions

The combinations are divided into two sections: Upper and Lower.In the Top Section you will score combinations scores of a single number of points on the die. You should try to get the most equal dice so that you get a higher score. The score you'll score will be the sum of the points you're looking for. For example, if you get three dice out of five, you're going to multiply three by five which equals fifteen and that's your score. If the sum of your points in this section is greater than 63, you will get a bonus of 35 points. In the Lower Section the possible combinations are more varied and include:

- 3 of a class: You must get three equal dice. You add up the score of all the dice.
- 4 of a class: You must get four equal dice. You add up the score of all the dice.
- "Full House": You must get three dice from one class and two from another. For example, three out of 1 and two out of 5. This move is worth 25 points.
- "Small Straight": You must get four consecutive dice. For example: 1, 2, 3 and 4 or 3, 4, 5 and 6. This play is worth 30 points.
- "Large Straight": You must get five consecutive dice. For example: 1, 2, 3, 4 and 5 or 2, 3, 4, 5 and 6. This play is worth 40 points.
- Yahtzee: You must get five equal dice of the same class. This play is worth 50 points.
- "Chance": Here you can score any play you get. The score will be the sum of all the dice. It is a move that allows you not to lose the shot when you do not have any other scoring options available.

# In game

Each player takes a point sheet. Everyone rolls the five dice in turn. Whoever gets the highest score starts the game. He will then be followed by the player on the left.
When it's your turn, you can roll all five dice up to three times. The dice are rolled by placing them in the glass, shaking them and then gently throwing them on the table. On the first throw you can decide to score the score or set aside those dice you want to save for your play. In the second you will roll those dice that you do not want to set aside. 
At this point you can write down your score or set aside the dice you want, which may be different from the ones you first chose. If you wish you can roll the dice for the third time. After the third shot you must decide what score you will score in one of the boxes. If you do not have plays available you must score a zero.

# The end of the game and winner

The game ends when all players have filled with some score, which can be zero, the thirteen squares. At this point we proceed to add the points. If you get more than 63 points in the Top Section you add 35 bonus points. You must remember to add all bonus points for additional Yahtzee in the Bottom Section. The player who gets the highest score by adding the points of the Upper and Lower Section will win the game.

# Yahtzee sheet

![yatzy](https://user-images.githubusercontent.com/114516225/210104084-9b05bf2c-cf8d-444e-8ba4-4f84b26c516d.jpg)
