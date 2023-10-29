import SimulationView
import tkinter as tk
from tkinter import filedialog


class ChallengeView(SimulationView.SimulationView):


    def __init__(self, controller, count):
        """Entrypoint to child function."""
        super().essential_gui(controller, count)
        
        self.window.title("Quame of Life: Challenges")
        self.canvas.configure(background = "grey")
        self.font = ("Helvetica", 30, "bold")
        self.red_score = tk.Label(self.window, font = self.font, text = "0.0", fg = "red", bg = "white")
        self.blue_score = tk.Label(self.window, font = self.font, text = "0.0", fg = "blue", bg = "white")
        self.free_boxes = tk.Label(self.window, font = ("Helvetica", 13, "bold"), text = f"Placeable Boxes: None")
        self.load_level.config(text = "Load Level")
        self.win = tk.Label(self.window, font = self.font)

        self.red_score.place(x = 560, y = 150)
        self.blue_score.place(x = 640, y = 150)
        self.free_boxes.place(x = 555, y = 390)



    def update_score(self):
        """Updates the scores of the user and the opponent."""
        controller = self.controller
        self.red_score.config(text = str(round(controller.opponent_points, 2)))
        self.blue_score.config(text = str(round(controller.player_points, 2)))

    def upload_file(self):
        """Allows the player to upload level to game."""
        self.win.place_forget()
        super().upload_file()
        self.update_max_boxes()

    def update_max_boxes(self):
        """Updates the amount of free boxes the user can place."""
        if self.controller.model.om.cell_limit != None:
            cells_left = self.controller.model.om.cell_limit - self.controller.current_blocks
            self.free_boxes.config(text = f"Placeable Boxes: {str(cells_left)}")


    def player_win(self):
        """Displays label text when user wins."""
        self.win.config(text = "You win!")
        self.win.place(anchor = "center", relx = 0.5, rely = 0.5)


    def opponent_win(self):
        """Displays label text when user loses."""
        self.win.config(text = "You lost!")
        self.win.place(anchor = "center", relx = 0.5, rely = 0.5)



        

    
