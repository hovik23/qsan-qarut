import numpy as np
import random

class Game():
	def __init__(self, N):
		self.grid = N
		self.score = 0
		self.is_finished = False
		self.is_won = False
		self.set_board()

	# Patrastel xaxadashty
	def set_board(self):
		# Lcnum enq matrixy zronerov
		self.board = np.zeros((self.grid, self.grid), dtype=int)

		# Erku tex 2 enq avelacnum (vor anpayman tarber texer linen)
		for _ in range(2):
			self.add_num()

	# Avelacnel mek tiv
	def add_num(self):
		if 0 in self.board:
			i, j = self.get_random_position()
			self.board[i][j] = 2

	# Gtnel azat vandak
	def get_random_position(self):
		zeros = np.argwhere(self.board == 0) # Indices where board == 0
		indices = np.ravel_multi_index([zeros[:, 0], zeros[:, 1]], self.board.shape)
		ind = np.random.choice(indices)
		i, j = np.unravel_index(ind, self.board.shape)
		return i, j

	def is_move_available(self):
		is_horiz_available = False
		is_vert_available = False

		is_left_available = False
		is_right_available = False
		is_up_available = False
		is_down_available = False

		# stugum enq, ardyoq qayl ka "dba" dzax kam aj
		for line in self.board:
			line = line[line != 0]
			for i in range(len(line) - 1):
				if line[i] == line[i + 1]:
					is_horiz_available = True

		# stugum enq, ardyoq qayl ka "dba" nerqev kam verev
		for line in self.board.transpose():
			if 0 in line:
				is_vert_available = True
			line = line[line != 0]
			for i in range(len(line) - 1):
				if line[i] == line[i + 1]:
					is_vert_available = True

		return is_horiz_available, is_vert_available

	def stack(self, move):
		is_horiz_available, is_vert_available = self.is_move_available()

		# Dzax
		if move == 'l':
			# amen sharqi hamar
			for i, line in enumerate(self.board):
				line = line[line != 0]
				# amen tvi hamar tvyal sharqum
				p = 0
				while p < len(line) - 1 and len(line) > 1:
					if line[p] == line[p + 1]:
						line[p] *= 2
						line[p + 1] = 0
					p += 1
				line = line[line != 0]
				line = np.insert(line, len(line), [ 0 for _ in range(self.grid - len(line)) ])
				self.board[i] = line

		# Aj
		elif move == 'r':
			# amen sharqi hamar
			for i, line in enumerate(self.board):
				line = line[line != 0]
				# amen tvi hamar tvyal sharqum
				p = len(line) - 1
				while p > 0 and len(line) > 1:
					if line[p] == line[p - 1]:
						line[p] *= 2
						line[p - 1] = 0
					p -= 1
				line = line[line != 0]
				line = np.insert(line, 0, [ 0 for _ in range(self.grid - len(line)) ])
				self.board[i] = line

		elif move == 'b':
			self.board = self.board.transpose()
			# amen sharqi hamar
			for i, line in enumerate(self.board):
				line = line[line != 0]
				# amen tvi hamar tvyal sharqum
				p = 0
				while p < len(line) - 1 and len(line) > 1:
					if line[p] == line[p + 1]:
						line[p] *= 2
						line[p + 1] = 0
					p += 1
				line = line[line != 0]
				line = np.insert(line, 0, [ 0 for _ in range(self.grid - len(line)) ])
				self.board[i] = line
			self.board = self.board.transpose()

		elif move == 'u':
			self.board = self.board.transpose()
			# amen sharqi hamar
			for i, line in enumerate(self.board):
				line = line[line != 0]
				# amen tvi hamar tvyal sharqum
				p = len(line) - 1
				while p > 0 and len(line) > 1:
					if line[p] == line[p - 1]:
						line[p] *= 2
						line[p - 1] = 0
					p -= 1
				line = line[line != 0]
				line = np.insert(line, len(line), [ 0 for _ in range(self.grid - len(line)) ])
				self.board[i] = line
			self.board = self.board.transpose()
					
	def make_move(self, move):
		self.stack(move)
		self.update_score()
		self.check_finish()

	def update_score(self):
		self.score = int(self.board.sum())

	def check_finish(self):
		if 2048 in self.board and self.is_won == False:
			self.is_won = True
			print()
			print("CONGRATULATIONS!!! YOU WON!!!")
			print()

		is_horiz_available, is_vert_available = self.is_move_available()
		if 0 not in self.board and not is_horiz_available and not is_vert_available:
			self.is_finished = True
			print("GAME OVER")
			exit()

	def show_model(self):
		self.update_score()
		print('Score:', self.score)
		print(self.board)
		print()

	def left_arrow(self, event):
		self.make_move('l')
		self.add_num()
		self.show_model()
		self.check_finish()

	def right_arrow(self, event):
		self.make_move('r')
		self.add_num()
		self.show_model()
		self.check_finish()

	def up_arrow(self, event):
		self.make_move('u')
		self.add_num()
		self.show_model()
		self.check_finish()

	def down_arrow(self, event):
		self.make_move('b')
		self.add_num()
		self.show_model()
		self.check_finish()

class Model():
	def __init__(self, N):
		self.game = Game(N)