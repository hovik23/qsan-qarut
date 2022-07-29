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
		i, j = self.get_random_position()
		while self.board[i][j] != 0:
			i, j = self.get_random_position()
		self.board[i][j] = 2

	# Gtnel azat vandak
	def get_random_position(self):
		i = random.randint(0, self.grid - 1)
		j = random.randint(0, self.grid - 1)
		return i, j

	def stack(self, move):
		# Dzax
		if move == 'l':
			# amen sharqi hamar
			for line in self.board:
				# amen tvi hamar tvyal sharqum
				for i in range(len(line) - 1):
					if line[i] != 0:
						k = i
						while k + 1 < self.grid - 1 and line[k + 1] == 0:
							k += 1

						if line[k + 1] == line[i]:
							line[i] = line[i] * 2
							line[k + 1] = 0

		# Aj
		elif move == 'r':
			# amen sharqi hamar
			for line in self.board:
				# amen tvi hamar tvyal sharqum
				for i in range(len(line) - 1):
					if line[i] != 0:
						k = i
						while k + 1 < self.grid - 1 and line[k + 1] == 0:
							k += 1

						if line[k + 1] == line[i]:
							line[k + 1] = line[k + 1] * 2
							line[i] = 0

		elif move == 'u':
			# amen sharqi hamar
			self.board = self.board.transpose()
			for line in self.board:
				# amen tvi hamar tvyal sharqum
				for i in range(len(line) - 1):
					if line[i] != 0:
						k = i
						while k + 1 < self.grid - 1 and line[k + 1] == 0:
							k += 1

						if line[k + 1] == line[i]:
							line[i] = line[i] * 2
							line[k + 1] = 0
			self.board = self.board.transpose()
			

		elif move == 'b':
			# amen sharqi hamar
			self.board = self.board.transpose()
			for line in self.board:
				# amen tvi hamar tvyal sharqum
				for i in range(len(line) - 1):
					if line[i] != 0:
						k = i
						while k + 1 < self.grid - 1 and line[k + 1] == 0:
							k += 1

						if line[k + 1] == line[i]:
							line[k + 1] = line[k + 1] * 2
							line[i] = 0
			self.board = self.board.transpose()


	# Gtnel, te qani vandak e azat vorosh koxmic
	def get_shift(self, move):
		# "dba" dzax
		if move == 'l':
			shift_array = [ np.nonzero(line != 0)[0][0] if len(np.nonzero(line != 0)[0]) != 0 else 0 for line in self.board ]
			print("Left shift array:", shift_array)
			return shift_array

		# "dba" aj
		elif move == 'r':
			shift_array = [ self.grid - np.nonzero(line != 0)[0][-1] - 1 if len(np.nonzero(line != 0)[0]) != 0 else 0 for line in self.board ]
			print("Right shift array:", shift_array)
			return shift_array

	def shift(self, move):
		if move == 'l':
			for i, line in enumerate(self.board):
				line = line[line != 0]
				line = np.insert(line, len(line), [ 0 for i in range(self.grid - len(line)) ])
				self.board[i] = line
		elif move == 'r':
			for i, line in enumerate(self.board):
				line = line[line != 0]
				line = np.insert(line, 0, [ 0 for i in range(self.grid - len(line)) ])
				self.board[i] = line
		elif move == 'b':
			self.board = self.board.transpose()
			for i, line in enumerate(self.board):
				line = line[line != 0]
				line = np.insert(line, 0, [ 0 for i in range(self.grid - len(line)) ])
				self.board[i] = line
			self.board = self.board.transpose()
		elif move == 'u':
			self.board = self.board.transpose()
			for i, line in enumerate(self.board):
				line = line[line != 0]
				line = np.insert(line, len(line), [ 0 for i in range(self.grid - len(line)) ])
				self.board[i] = line 
			self.board = self.board.transpose()
					
	def make_move(self, move):
		self.stack(move)
		self.shift(move)

	def update_score(self):
		self.score = int(self.board.sum())

	def check_finish(self):
		if 2048 in self.board:
			self.is_won = True

	def show_model(self):
		self.update_score()
		# print('Score:', self.score)
		print(self.board)
		print()

class Model():
	def __init__(self, N):
		self.game = Game(N)