import model as m
import view as v
import controller as c

N = 4

model = m.Model(N)
model.game.set_board()
print('Start:')
model.game.show_model()
print()

while model.game.is_won is False:
	move = input("Qayl:")
	print("Making move...")
	model.game.make_move(move) # stack enq anum
	print('Adding a num...')
	model.game.add_num()
	print("New matrix:")
	model.game.show_model()
	print()