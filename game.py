import tkinter as tk
from config import colors
import model as m
import view as v
# import numpy as np

# GRID_SIZE = 4

class Controller():
    def __init__(self):
        self.view = v.View()

        self.view.new_game_button = tk.Button(self.view.window,
            width=10,
            height=2,
            text="Start",
            bg='#121212',
            font=('Arial 25'),
            highlightbackground='#121212',
            command=lambda: self.start(int(self.view.current_value.get())))
        self.view.new_game_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.view.window.mainloop()

    def start(self, GRID_SIZE):
        self.view.spin_box.pack_forget()
        self.view.start_game()
        self.model = m.Model(GRID_SIZE)

        self.model.game.show_model()

        spacing = 20
        # self.cells = np.empty((GRID_SIZE, GRID_SIZE), dtype=dict)
        self.cells = [[{} for i in range(GRID_SIZE)] for k in range(GRID_SIZE)]

        for i in range(self.model.game.grid):
            for j in range(self.model.game.grid):
                frame_cell = tk.Frame(self.view.game_canvas,
                    bg=colors[self.model.game.board[i][j]],
                    width=(600-2*spacing-(self.model.game.grid+1)*spacing)/self.model.game.grid,
                    height=(600-2*spacing-(self.model.game.grid+1)*spacing)/self.model.game.grid)

                frame_cell.grid(row=i, column=j, padx=spacing/2, pady=spacing/2)

                cell_number = tk.Label(self.view.game_canvas,
                    bg=colors[self.model.game.board[i][j]],
                    fg='white',
                    text=str(self.model.game.board[i][j]),
                    font=('Arial 40'))
                cell_data = { "frame": frame_cell, "number": cell_number }

                cell_number.grid(row=i, column=j)
                self.cells[i][j] = cell_data

        # model.game.set_board()

        # Bacel patuhany (shog a)
        self.view.window.bind('<Left>', self.model.game.left_arrow)
        self.view.window.bind('<Left>', self.update_view, add='+')

        self.view.window.bind('<Right>', self.model.game.right_arrow)
        self.view.window.bind('<Right>', self.update_view, add='+')

        self.view.window.bind('<Up>', self.model.game.up_arrow)
        self.view.window.bind('<Up>', self.update_view, add='+')

        self.view.window.bind('<Down>', self.model.game.down_arrow)
        self.view.window.bind('<Down>', self.update_view, add='+')

    def update_view(self, _):
        self.view.score_label["text"] = "Score: " + str(self.model.game.score)

        for i in range(self.model.game.grid):
            for j in range(self.model.game.grid):
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
            command=self.new_game)
        self.view.new_game_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.view.window.unbind('<Left>')
        self.view.window.unbind('<Right>')
        self.view.window.unbind('<Up>')
        self.view.window.unbind('<Down>')

    def win_game(self):
        self.view.finish_label["text"] = "You Won!"
        self.view.finish_label.pack(side = tk.RIGHT, padx=25)


    def new_game(self):
        self.model.game.is_finished = False
        self.model.game.is_won = False
        self.model.game.score = 0
        self.view.finish_label.pack_forget()
        self.view.new_game_button.place_forget()
        self.model.game.set_board()

        self.view.window.bind('<Left>', self.model.game.left_arrow)
        self.view.window.bind('<Left>', self.update_view, add='+')

        self.view.window.bind('<Right>', self.model.game.right_arrow)
        self.view.window.bind('<Right>', self.update_view, add='+')

        self.view.window.bind('<Up>', self.model.game.up_arrow)
        self.view.window.bind('<Up>', self.update_view, add='+')

        self.view.window.bind('<Down>', self.model.game.down_arrow)
        self.view.window.bind('<Down>', self.update_view, add='+')

        self.update_view('l')

controller = Controller()