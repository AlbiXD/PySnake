import tkinter as tk
import random as rndm
gameWindow = tk.Tk()
gameWindow.geometry("500x500")



canvas = tk.Canvas(gameWindow, width=500, height=500, bg="white")
canvas.pack()

SCALE = 25
HEAD = "U"

isApple = False;

grid = ["E"] * 400

# Create GRID
for y in range(SCALE):
    canvas.create_line(0, y * SCALE, 500, y * SCALE)

for x in range(SCALE):
    canvas.create_line(x * SCALE, 0, x * SCALE, 500)





# x1 y1 x2 y2
rect = canvas.create_rectangle(0, 0, SCALE, SCALE, fill="green", outline="black")
apple = 0
# Movement Functions
def move_left(event):
    global HEAD
    HEAD = "L"

def move_right(event):
    global HEAD
    HEAD = "R"

def move_up(event):
    global HEAD
    HEAD = "U"

def move_down(event):
    global HEAD
    HEAD = "D"

gameWindow.bind("<Left>", move_left)
gameWindow.bind("<Right>", move_right)
gameWindow.bind("<Up>", move_up)
gameWindow.bind("<Down>", move_down)

canvas.move(rect, 50, 50)

def drawApple():
    global apple
    global isApple
    if isApple == False:
        apple = canvas.create_rectangle(0,0,SCALE, SCALE, fill ="red", outline="black")
        randomX = rndm.randint(0,19) 
        randomY = rndm.randint(0,19) 
        canvas.move(apple, SCALE*randomX,SCALE*randomY)
        isApple = True
        grid[randomX*randomY] = "A"
        print(randomX)
        print(randomY)
        print(randomX*randomY)



def Collision():
    return

# Continuous Movement
def gameLogic():
    global HEAD

    drawApple()

    if HEAD == "U":
        canvas.move(rect, 0, -SCALE)
    elif HEAD == "D":
        canvas.move(rect, 0, SCALE)
    elif HEAD == "L":
        canvas.move(rect, -SCALE, 0)
    elif HEAD == "R":
        canvas.move(rect, SCALE, 0)
    #Detect collision
    x1, y1, x2, y2 = canvas.coords(rect)



    gameWindow.after(200, gameLogic) 


gameLogic()
gameWindow.mainloop()
