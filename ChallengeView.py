import SimulationView
import tkinter as tk

class ChallengeView(SimulationView.SimulationView):


    def __init__(self, controller, count):
        super().essential_gui(controller, count)
        

        scroll = tk.Scrollbar(self.window)
        self.red_score = tk.Label(self.window, font = self.font, text = "0", fg = "red")
        self.blue_score = tk.Label(self.window, text = "0", fg = "blue")

        scroll.place(x = 555, y = 400)
        self.red_score.place(x = 545, y = 100)
        self.blue_score.place(x = 560, y = 100)



    def update_score(self):
        controller = self.controller
        self.red_score.config(text = str(controller.opponent_points))
        self.blue_score.config(text = str(controller.player_points))





        

    
