from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2,win):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),'black')
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),'black')
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),'black')
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),'black')

    def draw_move(self, to_cell, undo = False):
        #Draw red line from center of this cell to center of to_cell
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2
        if undo:
            self._win.draw_line(Line(Point(x1,y1),Point(x2,y2)),'grey')
        else:
            self._win.draw_line(Line(Point(x1,y1),Point(x2,y2)),'red')