import pyglet
from pyglet.window import mouse
from pyglet import clock
from pyglet.window import key
import os
import sys
import random
import decimal


pyglet.options['audio'] = ('directsound', 'openal', 'pulse')

window = pyglet.window.Window(width=1440, height=900)
window.set_caption('Math....ill')


num1_label = pyglet.text.Label('9',font_size = 100, x = 350, y = 500)
num2_label = pyglet.text.Label('2',font_size = 100, x = 650, y = 500)
mode_label = pyglet.text.Label('+',font_size = 100, bold = True, x = 500, y = 490)
result_label = pyglet.text.Label('87',font_size = 100, x = 1000, y = 500)
equal_label =  pyglet.text.Label('=',font_size = 100, x = 850, y = 500)

right_button = pyglet.resource.image('right_button.png')
wrong_button = pyglet.resource.image('wrong_button.png')
time_label = pyglet.text.Label('Time',font_size = 20, x = 20, y = 20)


you_win = pyglet.resource.image('you_win.jpg')
you_lose = pyglet.resource.image('you_lost.png')


#sound
correct_sound = pyglet.media.load('coolsfx.wav', streaming=False)
puzzle_backgroud = pyglet.media.load('puzzle_backgroud.wav', streaming=True)
fail_sound = pyglet.media.load('failsfx.wav',  streaming=False)



class Math(object):
    def __init__(self):
        self.time = 0
        self.num1 = 0
        self.num2 = 0
        self.mode = ''
        self.correct_math = 0
        self.incorrect_math = 0
        self.stat = 1
        self.result = 0
        self.selection = 0
        # self.stat= 1


math = Math()

@window.event
def on_draw():
    # print('1P
    num1_label.text = str(math.num1)
    num2_label.text = str(math.num2)
    mode_label.text = str(math.mode)
    result_label.text = str(math.result)


    if math.stat == 0:
        window.clear()
        you_lose.blit(250,200)
    else:
        window.clear()
        right_button.blit(450,140)
        wrong_button.blit(750,150)
        num1_label.draw()
        num2_label.draw()
        mode_label.draw()
        result_label.draw()
        equal_label.draw()
        time_label.text = 'TIME LEFT ' + str(5 - math.time)
        time_label.draw()
# @window.event
# def on_draw():

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return round(a / b, 2)


def generate_math():

    var1 = random.randint(1,9)
    var2 = random.randint(1,9)
    mode = random.randint(1,4)
    hash = random.randint(1,2)
    math.num1 = var1
    math.num2 = var2

    result = 0

    if mode == 1:
        result = add(var1,var2)
        math.mode = "+"
    if mode == 2:
        result = sub(var1,var2)
        math.mode = "-"
    if mode == 3:
        result = mul(var1,var2)
        math.mode = "x"
    if mode == 4:
        result = div(var1,var2)
        math.mode = "/"

    #Expect correct
    if hash == 1:
        # print('true')
        math.result = result
        math.selection = True
    #Expect incorrect
    else:
        result = result + random.randint(1,9)
        math.result = result
        math.selection = False


    # print(var1,' ',var2,' ',mode,' ' ,result,' ',hash)

generate_math()

def compare(player_choice):
    if player_choice == math.selection:
        correct_sound.play()
        math.time = 0
        generate_math()
    else:
        fail_sound.play()
        math.stat = 0
        # print('xxx')


def reset():
    math.stat = 1
    math.time = 0
    generate_math()


@window.event
def on_mouse_press(x, y, button, modifiers):

        player_choice = 99
        print(x,y)
        if math.stat == 0:
            if 440 < x < 650 and 269 < y < 360:
                sys.exit()

            if 800< x and x  < 1020 and 230 < y and y < 360:
                print('RESET')
                reset()
        else:
            if 450 < x < 650 and 140 < y < 350:
                player_choice = True
                print('RIGHT')
            if 745 < x < 1020 and 140 < y < 350:
                player_choice = False
                print('WRONG')
            compare(player_choice)


        # print(x,y)


def update_time(dt):
    if math.stat == 1:
        math.time += 1
        if math.time == 5:
           math.stat = 0


clock.schedule_interval(update_time,1)

pyglet.app.run()
