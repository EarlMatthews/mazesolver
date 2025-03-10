from tkinter import Tk, Canvas
import random
from point import Point
from line import Line
from cell import Cell

class Window:
    def __init__(self,title="My Application", width=400, height=500):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root)
        self.canvas.pack(expand=True, fill='both')
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        #self.update()

    def wait_for_close(self):
        self.running = True
        self.__root.mainloop()
    
    def close(self):
        self.running = False
        self.__root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas,fill_color)

def generate_random_lines(num_lines):
    lines = []
    for i in range(num_lines):
        start = Point(random.randint(0, 800), random.randint(0, 600))
        end = Point(random.randint(0, 800), random.randint(0, 600))
        lines.append(Line(start, end))
    return lines    

def generate_random_cells(num_cells,win):
    cells = []
    for i in range(num_cells):
        x1 = random.randint(0, 800)
        x2 = random.randint(0, 800)
        y1 = random.randint(0, 600)
        y2 = random.randint(0, 600)
        cells.append(Cell(x1,y1,x2,y2,win))
    return cells

def main():
    win = Window("My Application",800,600)
     # Create points and a line
    for cell in generate_random_cells(10,win):
        cell.draw()
    
    win.wait_for_close()
    
if __name__ == "__main__":
    main()