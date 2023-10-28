import tkinter as tk


class View:

    def __init__(self, count):
        self.window = tk.Tk()
        self.window.title("sample")
        self.window.geometry("750x500")


        self.width = 500
        self.height = 500

        self.count = count

        self.cell_width = int(self.width / self.count)

    def create_grid(self):
        
        canvas = tk.Canvas(self.window, background = "white", width = self.width, height = self.height)

        for line in range(0, self.width, int(self.cell_width)):
            canvas.create_line((line, 0), (line, self.height) , fill = "black", tags = "")
            canvas.create_line((0, line), (self.width, line), fill = "black", tag = "")
        
        canvas.grid(row = 0, column = 0)

    def create_squares(self):
        pass

    def update(self):
        print('updated')
        self.create_grid()