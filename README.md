# Wumpus-World-Q-Learning
## About the game
Wumpus World is the representation of a simple world where an explorer searches a dark, dangerous cave in search for a bounty of gold. In this cave, there are two threats to the explorer’s life: falling in bottomless pits (P) and being slain by the Wumpus (W). The explorer’s goal is to find the gold (G) then exit safely by backtracking through the cave. Typically, the cave is represented by a 4×4 grid or 16 rooms. Each room will have indicators that can be detected by the explorer. If the explorer smells a stench (S) that means that Wumpus may be in an adjacent tile. If the explorer feels a breeze (B) that means that a bottomless pit may be in an adjacent tile. If the agent sees glitter that means that there is gold in the current room and upon retrieval of the gold, the explorer is allowed to leave the cave. While exploring the cave, the explorer gathers knowledge and acts according to the gathered knowledge; this type of behavior makes the explorer a knowledge-based agent.

![map](https://repository-images.githubusercontent.com/254698189/4d035600-0afd-11eb-8052-a3f9a9d74041)

---
## Playing the game
In the following code, we use q-learning algorithm to solve this game. At the end, agent will be able to find the gold.
#### Information needs
* Number of rows and columns
* Starting point
* Wumpus, gold and pits points
* Hyperparameters (learning rate, discount rate, epsilon)

---
## Q-Learning Process
![process](https://cdn-media-1.freecodecamp.org/images/oQPHTmuB6tz7CVy3L05K1NlBmS6L8MUkgOud)
