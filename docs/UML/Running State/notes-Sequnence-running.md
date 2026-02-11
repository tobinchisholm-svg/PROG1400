Here is a **simple, beginner‑friendly explanation** of the sequence you posted.  
No technical jargon — just a clear explanation of what happens step‑by‑step during **one game tick** in the Running state.

***

# ✅ **Simple Explanation of the Sequence Diagram**

This is what happens **every time the game updates** (every tick):

***

### **1. The game loop starts**

The **GameController** begins the next update of the game.

***

### **2. The game gets the player’s direction**

*   GameController asks the **InputHandler** what direction the player pressed.
*   InputHandler sends back the direction (up, down, left, right).

***

### **3. The snake’s head updates its direction**

*   GameController tells the **SnakeHead** to use that direction.
*   (SnakeHead will ignore invalid moves like reversing 180°.)

***

### **4. The game checks where the snake wants to move next**

*   GameController asks SnakeHead:  
    **“If you move in that direction, what is the next tile?”**
*   SnakeHead returns the new position.

***

### **5. The game checks if the next tile is inside the grid**

*   GameController asks the **Grid** whether the position is inside the borders.
*   If it is *not* inside, the game ends (snake hit the wall).

***

### **6. The game checks if the snake will hit its own tail**

*   GameController asks the **SnakeBody** if the next tile is already occupied.
*   If yes → the game ends (snake hit itself).

***

### **7. The game checks if the next tile has an apple**

*   GameController asks the **Apple** if one is at that tile.
*   If yes:
    *   Snake grows
    *   Player gets points
    *   A new apple is spawned

***

### **8. The snake moves**

If the snake is still alive:

*   GameController tells **SnakeHead** to move to that new tile.
*   GameController then tells **SnakeBody** to follow the head (the tail shifts forward).

***

### **That’s the end of one game tick**

The process repeats over and over, creating the continuous movement and rules of Snake.

***


