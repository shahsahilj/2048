# 2048
Minimax algorithm for 2048 game


Description of code:

1 PlayerAI.py - This file computes the first children of the current board and computes the minimax value of each child. It the compares which has the max value and returns the move accordingly
I have implemented DFS using a fixed depth of 5 including the first ply and considering each min and max as a separate depth.

2 Minimaxab.py - This file is the implementation of the alpha-beta minimax algorithm

3 Helper.py - This file is the structure class used by the other codes. It has methods like getAvailableChildren(), canMove(), move(), merge(), heuristic(). The structure of the grid is changed to a one dimentional array to improve the efficiency of the code. Also these methods are improved to get a faster implementation. The heuristic() method calculates the utility of a given state. The 3 main heuristics used are: maximizing the number of empty tiles, keeping the max value on top left corner, and creating a snakelike pattern of decreasing numbers to facilitate easier combination. To implement the snake like patter different weights are given to each position and these are multiplied to the position values. This increases the likelihood of the order being maintained. The empty tiles are used when computing the final factor of the heuristic. A bonus is added to the score if the max tile is at top left corner. I also implemented the code for monotonicity and smoothness. However, when I tried to combine it with the other heuristics it disrupted the the grid more. So for the end testing I have included only the code for the previous three heuristics.


The following files were already provided by the professor(since aim of the class was to implement the AI algorithm for the player):

4 BaseAI.py - The general structure of the AI system

5. BaseDisplayer.py - Code for inheriting by Displayer

6. Displayer.py - Showing the current state of the board

7. ComputerAI.py - Generating the random tile at random position

8. Grid.py - Structure of the game board

9. GameManager.py - Central control of the game



Results:

I ran the code 50 times. The end state maxTile obtained is as follows:

For the alpha-beta pruning code:

512 - 22%
1024 - 44%
2048 - 34%
