import SimulationView
import tkinter as tk

class ChallengeView(SimulationView.SimulationView):


    def __init__(self, controller, count):
        super().essential_gui(controller, count)
        self.slider.config(y = 100)


        scroll = tk.Scrollbar(self.window)

        scroll.place(x = 555, y = 400)





        

    
