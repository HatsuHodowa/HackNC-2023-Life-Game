import tkinter as tk
import SimulationController
import ChallengeController

class MainMenu:

    def __init__(self):

        # main properties
        self.current_controller = None

        # creating window
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Quantum Life Battles")
        self.window.geometry("750x500")
        big_font = ('Helvetica', 50, 'bold')
        mid_font = ('Helvetica', 30, 'bold')

        title = tk.Label(self.window, text = "Quantum Life Battles", font = big_font)
        sandbox = tk.Button(self.window, text = "Sandbox Mode", font = mid_font, command = self.to_simulation)
        challenge = tk.Button(self.window, text = "Challenge Mode", font = mid_font, command = self.to_challenge)

        title.place(anchor= "center", relx = 0.5, rely = 0.3)
        sandbox.place(anchor = "center", relx = 0.5, rely = 0.5)
        challenge.place(anchor = "center", relx = 0.5, rely = 0.65)
        
        # mainloop
        self.window.mainloop()

    def open_menu(self):
        pass

    def close_menu(self):
        pass

    def to_simulation(self):
        self.close_menu()
        self.current_controller = SimulationController.SimulationController(self)

    def to_challenge(self):
        self.close_menu()
        self.current_controller = ChallengeController.ChallengeController(self)
    
x = MainMenu()