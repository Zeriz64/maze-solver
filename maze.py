import time
from tkinter import Tk, BOTH, Canvas
from ui import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self.win = win

        self.create_cells()

    def create_cells(self):
        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                self.cells[i].append(Cell(self.win))
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        if self.win is None:
            return
        x = (i * self.cell_size_x) + self.x1
        y = (j * self.cell_size_y) + self.y1
        cell = self.cells[i][j]
        cell.draw(x, y, x+self.cell_size_x, y+self.cell_size_y)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.01)
