import tkinter as tk
from config import colors
import model as m
import view as v
# import numpy as np

GRID_SIZE = 4

class Controller():
    def __init__(self):
        self.model = m.Model(GRID_SIZE)
        self.view = v.View()

        self.model.game.show_model()

        spacing = 20
        # self.cells = np.empty((GRID_SIZE, GRID_SIZE), dtype=dict)
        self.cells = [[{} for i in range(GRID_SIZE)] for k in range(GRID_SIZE)]

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                frame_cell = tk.Frame(self.view.game_canvas,
                    bg=colors[self.model.game.board[i][j]],
                    width=(600-2*spacing-(GRID_SIZE+1)*spacing)/GRID_SIZE,
                    height=(600-2*spacing-(GRID_SIZE+1)*spacing)/GRID_SIZE)

                frame_cell.grid(row=i, column=j, padx=spacing/2, pady=spacing/2)

                cell_number = tk.Label(self.view.game_canvas,
                    bg=colors[self.model.game.board[i][j]],
                    fg='white',
                    text=str(self.model.game.board[i][j]),
                    font=('Arial 40'))
                cell_data = { "frame": frame_cell, "number": cell_number }

                cell_number.grid(row=i, column=j)
                self.cells[i][j] = cell_data

    def update_view(self, _):
        self.view.score_label["text"] = "Score: " + str(self.model.game.score)

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.cells[i][j]["frame"]["bg"] = colors[self.model.game.board[i][j]]
                self.cells[i][j]["number"]["bg"] = colors[self.model.game.board[i][j]]
                self.cells[i][j]["number"]["text"] = str(self.model.game.board[i][j])

        if self.model.game.is_finished:
            self.finish_game()

        if self.model.game.is_won:
            self.win_game()

        # self.view.window.after(1000, self.update_view)

    def finish_game(self):
        self.view.finish_label["text"] = "Game Over"
        self.view.finish_label.pack(side=tk.RIGHT, padx=25)

        self.view.new_game_button = tk.Button(self.view.window,
            width=11,
            height=2,
            text="Start Again",
            bg='#121212',
            font=('Arial 25'),
            highlightbackground='#121212',
            command=new_game)
        self.view.new_game_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.view.window.unbind('<Left>')
        self.view.window.unbind('<Right>')
        self.view.window.unbind('<Up>')
        self.view.window.unbind('<Down>')

    def win_game(self):
        self.view.finish_label["text"] = "You Won!"
        self.view.finish_label.pack(side = tk.RIGHT, padx=25)


def new_game():
    controller.model.game.is_finished = False
    controller.model.game.is_won = False
    controller.model.game.score = 0
    view.finish_label.pack_forget()
    view.new_game_button.place_forget()
    controller.model.game.set_board()

    view.window.bind('<Left>', model.game.left_arrow)
    view.window.bind('<Left>', controller.update_view, add='+')

    view.window.bind('<Right>', model.game.right_arrow)
    view.window.bind('<Right>', controller.update_view, add='+')

    view.window.bind('<Up>', model.game.up_arrow)
    view.window.bind('<Up>', controller.update_view, add='+')

    view.window.bind('<Down>', model.game.down_arrow)
    view.window.bind('<Down>', controller.update_view, add='+')

    controller.update_view('l')

controller = Controller()
model = controller.model
view = controller.view

# model.game.set_board()

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
# model.game.show_model()
