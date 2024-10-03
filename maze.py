import time
from tkinter import Tk, BOTH, Canvas
from ui import Cell
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self.win = win
        if seed != None:
            self.seed = random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        print("Creating Paths")
        self.break_walls_r(0, 0)
        print("Maze Drawn")
        self.reset_cells_visited()

    def create_cells(self):
        print("Creating Cells")
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

    def break_entrance_and_exit(self):
        print("Creating Entrance and Exit")
        first_cell = self.cells[0][0]
        last_cell = self.cells[self.num_cols-1][self.num_rows-1]
        first_cell.top_wall = False
        self.draw_cell(0, 0)
        last_cell.bot_wall = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)

    def break_walls_r(self, i, j):
        current_cell = self.cells[i][j]
        current_cell.visited = True
        new_i = i
        new_j = j
        while True:
            cells_choices = []

            if i > 0:
                top_cell = self.cells[i-1][j]
                if not top_cell.visited:
                    cells_choices.append(top_cell)
            if i < self.num_cols - 1:
                bot_cell = self.cells[i+1][j]
                if not bot_cell.visited:
                    cells_choices.append(bot_cell)

            if j > 0:
                left_cell = self.cells[i][j-1]
                if not left_cell.visited:
                    cells_choices.append(left_cell)
            if j < self.num_rows - 1:
                right_cell = self.cells[i][j+1]
                if not right_cell.visited:
                    cells_choices.append(right_cell)

            routes = len(cells_choices)
            if routes == 0:
                self.draw_cell(i, j)
                return
            path = random.randrange(routes)
            new_cell = cells_choices[path-1]

            if new_cell.x1 > current_cell.x1:
                current_cell.right_wall = False
                new_cell.left_wall = False
                new_i = i + 1
            if new_cell.x1 < current_cell.x1:
                current_cell.left_wall = False
                new_cell.right_wall = False
                new_i = i - 1

            if new_cell.y1 > current_cell.y1:
                current_cell.bot_wall = False
                new_cell.top_wall = False
                new_j = j + 1
            if new_cell.y1 < current_cell.y1:
                current_cell.top_wall = False
                new_cell.bot_wall = False
                new_j = j - 1

            self.draw_cell(i, j)
            self.break_walls_r(new_i, new_j)

    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i , j):
        self.animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        possible_paths = []
        
        if i > 0 and not current_cell.top_wall and not self.cells[i][j-1].visited:
            possible_paths.append((i, j-1))
        if i < self.num_cols and not current_cell.bot_wall and not self.cells[i][j+1].visited:
            possible_paths.append((i, j+1))

        if j > 0 and not current_cell.left_wall and not self.cells[i-1][j].visited:
            possible_paths.append((i-1, j))
        if j < self.num_rows and not current_cell.right_wall and not self.cells[i+1][j].visited:
            possible_paths.append((i+1, j))
        
        for path in possible_paths:
            current_cell.draw_move(self.cells[path[0]][path[1]])
            if self.solve_r(path[0], path[1]):
                return True
            else:
                current_cell.draw_move(self.cells[path[0]][path[1]], True)

        return False


