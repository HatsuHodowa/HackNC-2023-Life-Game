import SimulationView
import tkinter as tk
from tkinter import filedialog

class ChallengeView(SimulationView.SimulationView):


    def __init__(self, controller, count):
        super().essential_gui(controller, count)
        
        self.canvas.configure(background = "grey")
        scroll = tk.Scrollbar(self.window, orient = "vertical")
        self.font = ("Helvetica", 30, "bold")
        self.red_score = tk.Label(self.window, font = self.font, text = "0.0", fg = "red", bg = "white")
        self.blue_score = tk.Label(self.window, font = self.font, text = "0.0", fg = "blue", bg = "white")
        self.free_boxes = tk.Label(self.window, font = self.font, text = str(self.controller.current_blocks))
        self.load_level.config(text = "Load Level")


        scroll.place(x = 555, y = 400)
        self.red_score.place(x = 570, y = 150)
        self.blue_score.place(x = 630, y = 150)
        self.free_boxes.place(x = 700, y = 200)



    def update_score(self):
        controller = self.controller
        self.red_score.config(text = str(controller.opponent_points))
        self.blue_score.config(text = str(controller.player_points))





        

    
