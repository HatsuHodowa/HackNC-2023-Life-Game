import SimulationView
import tkinter as tk
from tkinter import filedialog

class ChallengeView(SimulationView.SimulationView):


    def __init__(self, controller, count):
        super().essential_gui(controller, count)
        
        self.window.title("Game of Life Challenges")
        self.canvas.configure(background = "grey")
        self.font = ("Helvetica", 30, "bold")
        self.red_score = tk.Label(self.window, font = self.font, text = "0.0", fg = "red", bg = "white")
        self.blue_score = tk.Label(self.window, font = self.font, text = "0.0", fg = "blue", bg = "white")
        self.free_boxes = tk.Label(self.window, font = ("Helvetica", 13, "bold"), text = f"Placeable Boxes: None")
        self.load_level.config(text = "Load Level")

        self.red_score.place(x = 560, y = 150)
        self.blue_score.place(x = 640, y = 150)
        self.free_boxes.place(relx = 0.67, rely = 0.82)



    def update_score(self):
        controller = self.controller
        self.red_score.config(text = str(controller.opponent_points))
        self.blue_score.config(text = str(controller.player_points))

    def upload_file(self):
        super().resetted()
        super().upload_file()
        self.update_max_boxes()

    def update_max_boxes(self):
        if self.controller.model.om.cell_limit != None:
            cells_left = self.controller.model.om.cell_limit - self.controller.current_blocks
            self.free_boxes.config(text = f"Placeable Boxes: {str(cells_left)}")



        

    
