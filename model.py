import numpy as np

class Game():
    def __init__(self, grid_size):
        self.grid = grid_size
        self.score = 0
        self.is_finished = False
        self.is_won = False
        self.set_board()

    # Patrastel xaxadashty
    def set_board(self):
        # Lcnum enq matrixy zronerov
        self.board = np.zeros((self.grid, self.grid), dtype=int)
        self.add_num()

    # Avelacnel mek tiv
    def add_num(self):
        if 0 in self.board:
            i, j = self.get_random_position()
            self.board[i][j] = np.random.choice([2, 4])

    # Gtnel azat vandak
    def get_random_position(self):
        zeros = np.argwhere(self.board == 0) # Indices where board == 0
        indices = np.ravel_multi_index([zeros[:, 0], zeros[:, 1]], self.board.shape)
        ind = np.random.choice(indices)
        i, j = np.unravel_index(ind, self.board.shape)
        return i, j

    # TO-DO: Check if moves are available
    def is_move_available(self):
        is_horiz_available = False
        is_vert_available = False

        for line in self.board:
            for i in range(len(line[line != 0]) - 1):
                if line[i] == line[i + 1]:
                    is_horiz_available = True
                    break
        for line in self.board.transpose():
            for i in range(len(line[line != 0]) - 1):
                if line[i] == line[i + 1]:
                    is_vert_available = True
                    break

        return is_horiz_available, is_vert_available

    def stack(self, move):
        is_moved = False
        # Dzax
        if move == 'l':
            # amen sharqi hamar
            for i, line in enumerate(self.board):
                line = line[line != 0]
                # amen tvi hamar tvyal sharqum
                zero_iterator = 0
                while zero_iterator < len(line) - 1 and len(line) > 1:
                    if line[zero_iterator] == line[zero_iterator + 1]:
                        line[zero_iterator] *= 2
                        line[zero_iterator + 1] = 0
                    zero_iterator += 1
                line = line[line != 0]
                line = np.insert(line, len(line), [ 0 for _ in range(self.grid - len(line)) ])
                if not np.array_equal(self.board[i], line):
                    self.board[i] = line
                    is_moved = True
            if is_moved:
                self.add_num()

        # Aj
        elif move == 'r':
            # amen sharqi hamar
            for i, line in enumerate(self.board):
                line = line[line != 0]
                # amen tvi hamar tvyal sharqum
                zero_iterator = len(line) - 1
                while zero_iterator > 0 and len(line) > 1:
                    if line[zero_iterator] == line[zero_iterator - 1]:
                        line[zero_iterator] *= 2
                        line[zero_iterator - 1] = 0
                    zero_iterator -= 1
                line = line[line != 0]
                line = np.insert(line, 0, [ 0 for _ in range(self.grid - len(line)) ])
                if not np.array_equal(self.board[i], line):
                    self.board[i] = line
                    is_moved = True
            if is_moved:
                self.add_num()

        # Nerqev (dzhoxq)
        elif move == 'b':
            self.board = self.board.transpose()
            # amen sharqi hamar
            for i, line in enumerate(self.board):
                line = line[line != 0]
                # amen tvi hamar tvyal sharqum
                zero_iterator = len(line) - 1
                while zero_iterator > 0 and len(line) > 1:
                    if line[zero_iterator] == line[zero_iterator - 1]:
                        line[zero_iterator] *= 2
                        line[zero_iterator - 1] = 0
                    zero_iterator -= 1
                line = line[line != 0]
                line = np.insert(line, 0, [ 0 for _ in range(self.grid - len(line)) ])
                if not np.array_equal(self.board[i], line):
                    self.board[i] = line
                    is_moved = True
            if is_moved:
                self.add_num()
            self.board = self.board.transpose()

        # Verev
        elif move == 'u':
            self.board = self.board.transpose()
            # amen sharqi hamar
            for i, line in enumerate(self.board):
                line = line[line != 0]
                # amen tvi hamar tvyal sharqum
                zero_iterator = 0
                while zero_iterator < len(line) - 1 and len(line) > 1:
                    if line[zero_iterator] == line[zero_iterator + 1]:
                        line[zero_iterator] *= 2
                        line[zero_iterator + 1] = 0
                    zero_iterator += 1
                line = line[line != 0]
                line = np.insert(line, len(line), [ 0 for _ in range(self.grid - len(line)) ])
                if not np.array_equal(self.board[i], line):
                    self.board[i] = line
                    is_moved = True
            if is_moved:
                self.add_num()
            self.board = self.board.transpose()

    def make_move(self, move):
        self.stack(move)
        self.update_score()
        # self.check_finish()

    def update_score(self):
        self.score = int(self.board.sum())

    def check_finish(self):
        if 2048 in self.board and self.is_won is False:
            self.is_won = True
            print()
            print("CONGRATULATIONS!!! YOU WON!!!")
            print()

        is_horiz_available, is_vert_available = self.is_move_available()
        if 0 not in self.board and not is_horiz_available and not is_vert_available:
            self.is_finished = True
            print("GAME OVER")
            # exit()

    def show_model(self):
        self.update_score()
        print('Score:', self.score)
        print(self.board)
        print()

    def left_arrow(self, _):
        self.make_move('l')
        self.show_model()
        self.check_finish()

    def right_arrow(self, _):
        self.make_move('r')
        self.show_model()
        self.check_finish()

    def up_arrow(self, _):
        self.make_move('u')
        self.show_model()
        self.check_finish()

    def down_arrow(self, _):
        self.make_move('b')
        self.show_model()
        self.check_finish()

class Model():
    def __init__(self, grid_size):
        self.game = Game(grid_size)
