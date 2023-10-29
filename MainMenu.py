import tkinter as tk
import SimulationController
import ChallengeController
import tkvideo as video
import os

class MainMenu:

    def __init__(self):

        # main properties
        self.current_controller = None

        # creating window
        self.window = tk.Tk()
        self.window.configure(background = "gray")
        self.window.resizable(False, False)
        self.window.title("Quame of Life")
        self.window.geometry("750x500")

        # creates video
        video_label = tk.Label(self.window, bg = "gray")
        video_label.pack()
        curr_path = os.path.dirname(__file__)
        video_path = curr_path + "\\Assets\\menu_video.mp4"
        video_player = video.tkvideo(video_path, video_label, loop = 1, size = (750, 750))
        video_player.play()

        # creating interface
        big_font = ('Helvetica', 50, 'bold')
        mid_font = ('Helvetica', 30, 'bold')
        title = tk.Label(self.window, text = "Quame of Life", font = big_font, fg = "white", bg = "#2a2a2a")
        sandbox = tk.Button(self.window, text = "Sandbox Mode", font = mid_font, command = self.to_simulation)
        challenge = tk.Button(self.window, text = "Challenge Mode", font = mid_font, command = self.to_challenge)

        title.place(anchor= "center", relx = 0.5, rely = 0.3)
        sandbox.place(anchor = "center", relx = 0.5, rely = 0.5)
        challenge.place(anchor = "center", relx = 0.5, rely = 0.65)
        
        # mainloop
        self.window.mainloop()

    def open_menu(self):
        self.window.wm_state("normal")

    def close_menu(self):
        self.window.wm_state("iconic")

    def to_simulation(self):
        self.close_menu()
        self.current_controller = SimulationController.SimulationController(self)

    def to_challenge(self):
        self.close_menu()
        self.current_controller = ChallengeController.ChallengeController(self)
    
x = MainMenu()