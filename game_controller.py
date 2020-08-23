LOCATION_1 = 48
LOCATION_2 = 84
TEXT_COLOR = (178, 34, 34)
TEXT_SIZE_BIG = 50
TEXT_SIZE_SMALL = 25
WHITE = 255
BLACK = 0


class GameController:
    '''maintains the state of the game, reports winner and record the game
    results'''
    def __init__(self, board, gm, WIDTH, HEIGHT):
        self.board = board
        self.gm = gm
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.black_count = 0  # user's points
        # a boolean variable that controls if the store_score method should be
        # called
        self.call_store_method = True
        # a boolean variable that controls if the score is a new high score
        self.new_high_score = False
        # a boolean variable that reflects if the game ends, used in draw()
        self.game_ends = False

    def end_game(self):
        '''
        end the game and call "result" when all spaces are taken,
         or no valid spaces
        '''
        # if no legal moves for either, end game
        if self.gm.no_ai_moves is True and self.gm.no_player_moves is True:
            self.result_display()
            self.game_ends = True
        # if no space left, end game
        else:
            for i in range(self.board.ROWS):
                for j in range(self.board.COLUMNS):
                    if self.board.spaces[i][j] is None:
                        return
            self.result_display()
            self.game_ends = True

    def result_display(self):
        '''print the result to the screen if either party wins or tie'''
        # count the total number of both players
        black_counter = 0
        white_counter = 0
        for i in range(len(self.board.spaces)):
            for item in self.board.spaces[i]:
                if item and item.color == WHITE:
                    white_counter += 1
        for i in range(len(self.board.spaces)):
            for item in self.board.spaces[i]:
                if item and item.color == BLACK:
                    black_counter += 1

        self.black_count = black_counter  # update user's points

        black_count_message = "The Black has " + str(black_counter) + " tiles"
        white_count_message = "The White has " + str(white_counter) + " tiles"
        # when black tiles win
        if black_counter > white_counter:
            fill(*TEXT_COLOR)
            textSize(TEXT_SIZE_BIG)
            textAlign(CENTER)
            text("BLACK WINS!", self.WIDTH/2, self.HEIGHT/2)
            textSize(TEXT_SIZE_SMALL)
            text(black_count_message, self.WIDTH/2, self.HEIGHT/2 + LOCATION_1)
            text(white_count_message, self.WIDTH/2, self.HEIGHT/2 + LOCATION_2)
        # when white tiles win
        elif white_counter > black_counter:
            fill(*TEXT_COLOR)
            textSize(TEXT_SIZE_BIG)
            textAlign(CENTER)
            text("WHITE WINS!", self.WIDTH/2, self.HEIGHT/2)
            textSize(TEXT_SIZE_SMALL)
            text(white_count_message, self.WIDTH/2, self.HEIGHT/2 + LOCATION_1)
            text(black_count_message, self.WIDTH/2, self.HEIGHT/2 + LOCATION_2)
        # when it's a tie
        else:
            fill(*TEXT_COLOR)
            textSize(TEXT_SIZE_BIG)
            textAlign(CENTER)
            text("IT'S A TIE!", self.WIDTH/2, self.HEIGHT/2)
            textSize(TEXT_SIZE_SMALL)
            text(black_count_message, self.WIDTH/2, self.HEIGHT/2 + LOCATION_1)
            text(white_count_message, self.WIDTH/2, self.HEIGHT/2 + LOCATION_2)

    def store_score(self, filename):
        '''store the score'''
        answer = self.input("What's your name?")
        if answer:
            answer = answer
        elif answer == "":
            answer = "Anonymous"  # store as "Anonymous" if not entered
        else:
            self.call_store_method = False  # don't store if "cancel"
            return

        # create the file if not already
        results = open(filename, "a")

        # generate the string to store
        record = (answer + " " + str(self.black_count))
        self.compare_score(filename)  # check if it's a new high score
        if not self.new_high_score:
            results = open(filename, "a")  # append the record to the end
            results.write(record + "\n")
        else:
            # append the record to the beginning of the file
            results = open(filename, "r+")
            content = results.read()
            results.seek(0)  # add the new high score to the beginning
            results.write(record + "\n" + content)
        results.close()
        self.call_store_method = False  # makes sure only stores the score once

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def compare_score(self, filename):
        '''compares and see if the score is a new highest score'''
        scores = []  # a list to store current scores

        try:
            results = open(filename)
        except FileNotFoundError:
            print("File cannot be opened.")

        # get a list of all scores
        for line in results:
            words = line.strip().split(" ")
            score = int(words[len(words) - 1])
            scores.append(score)

        # decide if the score is a new high score
        for score in scores:
            if score >= self.black_count:
                return
        self.new_high_score = True
