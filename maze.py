from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate (self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
                self._win.redraw()
                self._win.canvas.after(50)
                self._win.canvas.update()


    def _break_entrance_and_exit(self):
        """
        Creates an entrance at the top-left cell (0,0) and an exit at the bottom-right cell
        by removing outer walls from these cells. For the entrance, the top wall is removed,
        and for the exit, the bottom wall is removed.
        """
        # Break the top wall of the entrance (top-left cell)
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        
        # Break the bottom wall of the exit (bottom-right cell)
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        
        # Redraw the cells to show the changes
        if self._win is not None:
            self._draw_cell(0, 0)  # Redraw entrance
            self._draw_cell(self._num_cols - 1, self._num_rows - 1)  # Redraw exit