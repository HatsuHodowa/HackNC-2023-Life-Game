import tkinter as tk
import View, Model


class MainMenu:

    def __init__(self):
        

        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Quantum Life Battles")
        self.window.geometry("750x500")
        big_font = ('Helvetica', 50, 'bold')
        mid_font = ('Helvetica', 30, 'bold')

        title = tk.Label(self.window, text = "Quantum Life Battles", font = big_font)
        sandbox = tk.Button(self.window, text = "Sandbox Mode", font = mid_font, command = self.to_controller)
        challenge = tk.Button(self.window, text = "Challenge Mode", font = mid_font)


        title.place(anchor= "center", relx = 0.5, rely = 0.3)
        sandbox.place(anchor = "center", relx = 0.5, rely = 0.5)
        challenge.place(anchor = "center", relx = 0.5, rely = 0.65)

        self.window.mainloop()
    
    def to_controller(self):
        self.window.destroy()
        import Controller
    
x = MainMenu()