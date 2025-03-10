from tkinter import Tk, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y,fill=fill_color,width=2)

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


def main():
    win = Window("My Application",800,600)
    win.wait_for_close()

     # Create points and a line
    start = Point(100, 100)
    end = Point(300, 300)
    line = Line(start, end)

    win.draw_line(line,'red')

if __name__ == "__main__":
    main()