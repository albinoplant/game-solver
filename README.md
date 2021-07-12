# game-solver

Python project I develop to solve [Water Sort Puzzle](https://apps.apple.com/us/app/water-sort-puzzle/id1514542157) levels.

Original puzzle's goal is to sort the water in flasks, so that each flask contains only one color of liquid and is fully filled.


![alt text](https://i.ytimg.com/vi/ez1Wo78TyfU/maxresdefault.jpg "Water Sort Puzzle screenshot")
### TODO

- [x] Base class of the game - Flask
- [x] Game class that manages the rules and is composed of Flask List
- [x] Helper method to print current state of the game to the console
- [x] Method to calculate list of possible moves in the current state
- [x] Refactor code so that pouring action is the method of Flask class and Game class only checks if this action is allowed
- [ ] Method that tries to solve the puzzle by randomly selecting one of possible choices
- [ ] Implement system that optionally prevents the algorithm going backwards 
- [ ] Implement learning mechanism