# Othello
* Othello is a strategy board game for two players, played on an uncheckered board. During a play, any disks of the opponent's color that are in a straight line and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color.The object of the game is to have the majority of disks turned to display your color when the last playable empty square is filled.

* I wrote a “smart_ai” method in my game_controller. 
    Whenever it’s the AI’s turn, “ai_make_move” will call “smart_ai”.
    "Smart_ai" is a greedy method that choose the step that will flip most disks.
* The AI player becomes smarter. Before I just let the AI randomly choose from
    legal moves, and it was very easy to beat the computer.
* If I don’t have the “smart_ai” method, most players won. 
    After I have it, few people won. 
* Even though the AI became smarter, it’s still possible to beat it. 
    Especially when I aim for the corners and the edges, the AI tends to fail.
