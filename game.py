import model as m
import view as v

N = 4

class Controller():
	def __init__(self):
		self.model = m.Model(N)
		self.view = v.View()

	def update_view(self, event):
		self.view.score_label["text"] = "Score: " + str(self.model.game.score)
		# self.view.window.after(1000, self.update_view)

controller = Controller()
model = controller.model
view = controller.view

model.game.set_board()

# Bacel patuhany (shog a)
view.window.bind('<Left>', model.game.left_arrow)
view.window.bind('<Left>', controller.update_view, add='+')

view.window.bind('<Right>', model.game.right_arrow)
view.window.bind('<Right>', controller.update_view, add='+')

view.window.bind('<Up>', model.game.up_arrow)
view.window.bind('<Up>', controller.update_view, add='+')

view.window.bind('<Down>', model.game.down_arrow)
view.window.bind('<Down>', controller.update_view, add='+')

view.window.mainloop()
model.game.show_model()


# # Console App
# while model.game.is_won is False:
# 	move = input("Qayl:")
# 	print("Making move...")
# 	model.game.make_move(move) # stack enq anum
# 	model.game.check_finish()
# 	print('Adding a num...')
# 	model.game.add_num()
# 	print("New matrix:")
# 	model.game.show_model()
# 	print()