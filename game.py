import numpy as np
from tkinter import *

width, height = 25, 25

def load_from_path(path):
    file = open(path, "r")
    content = file.read()
    height = content.count('\n') + 1
    width = content.find('\n')
    content = content.replace("\n", "")
    start_state = np.zeros((width, height), dtype=bool)
    for i in range(width):
        for j in range(height):
            if(content[(i*height)+j] != '\n'):
                start_state[i][j] = content[(i*height)+j]
    file.close()
    return start_state

def next_board_state(current_state):
    next_state = np.copy(current_state)
    for x in range(width):
        for y in range(height):
            sum = 0
            for p in range (x-1, x+2):
                for q in range(y-1, y+2):
                    if((x,y) != (p,q) and p >= 0 and q >= 0 and p < width and q < height):
                        if(current_state[p][q]):
                            sum += 1
            if(sum < 2):
                next_state[x][y] = 0
            elif(sum == 2 and current_state[x][y] == 1):
                next_state[x][y] = 1
            elif(sum == 3):
                next_state[x][y] = 1
            else:
                next_state[x][y] = 0
    return next_state

def render(canvas, board):
    height, width = board.shape
    img = PhotoImage(width=width*10, height=height*10)

    for i in range(height):
        for j in range(width):
            color = "#000000" if board[i][j] else "#FFFFFF"
            for k in range(10):
                for l in range(10):
                    img.put(color, (j * 10 + k, i * 10 + l))

    canvas.create_image((0, 0), image=img, anchor="nw")
    canvas.img = img

def render_board(root, canvas, current_state):
    render(canvas, current_state)
    next_state = next_board_state(current_state)
    root.after(10, render_board, root, canvas, next_state)

def main():
    start_state = np.random.choice([True, False], size=(width, height))
    #start_state = load_from_path("toad.txt")
    root = Tk()
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()

    render_board(root, canvas, start_state)

    mainloop()

if __name__ == "__main__":
    main()