from ui import *

def main():
    win = Window(800, 600)
    test_cell = Cell(win)
    test_cell.top_wall = False
    test_cell.right_wall = False
    test_cell2 = Cell(win)
    test_cell2.left_wall = False
    test_cell2.right_wall = False
    test_cell3 = Cell(win)
    test_cell3.bot_wall = False
    test_cell3.left_wall = False
    test_cell.draw(2,2, 42,42)
    test_cell2.draw(42,2, 82,42)
    test_cell3.draw(82,2, 122,42)
    test_cell.draw_move(test_cell2)
    test_cell2.draw_move(test_cell3)
    win.wait_for_close()

main()
