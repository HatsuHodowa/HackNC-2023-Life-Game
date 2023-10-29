import tkinter as tk
import SimulationView, Model
import SimulationController

class MainMenu:

    def __init__(self):

        # main properties
        self.current_controller = None

        # opening menu to start
        self.open_menu()
        
        # mainloop
        self.window.mainloop()

    def open_menu(self):

        # creating window
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Quantum Life Battles")
        self.window.geometry("750x500")
        big_font = ('Helvetica', 50, 'bold')
        mid_font = ('Helvetica', 30, 'bold')

        title = tk.Label(self.window, text = "Quantum Life Battles", font = big_font)
        sandbox = tk.Button(self.window, text = "Sandbox Mode", font = mid_font, command = self.to_simulation)
        challenge = tk.Button(self.window, text = "Challenge Mode", font = mid_font)

        title.place(anchor= "center", relx = 0.5, rely = 0.3)
        sandbox.place(anchor = "center", relx = 0.5, rely = 0.5)
        challenge.place(anchor = "center", relx = 0.5, rely = 0.65)

    def close_menu(self):
        self.window.destroy()
    
    def to_simulation(self):
        #self.window.destroy()
        self.current_controller = SimulationController.SimulationController(self)
    
x = MainMenu()