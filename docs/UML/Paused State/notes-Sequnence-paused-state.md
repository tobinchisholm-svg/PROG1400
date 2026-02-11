Here is a **simple, clear explanation** of what is happening in your **Paused State** sequence diagram.  
You can copy‑paste this into your PROG1400 assignment.

***

# ✅ **Simple Explanation of the Paused State Sequence**

This diagram shows what happens when the game is **paused**.  
Nothing in the game world moves — the snake, apple, and grid all stay frozen.  
The only thing the game cares about is whether the player wants to **resume** or use pause menu options.

Here is the step‑by‑step explanation:

***

### **1. The game enters the Paused state**

A note explains that the **game is paused**.  
This means:

*   no movement
*   no updates
*   no collisions
*   no apple spawning

Everything is completely frozen.

***

### **2. The pause menu appears**

The **GameController** tells the **Pause Menu UI** to show the pause screen.

This is the menu the player sees, usually with options like:

*   Resume
*   Settings
*   Exit to Main Menu

***

### **3. The game waits for the player**

A loop begins where:

*   The **GameController** asks the **InputHandler**:  
    “Did the player press a button?”
*   The InputHandler sends back the player’s choice.

This repeats over and over **until the player chooses something**.

During this loop, gameplay objects like SnakeHead, SnakeTail, Apple, and Grid do **nothing**.  
They are only listed so you know they still exist, but they are inactive.

***

### **4. The GameController decides what to do next**

The GameController checks what the player selected:

#### ✔ **If the player selects “Resume”**

*   The GameController changes the game state back to **Running**.
*   Gameplay continues exactly where it left off.

#### ✔ **If the player selects another menu option**

Example: Settings or Help

*   The GameController tells the Pause Menu UI to show that screen.

***

# ⭐ **Summary**

*   The **GameController** is the boss in this state — it makes all decisions.
*   **PauseMenu UI** only displays the menu.
*   **InputHandler** only reports what the player pressed.
*   **Snake, Apple, Grid** stay frozen and do nothing.
*   The game stays paused until the player chooses **Resume**.


