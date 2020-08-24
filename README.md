# Othello
1. In general, the game can only have 3 classes. A board, a disk, and game
controller. 

2. Some of the methods in human_make_move and ai_make_move should be in game
manager and disk and board.

3. Separate codes into smaller chunks so that they can be in unit test.

4. Details:
    Disk should be able to flip itself. 
    If the AI is a more complex AI, probrably make it its own class.
    Game manager and game controller are similar names. Better name the current
    game controller as move_manager or something. The name needs to be more 
    explicit.