import tkinter as tk

class View():
    def __init__(self):
        self.start_window()
        self.current_value = tk.StringVar()
        self.spin_box = tk.Spinbox(
            self.window,
            from_=0,
            to=50,
            values=(tuple(range(4,16))),
            textvariable=self.current_value,
            wrap=True)
        self.spin_box.pack()

    def start_game(self):
        self.new_game_button.place_forget()
        self.main_canvas = self.set_main_canvas()
        self.game_canvas = self.set_game_canvas()

    def start_window(self):
        self.window = tk.Tk()
        self.window.title("Qsan Qarut")
        self.window.geometry('600x665')
        self.window.resizable(False, False)
        self.window.configure(bg='#121212')
        self.score_label = tk.Label()
        self.finish_label = tk.Label(self.window,
            text="Game Over",
            font=('Arial 35'),
            fg='white',
            bg='#121212')
        self.new_game_button = tk.Button()

    def set_main_canvas(self):
        canvas = tk.Canvas(self.window,
            width=600,
            height=650,
            background="#121212",
            highlightthickness=0)
        canvas.pack()

        self.score_label = tk.Label(self.window,
            text="Score: 0",
            font=('Arial 35'),
            fg='white',
            bg='#121212')
        self.score_label.pack(side = tk.LEFT, padx=25)

        return canvas

    def set_game_canvas(self):
        window_width = 600
        window_height = 650
        window_spacing = 25
        bar_height = 65

        canvas_width = window_width  - window_spacing*2
        canvas_height = window_height - bar_height - window_spacing*2

        canvas = tk.Canvas(self.main_canvas,
            width=canvas_width,
            height=canvas_height,
            background="#232323")
        canvas.pack(padx=25, pady=25)
        return canvas
