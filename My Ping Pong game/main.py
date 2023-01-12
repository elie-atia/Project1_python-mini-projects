from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
RACKET_WIDTH = 50
RACKET_HEIGHT = 250
SPACE_SIZE = 50
RACKET_COLOR = "#00FF00"
BALL_COLOR = "#FF0000"
BACKGROUND_COLOR = "#FFFFFF"

class Racket:
    def __init__(self,number = 1):
        if(number == 1):
            x = 0
        else:
            x = GAME_WIDTH -SPACE_SIZE
            print("racket 2 created")
        
        self.coordinates = [x,GAME_HEIGHT/2 - GAME_HEIGHT/2]
        self.square = canvas.create_rectangle(self.coordinates[0], self.coordinates[1], self.coordinates[0] + RACKET_WIDTH, self.coordinates[1] + RACKET_HEIGHT, fill=RACKET_COLOR, tag="racket")
            

def check_racket_inside(y):

    if y < 0 or y >= (GAME_HEIGHT-RACKET_HEIGHT+SPACE_SIZE):
        return False
    return True

def change_direction(racket,direction):

    x, y = racket.coordinates


    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE

    if (check_racket_inside(y)):

        racket.coordinates[1] = y

        canvas.delete(racket.square)

        square = canvas.create_rectangle(x, y, x + RACKET_WIDTH, y + RACKET_HEIGHT, fill=RACKET_COLOR)

        racket.square = square


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


racket1 = Racket(1)
racket2 = Racket(2)


window.bind('<Up>', lambda event: change_direction(racket1,'up',))
window.bind('<Down>', lambda event: change_direction(racket1,'down'))

window.bind('<w>', lambda event: change_direction(racket2,'up',))
window.bind('<s>', lambda event: change_direction(racket2,'down'))


window.mainloop()