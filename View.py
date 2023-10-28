import tkinter as tk
import Model
from tkinter import filedialog

def rgb_convert(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


class View:



    def __init__(self, controller, count):


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
        self.grid_count.set(self.controller.cell_count)
        self.slider = tk.Scale(self.window, from_ = 1, to = 100, command = self.change_framerate, orient = "horizontal")

        start = tk.Button(self.window, text = "Start Simulation", font = font, height = 1, width = 15, command = self.started)
        stop = tk.Button(self.window, text = "Stop Simulation", font = font, height = 1, width = 15, command = self.stopped)
        reset = tk.Button(self.window, text = "Clear Grid", font = font, height = 1, width = 15, command = self.resetted)
        input_file = tk.Button(self.window, text = "Input Configuration", font = font, height = 1, width = 15, command = self.upload_file)
        save_config = tk.Button(self.window, text = "Save Configuration", font = font, height = 1, width = 15, command = self.controller.saveConfiguration)

    
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

        self.width = 500
        self.height = 500

        self.count = count
        self.squares = []
        self.cell_width = int(self.width / self.count)
        self.canvas = tk.Canvas(self.window, background = "white", width = self.width, height = self.height)

    def update_cell_count(self, count):
        self.count = count
        self.cell_width = int(self.width / self.count)
        

    def cell_adjust(self, event):
        self.controller.updateCellCount(self.grid_count.get())
    
    def resetted(self):
        self.controller.clearCells()
        self.controller.stop()
        self.status.config(text = "Status: Stopped")

    def started(self):
        self.controller.start()
        self.status.config(text = "Status: Running")
    
    def stopped(self):
        self.controller.stop()
        self.status.config(text = "Status: Stopped")

    def upload_file(self):
        self.controller.loadConfiguration(self.controller.model.om, filedialog.askopenfilename(initialdir="/SaveData"))

    def change_framerate(self, event):
        self.controller.framerate = self.slider.get()

    def on_square_click(self, event):
        x = int(event.x / self.cell_width)
        y = int(event.y / self.cell_width)
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

                red = int(255 * opponent_value)
                green = 0
                blue = int(255 * value)
                square = self.canvas.create_rectangle(x_position, y_position, x_position + self.cell_width, y_position + self.cell_width, fill = rgb_convert(red, green, blue))
                self.squares.append(square)

                self.canvas.tag_bind(square, '<Button-1>', self.on_square_click) 
        
                
                    

    def create_grid(self):
        """Creates grids within the UI"""
        

        for line in range(0, self.width, int(self.cell_width)):
            a= self.canvas.create_line((line, 0), (line, self.height) , fill = "grey", tags = "")
            b = self.canvas.create_line((0, line), (self.width, line), fill = "grey", tag = "")
            self.squares.append(a)
            self.squares.append(b)
        self.canvas.grid(row = 0, column = 0)


    def update(self):

        self.create_squares()
        self.create_grid()