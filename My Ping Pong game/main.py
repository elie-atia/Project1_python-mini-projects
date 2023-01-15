from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200
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
            
class Ball:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BALL_COLOR, tag="ball")

def next_ball_place(ball,racket1,racket2,ball_direction):

    x, y = ball.coordinates
    
    #print(f'ball direction is {ball_direction}')

    if ball_direction == "up":
        y -= SPACE_SIZE
    elif ball_direction == "down":
        y += SPACE_SIZE
    elif ball_direction == "left":
        x -= SPACE_SIZE
    elif ball_direction == "right":
        x += SPACE_SIZE

    if x == racket1.coordinates[0] and y in range(int(racket1.coordinates[1]),int(racket1.coordinates[1]+RACKET_HEIGHT)):

        x += 2*SPACE_SIZE
        ball_direction = "right"
        print('collision with racket 1')

    if x == racket2.coordinates[0] and y in range(int(racket2.coordinates[1]),int(racket2.coordinates[1]+RACKET_HEIGHT)):

        x -= 2*SPACE_SIZE
        ball_direction = "left"

    elif x == 0:

        print("game over, racket1 loss")
        game_over(1)
    
    elif x>= (GAME_WIDTH-RACKET_WIDTH+SPACE_SIZE):

        pint("game over, racket2 loss")
        game_over(2)

    canvas.delete("ball")
    
    ball.coordinates = [x,y]

    square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BALL_COLOR,tag="ball")
    

    window.after(SPEED, next_ball_place, ball,racket1, racket2,ball_direction)


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

def game_over(number):

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text=f"GAME OVER RACKET{number} LOSS" , fill="red", tag="gameover")

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
ball_direction = 'left'

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
ball = Ball()


window.bind('<Up>', lambda event: change_direction(racket1,'up',))
window.bind('<Down>', lambda event: change_direction(racket1,'down'))

window.bind('<w>', lambda event: change_direction(racket2,'up',))
window.bind('<s>', lambda event: change_direction(racket2,'down'))

next_ball_place(ball,racket1,racket2,ball_direction)

window.mainloop()