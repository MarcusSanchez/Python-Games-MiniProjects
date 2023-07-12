from tkinter import *
import random

gameRunning = False
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 70
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#000000'
FOOD_COLOR = '#000000'
BACKGROUND_COLOR = '#FFFFFF'
directions = ['down', 'up', 'left', 'right']
score = 0
direction = random.choice(directions)


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([350, 350])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)


class Food:
    def __init__(self, snake):
        def findFood(snake):
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            if (x, y) in snake.coordinates or [x, y] in snake.coordinates:
                findFood(snake)
            else:
                self.coordinates = [x, y]
                canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

        findFood(snake)


def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f'Score:{score}')
        canvas.delete('food')
        food = Food(snake)

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        start_window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    if new_direction == 'right' and direction != 'left':
        direction = new_direction
    if new_direction == 'up' and direction != 'down':
        direction = new_direction
    if new_direction == 'down' and direction != 'up':
        direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True

    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1::]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    global gameRunning
    gameRunning = False
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text='GAME OVER', fill='red', tag='gameover')
    canvas.create_text(canvas.winfo_width() / 2, (canvas.winfo_height() / 2) + 75,
                       font=('consolas', 40), text='Press Space To Reset', fill='green', tag='gameover')


def start_button():
    global score, gameRunning
    if gameRunning is False:
        canvas.delete(ALL)

        canvas1 = Canvas(start_window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        canvas1.pack()

        start_window.update()
        score = 0
        label.config(text=f'Score:{score}')
        snake = Snake()
        food = Food(snake)
        next_turn(snake, food)
        gameRunning = True


start_window = Tk()
start_window.title("Snake")
start_window.resizable(False, False)

label = Label(start_window, text=f'Score:{score}', font=('consolas', 40))
label.pack()
canvas = Canvas(start_window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

canvas.create_text(250, 250,
                   font=('consolas', 70), text='SNAKE:', fill=SNAKE_COLOR, tag='NEKey')
canvas.create_text(350, 350,
                   font=('consolas', 25), text='Press Space Key to Start', fill='red', tag='NEKey')
start_window.bind('<space>', lambda event: start_button())

start_window.update()

start_window_width = start_window.winfo_width()
start_window_height = start_window.winfo_height()

screen_width = start_window.winfo_screenwidth()
screen_height = start_window.winfo_screenheight()

x = int((screen_width / 2) - (start_window_width / 2))
y = int((screen_height / 2) - (start_window_height / 2))
start_window.geometry(f'{start_window_width}x{start_window_height}+{x}+{y}')

start_window.geometry(f'{start_window_width}x{start_window_height}+{x}+{y}')
start_window.bind('<Left>', lambda event: change_direction('left'))
start_window.bind('<Right>', lambda event: change_direction('right'))
start_window.bind('<Up>', lambda event: change_direction('up'))
start_window.bind('<Down>', lambda event: change_direction('down'))

start_window.mainloop()
