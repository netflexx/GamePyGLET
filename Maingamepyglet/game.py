import pyglet
from pyglet.window import mouse
from pyglet import clock
from pyglet.window import key

window = pyglet.window.Window(width=1440, height=700)
window.set_caption('A different caption')


label = pyglet.text.Label('Hello',font_size = 46, x = 1440, y = 900,
                          anchor_x='center', anchor_y='center')
imageplayer = pyglet.image.load('coolplayer.png')
clone = imageplayer


enemy = pyglet.image.load('enemy.png')
enemy_clone_list = []

galaxy  = pyglet.image.load('galaxy.jpg')
# galaxy_backgroud = pyglet.sprite.Sprite(galaxy)
white_backgroud = pyglet.image.load('white.jpg')

spaceship = pyglet.image.load('spaceship.gif')
# smallship =
animspaceship = pyglet.sprite.Sprite(spaceship)
#t_caption('COOL


findemoji = pyglet.image.load('findtheoddemoji.jpg')





@window.event
def on_draw():
    # print('1P
    window.clear()
    label.draw()
    white_backgroud.blit(0,0)
    enemy.blit(1340,400) #go form 1500 to 1340
    # galaxy.blit(0,-50)
    # animspaceship.draw()
    print(player.Ycor)
    imageplayer.blit(50, player.Ycor)
    # for i in range(8):
    #     enemy_clone_list.append()
    # clone.blit(400,player.Ycor)
    # print(mouse1.mousex)


@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x,y)






time = 0
# print('1')
class Mouse(object):
    def __init__(self):
        self.mousex = 0
        self.mousey = 0
        self.temp = 0

mouse1 = Mouse()


class main_player(object):
    def __init__(self):
        self.Xcor = 0
        self.Ycor = 300
        self.temp = 0
        self.press_stat = 0

player = main_player()


@window.event
def on_text_motion(motion):
    temp = player.Ycor

    if (motion == pyglet.window.key.MOTION_UP):
        temp += 10
        if temp >= 590:
            player.Ycor = 590
        else:
            player.Ycor += 10
    if (motion == pyglet.window.key.MOTION_DOWN):
        temp -= 10
        if temp <= -40:
            player.Ycor = -40
        else:
            player.Ycor -= 10

@window.event
def on_key_press(symbol, modifiers):
    print('on_key_press')
    if symbol == key.W:
        player.Xcor += 10
        player.press_stat = 1
    if symbol == key.S:
        player.Xcor -= 10
    print('A key was pressed')
    # print(symbol,modifiers)

@window.event
def on_mouse_press(x, y, button, modifiers):
    print('mouse pressed')
    print(x,y)

@window.event
def on_draw():
    # print('1P
    window.clear()
    label.draw()
    white_backgroud.blit(0,0)
    enemy.blit(1340,400) #go form 1500 to 1340
    # galaxy.blit(0,-50)
    # animspaceship.draw()
    print(player.Ycor)
    imageplayer.blit(50, player.Ycor)
    # for i in range(8):
    #     enemy_clone_list.append()
    # clone.blit(400,player.Ycor)
    # print(mouse1.mousex)

def update(dt):
    print('cool')
    clone.blit(400,player.Ycor)
    # print('%f seconds since last callback', dt)
    # print(dt)
    # if player.press_stat == 1:
    #     player.Xcor += 10
    #     player.press_stat  = 0
    #     print(player.press_stat)
    #     print(dt)

def time_elapsed(dt):
    global time


    time += 1
    # print(time)
    # print("ds")

pyglet.clock.schedule_interval(update, 1)
pyglet.clock.schedule_interval(time_elapsed, 1)

pyglet.app.run()
