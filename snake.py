import tkinter as tk
import random as rndm
gameWindow = tk.Tk()
gameWindow.geometry("500x500")



canvas = tk.Canvas(gameWindow, width=500, height=500, bg="white")
canvas.pack()


SCALE = 25
HEAD = "F"

isApple = False;
previousIndex = 0
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

def print_grid(event):
    for i in range(len(grid)):  # Remove +1
        print(grid[i], end=" ")
        if (i + 1) % 20 == 0:  # Adjust condition
            print()  # Newline after every 20 elements
    print("-----------------------------------------")

gameWindow.bind("<Left>", move_left)
gameWindow.bind("<Right>", move_right)
gameWindow.bind("<Up>", move_up)
gameWindow.bind("<Down>", move_down)
gameWindow.bind("r", print_grid)

sX = rndm.randint(1,18) 
sY = rndm.randint(3,16)
canvas.move(rect, SCALE*sX, SCALE*sY)

x1, y1, x2, y2 = canvas.coords(rect)
prevIndex = int(((x2/25)*(y2/25))-1)

def drawApple():
    global apple
    global isApple
    if isApple == False:
        apple = canvas.create_rectangle(0,0,SCALE, SCALE, fill ="red", outline="black")
        row = rndm.randint(0,19) 
        col = rndm.randint(0,19)
        print(row+1, col+1)
        canvas.move(apple, SCALE*row,SCALE*col)
        isApple = True
        grid[(col*20) + (row)] = "A"



def Collision():
    return

# Continuous Movement
def gameLogic():
    global HEAD
    global prevIndex
    
    drawApple()

    #LETS MOVE THE DAMN SNAKE
    if HEAD == "U":
        canvas.move(rect, 0, -SCALE)
    elif HEAD == "D":
        canvas.move(rect, 0, SCALE)
    elif HEAD == "L":
        canvas.move(rect, -SCALE, 0)
    elif HEAD == "R":
        canvas.move(rect, SCALE, 0)

    
    x1, y1, x2, y2 = canvas.coords(rect)


    
    index = int(((x2/25)*(y2/25))-1)


    x = (x2/25)-1
    y = (y2/25)-1
    
    if(index < 0 or x > 19 or y > 19):
        gameWindow.destroy()
        return
    
    grid[index] = "S"
    print("Current Index: ", index)
    print("Previous Index: ", prevIndex)

    prevIndex = index;
    gameWindow.after(20000, gameLogic) 


gameLogic()
gameWindow.mainloop()



