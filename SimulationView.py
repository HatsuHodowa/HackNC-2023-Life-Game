import tkinter as tk
import Model
from tkinter import filedialog


def rgb_convert(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


class SimulationView:


    def __init__(self, controller, count):
        """Main function of this class."""
        self.controller = controller

        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Quantum Life Battles")
        self.window.geometry("750x500")

        font = ('Helvetica', 14, "bold")

        self.status = tk.Label(self.window, text = "Status: Stopped", font = font)
        speedlabel = tk.Label(self.window, text = "Speed Slider", font = font)
        zoomlabel = tk.Label(self.window, text = "Zoom Slider", font = font)
        
        self.grid_count = tk.Scale(self.window, from_ = 1, to = self.controller.cell_count, command = self.cell_adjust, orient = "horizontal")
        self.slider = tk.Scale(self.window, from_ = 1, to = 100, command = self.change_framerate, orient = "horizontal")

        start = tk.Button(self.window, text = "Start Simulation", font = font, height = 1, width = 15, command = self.started)
        stop = tk.Button(self.window, text = "Stop Simulation", font = font, height = 1, width = 15, command = self.stopped)
        reset = tk.Button(self.window, text = "Clear Grid", font = font, height = 1, width = 15, command = self.resetted)
        input_file = tk.Button(self.window, text = "Input Configuration", font = font, height = 1, width = 15, command = self.upload_file)
        save_config = tk.Button(self.window, text = "Save Configuration", font = font, height = 1, width = 15, command = self.controller.saveConfiguration)
        back_button = tk.Button(self.window, text = "Back", font = font, height = 1, width = 15, command = self.back_to_menu)

    
        self.status.place(x = 575, y = 10)
        start.place(x = 555, y = 50)
        stop.place(x = 555, y = 110)
        reset.place(x = 555, y = 170)
        self.slider.place(x = 570, y = 240)
        speedlabel.place(x = 575, y = 220)
        zoomlabel.place(x = 575, y = 280)
        save_config.place(x = 555, y = 420)
        input_file.place(x = 555, y = 370)
        self.grid_count.place(x = 570, y = 300)
        back_button.place(anchor = "center", x = 630, rely = 0.95)

        self.width = 500
        self.height = 500

        self.count = count
        self.squares = []
        self.cell_width = int(self.width / self.count)
        self.canvas = tk.Canvas(self.window, background = "white", width = self.width, height = self.height)
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)

    def back_to_menu(self):
        self.window.destroy()
        self.controller.menu.open_menu()

    def scroll_start(self, event):
        """Starts the panning movement by taking in initial x and y coordinates."""
        self.canvas.scan_mark(event.x, event.y)


    def scroll_move(self, event):
        """Allows the user to drag and pan across the grid canvas."""
        self.canvas.scan_dragto(event.x, event.y, gain = 1)


    def update_cell_count(self, count):
        """Continuosly updates cell count when zoom slider is utilized."""
        self.count = self.controller.cell_count - count
        self.cell_width = int(self.width / self.count)
    

    def cell_adjust(self, event):
        """Changes the amount of cells are present within the UI."""
        self.controller.updateCellCount(self.grid_count.get() - 1)
    

    def resetted(self):
        """Resets the grid."""
        self.controller.clearCells()
        self.controller.stop()
        self.status.config(text = "Status: Stopped")


    def started(self):
        """Starts the grid."""
        self.controller.start()
        self.status.config(text = "Status: Running")
    

    def stopped(self):
        """Stops the grid."""
        self.controller.stop()
        self.status.config(text = "Status: Stopped")


    def upload_file(self):
        """Allows the user to upload level presets to the grid."""
        self.controller.loadConfiguration(self.controller.model.om, filedialog.askopenfilename(initialdir="/SaveData"))


    def change_framerate(self, event):
        """Changes the speed of the models."""
        self.controller.framerate = self.slider.get()


    def on_square_click(self, event):
        """Inverts the grid box selected by the user."""
        x = int(self.canvas.canvasx(event.x) / self.cell_width)
        y = int(self.canvas.canvasy(event.y) / self.cell_width)
        value = self.controller.model.getCellP(y, x)
        self.controller.model.setCellP(y, x, 1 - value)


    def create_squares(self):
        """Generates squares within cells."""
        for k in self.squares:
            self.canvas.delete(k)
        self.squares = []

        for y, cells in enumerate(self.controller.model.pm.li): 
            for x, value in enumerate(cells):
                x_position = self.cell_width * x
                y_position = self.cell_width * y

                opponent_value = self.controller.model.getCellO(y, x)

                red = int(50+205 * opponent_value)
                if opponent_value == 0:
                    red = 0
                green = 0
                blue = int(50+205 * value)
                if value == 0:
                    blue = 0
                square = self.canvas.create_rectangle(x_position, y_position, x_position + self.cell_width, y_position + self.cell_width, fill = rgb_convert(red, green, blue))
                self.squares.append(square)

                self.canvas.tag_bind(square, '<Button-1>', self.on_square_click) 
        
                
    def create_grid(self):
        """Creates grids within the UI"""
        line_length = self.controller.cell_count * self.cell_width
        for line in range(0, self.width, int(self.cell_width)):
            a= self.canvas.create_line((line, 0), (line, line_length) , fill = "grey", tags = "")
            b = self.canvas.create_line((0, line), (line_length, line), fill = "grey", tag = "")
            self.squares.append(a)
            self.squares.append(b)
        self.canvas.grid(row = 0, column = 0)


    def update(self):
        """Updates the class."""
        self.create_squares()
        self.create_grid()