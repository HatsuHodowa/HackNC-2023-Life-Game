import tkinter as tk
import SimulationController
import ChallengeController
import tkvideo as video
import os

class MainMenu:

    def __init__(self):
        """Entry function to the class."""

        # main properties
        self.current_controller = None
        self.current_size = 15

        # creating window
        self.window = tk.Tk()
        self.window.configure(background = "gray")
        self.window.resizable(False, False)
        self.window.title("Quame of Life")
        self.window.geometry("750x500")

        # creates video
        video_label = tk.Label(self.window, bg = "gray")
        video_label.pack()
        video_player = video.tkvideo("menu_video.mp4", video_label, loop = 1, size = (750, 750))
        video_player.play()

        # creating interface
        big_font = ('Helvetica', 50, 'bold')
        mid_font = ('Helvetica', 30, 'bold')
        small_font = ('Helvetic', 15)
        title = tk.Label(self.window, text = "Quame of Life", font = big_font, fg = "white", bg = "#2a2a2a")
        sandbox = tk.Button(self.window, text = "Sandbox Mode", font = mid_font, command = self.to_simulation, fg = "gray", bg = "#191919")
        challenge = tk.Button(self.window, text = "Challenge Mode", font = mid_font, command = self.to_challenge, fg = "gray", bg = "#191919")
        size_label = tk.Label(self.window, text = "Grid Size", font = small_font, fg = "white", bg = "#2a2a2a")
        self.size_scale = tk.Scale(self.window, from_ = 5, to = 50, command = self.configure_size, orient = "horizontal", length = 200, bg = "#191919", font = small_font, fg = "white", troughcolor="gray")
        self.size_scale.set(15)

        title.place(anchor= "center", relx = 0.5, y = 100)
        sandbox.place(anchor = "center", relx = 0.5, y = 200)
        challenge.place(anchor = "center", relx = 0.5, y = 300)
        size_label.place(anchor = "center", relx = 0.5, y = 370)
        self.size_scale.place(anchor = "center", relx = 0.5, y = 420)
        
        # mainloop
        self.window.mainloop()

    def open_menu(self):
        """Opens the ui portal for the menu."""
        self.window.wm_state("normal")

    def close_menu(self):
        """Minimizes the ui portal for the menu."""
        self.window.wm_state("iconic")

    def configure_size(self, event):
        self.current_size = self.size_scale.get()

    def to_simulation(self):
        """Opens an instance of the simulation mode of the game."""
        self.close_menu()
        self.current_controller = SimulationController.SimulationController(self)

    def to_challenge(self):
        """Opens an instance of the challenge mode of the game."""
        self.close_menu()
        self.current_controller = ChallengeController.ChallengeController(self)
    
x = MainMenu()