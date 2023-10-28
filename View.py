import tkinter as tk
import Model

def rgb_convert(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


class View:



    def __init__(self, controller, count):


        self.controller = controller


        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("sample")
        self.window.geometry("750x500")

        font = ('Helvetica', 14, "bold")

        title = tk.Label(self.window, text = "")
        start = tk.Button(self.window, text = "Start Simulation", font = font, height = 3, width = 15, command = self.controller.start)
        stop = tk.Button(self.window, text = "Stop Simulation", font = font, height = 3, width = 15, command = self.controller.stop)
        reset = tk.Button(self.window, text = "Clear Grid", font = font, height = 3, width = 15, command = self.controller.clearCells)
    

        start.place(x = 555, y = 50)
        stop.place(x = 555, y = 110)
        reset.place(x = 555, y = 170)

        self.width = 500
        self.height = 500

        self.count = count
        self.squares = []
        self.cell_width = int(self.width / self.count)
        self.canvas = tk.Canvas(self.window, background = "white", width = self.width, height = self.height)



    def create_squares(self):
        """Generates squares within cells."""
        for k in self.squares:
            self.canvas.delete(k)
        self.squares = []

        for y, cells in enumerate(self.controller.model.li): 
            for x, value in enumerate(cells):
                x_position = self.cell_width * x
                y_position = self.cell_width * y
                red = int(255 * value)
                green = int(255 * value)
                blue = int(255 * value)
                square = self.canvas.create_rectangle(x_position, y_position, x_position + self.cell_width, y_position + self.cell_width, fill = rgb_convert(red, green, blue))
                self.squares.append(square)

                def on_mouse_click(event):
                    print(x, y)
                    self.controller.setCell(x, y, 1 - value)

                self.canvas.tag_bind(square, '<Button-1>', on_mouse_click) 
        
                
                    

    def create_grid(self):
        """Creates grids within the UI"""
        

        for line in range(0, self.width, int(self.cell_width)):
            self.canvas.create_line((line, 0), (line, self.height) , fill = "grey", tags = "")
            self.canvas.create_line((0, line), (self.width, line), fill = "grey", tag = "")
        
        self.canvas.grid(row = 0, column = 0)


    def update(self):

        self.create_squares()
        self.create_grid()