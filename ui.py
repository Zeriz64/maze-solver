from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, win):
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bot_wall = True
        self.win = win

    def draw(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        if self.left_wall:
            self.win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.right_wall:
            self.win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.top_wall:
            self.win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.bot_wall:
            self.win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        x = self.x1 - self.x2
        y = self.y1 - self.y2
        from_x = self.x1 - x / 2
        from_y = self.y1 - y / 2

        x = to_cell.x1 - to_cell.x2
        y = to_cell.y1 - to_cell.y2
        to_x = to_cell.x1 - x / 2
        to_y = to_cell.y1 - y / 2
        
        if undo:
            color = "gray"
        else:
            color = "red"

        self.win.draw_line(Line(Point(from_x, from_y), Point(to_x, to_y)), color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, x, y):
        self.pointA = x
        self.pointB = y
    
    def draw(self, canvas, color):
        canvas.create_line(self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=color, width=2)

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, color="black"):
        line.draw(self.canvas, color)
