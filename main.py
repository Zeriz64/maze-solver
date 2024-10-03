from ui import *
from maze import Maze

width = 800
height = 600

def main():
    width = 1920
    height = 1080
    buffer = 20
    cell_size = 40
    num_cols = (width - buffer) // cell_size
    num_rows = (height - buffer) // cell_size


    win = Window(width, height)
    maze = Maze(buffer, buffer, num_rows, num_cols, cell_size, cell_size, win)
    win.wait_for_close()

main()
