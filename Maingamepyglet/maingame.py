import pyglet
from pyglet.window import key
from pyglet.window import mouse
import random
import sys
#from puzzle_game import *
#from math_game import *
from question import *


# Global variables:
# Creat a black window:
window = pyglet.window.Window(1440, 900)

label = pyglet.text.Label("0", font_size=36, y=300, x=400)

pause_texture = pyglet.image.load('pause_75_75.png')
pause_sprite = pyglet.sprite.Sprite(pause_texture, x=1300, y=window.height-100)

choice1 = pyglet.image.load('mrtoan.png')
choice2 = pyglet.image.load('mrhung.png')
choice3 = pyglet.image.load('mslaurie.png')
choice4 = pyglet.image.load('mrmanoj.png')

choice1_sprite = pyglet.sprite.Sprite(choice1, x=900,y=200)
choice2_sprite = pyglet.sprite.Sprite(choice2, x=1050,y=200)
choice3_sprite = pyglet.sprite.Sprite(choice3, x=350,y=200)
choice4_sprite = pyglet.sprite.Sprite(choice4, x=200,y=200)

day = pyglet.image.load('day.png')
mid = pyglet.image.load('midday.png')
night = pyglet.image.load('night.png')
day_sprite = pyglet.sprite.Sprite(img=day)
mid_sprite = pyglet.sprite.Sprite(img=mid)
night_sprite = pyglet.sprite.Sprite(img=night)

#music_game = pyglet.image.load('music_on_32_32.png')
#music_sprite = pyglet.sprite.Sprite(music_game)

replay_texture = pyglet.image.load('replay_75_75.png')
replay_sprite = pyglet.sprite.Sprite(replay_texture, x=1300, y=window.height-100)

guideEN = pyglet.image.load('guideEN.png')
guideEN_sprite = pyglet.sprite.Sprite(guideEN)

guideFR = pyglet.image.load('guideFR.png')
guideFR_sprite = pyglet.sprite.Sprite(guideFR)

screenEN = pyglet.image.load('EN.png')
screenEN_sprite = pyglet.sprite.Sprite(screenEN)

screenFR = pyglet.image.load('FR.png')
screenFR_sprite = pyglet.sprite.Sprite(screenFR)

question_mark = pyglet.image.load('question_mark_120_60.png')
question_mark_sprite = pyglet.sprite.Sprite(question_mark, x = random.randint(100,800) ,y = random.randint(100,1300))

overEN = pyglet.image.load('overEN.png')
overEN_sprite = pyglet.sprite.Sprite(overEN)
overFR = pyglet.image.load('overFR.png')
overFR_sprite = pyglet.sprite.Sprite(overFR)

arcade_puzzle = pyglet.image.load('arcade.png')
arcade_puzzle_sprite = pyglet.sprite.Sprite(arcade_puzzle, x= 800, y = 700)
arcade_math = pyglet.image.load('arcade_math.png')
arcade_math_sprite = pyglet.sprite.Sprite(arcade_math, x = 900, y = 700)

# music
main_music = pyglet.resource.media("Kevin MacLeod _ Silly Fun [all in one].mp3",streaming=False)



class Game(object):
    def __init__(self):
        self.character_x = 830              # starting posistion of character
        self.character_y = 620
        self.pause = False
        self.screenwindow = True
        self.guide = False
        self.mark_appears = False
        self.time = 0
        self.gameover = False
        self.character = pyglet.resource.image('mrmanoj.png')
        self.day = True
        self.mid = False
        self.night = False
        self.lang = 'EN'            # language, default : English
        self.playhere = False
        self.score = 0
        self.musicp = False
game = Game()


# moving character base on key press:
@window.event
def on_text_motion(motion):
    if game.screenwindow is False and game.pause is False:
        if motion == pyglet.window.key.MOTION_RIGHT:
            if (game.character_x + 15) < 1030:
                game.character_x += 15
        elif motion == pyglet.window.key.MOTION_UP:
            if (game.character_y + 15) < 740:
                game.character_y += 15
        elif motion == pyglet.window.key.MOTION_LEFT:
            if (game.character_x - 15) > 450:
                game.character_x -= 15
        elif motion == pyglet.window.key.MOTION_DOWN:
            if (game.character_y - 15) > 160:
                game.character_y -= 15

# press Y to quit guide screen:
@window.event
def on_key_press(symbol, modifiers):
    if not game.screenwindow and game.guide:
        if symbol == key.Y:
            game.guide = False
            game.playhere = True
    if not game.screenwindow and not game.guide and game.playhere:
        if symbol == key.Q:
            game.gameover = True


@window.event
def on_mouse_press(x, y, button, modifiers):
    # print(x,y)
    # hit Play button to start game:
    kv = random.randint(1,2)
    if game.screenwindow is True and x > 475  and x < 960:
        if y > 130  and y < 275 :
            game.screenwindow = False
            game.guide = True
            return
    # hit arcade game machine:
    if not game.pause and game.playhere is True:
        # print (x,y)
        if x > 810 and x < 860:
            if y > 708 and y < 825:
                if kv == 1:
                    os.system('python3 puzzletest.py')
                else:
                    os.system('python3 debugtest.py')
    if not game.pause and game.playhere is True:
        if x > 910 and x < 960:
            if y > 700 and y < 825:
                os.system('python3 mathtest.py')
    # hit pause button to pause game:
    if game.screenwindow is False and game.pause is False and x > pause_sprite.x and x < (pause_sprite.x + pause_sprite.width):
        if y > pause_sprite.y and y < (pause_sprite.y + pause_sprite.height):
            game.pause = True
            return
    # hit replay to replay:
    if game.screenwindow is False and game.pause is True and x > replay_sprite.x and x < (replay_sprite.x + replay_sprite.width):
        if y > replay_sprite.y and y < (replay_sprite.y + replay_sprite.height):
            game.pause = False
            return
    # change character base on player's mouse click position, default = mrManoj:
    if game.screenwindow is True and game.pause is False and x > 350 and x < 500:
        if y > 350 and y < 500:
            game.character = pyglet.resource.image('mrhung.png')
            return
    elif game.screenwindow is True and game.pause is False and x > 790 and x < 935 :
        if y > 350  and y < 500 :
            game.character = pyglet.resource.image('mslaurie.png')
            return
    elif game.screenwindow is True and game.pause is False and x > 570 and x < 710:
        if y > 350 and y < 500 :
            game.character = pyglet.resource.image('mrtoan.png')
            return
    # change language through clicking:
    if game.screenwindow is True and game.pause is False and x > 50 and x < 125:
        if y > 130 and y < 190 :
            game.lang = 'EN'
            return
    if game.screenwindow is True and game.pause is False and x > 50 and x < 125:
        if y > 250 and y < 310 :
            game.lang = 'FR'
            return
    # replay or quit at game over screen:
    if game.gameover is True :
        if x > 540 and x < 850:
            if y > 325 and y < 425 :
                game.gameover = False
                game.screenwindow = True
                return
        if x > 600 and x < 780:
            if y > 170 and y < 260 :
                sys.exit()
                return
    # hit bugs:
    if game.playhere is True and game.pause is False and x > question_mark_sprite.x and x < (question_mark_sprite.x + question_mark_sprite.width):
        if y > question_mark_sprite.y and y < (question_mark_sprite.height + pause_sprite.y) :
            game.lang = 'EN'
            return


game.character.anchor_x = game.character.width
game.character.anchor_y = game.character.height


# Event callbacks
@window.event
def on_draw():
    # check language and draw start screen:
    if game.screenwindow and game.lang != 'FR' and not game.guide:
       window.clear()
       screenEN_sprite.draw()
    elif game.screenwindow and game.lang != 'EN' and not game.guide:
       window.clear()
       screenFR_sprite.draw()
    # check language and draw guide screen:
    elif game.guide is True and not game.screenwindow and game.lang == 'EN':
       window.clear()
       day_sprite.draw()
       guideEN_sprite.draw()
    elif game.guide is True and not game.screenwindow and game.lang == 'FR':
       window.clear()
       day_sprite.draw()
       guideFR_sprite.draw()
    # draw game screen:
    elif game.playhere:
        if not game.pause and not game.gameover:
            window.clear()
            label.draw()
            if game.time % 15 == 0 or game.time == 10:
                if game.time > 1:
                    game.mark_appears = True
            if game.day:
                day_sprite.draw()
                game.character.blit(game.character_x, game.character_y)
                pause_sprite.draw()
                arcade_math_sprite.draw()
                arcade_puzzle_sprite.draw()
            elif game.night:
                night_sprite.draw()
                game.character.blit(game.character_x, game.character_y)
                pause_sprite.draw()
                arcade_math_sprite.draw()
                arcade_puzzle_sprite.draw()
            elif game.mid:
                mid_sprite.draw()
                game.character.blit(game.character_x, game.character_y)
                arcade_math_sprite.draw()
                arcade_puzzle_sprite.draw()
                pause_sprite.draw()
            if game.mark_appears:
                question_mark_sprite.draw()
        if game.gameover and game.lang == 'EN':
            window.clear()
            overEN_sprite.draw()
        elif game.gameover and game.lang == 'FR':
            window.clear()
            overFR_sprite.draw()
        if game.pause:
            replay_sprite.draw()


def time_elapsed(dt):
    if game.playhere and game.pause is False:
        game.time +=1
        # print(game.time)
    if game.time > 120 and game.time < 240:
        game.mid = True
        game.day = False
        game.night = False
    if game.time > 240 and game.time < 300:
        game.night = True
        game.day = False
        game.mid = False
    if game.gameover is True:
        game.night = False
        game.day = True
        game.mid = False
        game.time = 0
    if game.time == 1 or game.time % 76 == 0:
        game.time > 1
        game.musicp = True
    if game.musicp:
        main_music.play()
        game.musicp = False



# Game loop (loop? Why loop?)
def game_loop(dt):
    label.text = str(int(label.text) + 1)


pyglet.clock.schedule(game_loop)
pyglet.clock.schedule_interval(time_elapsed,1)
pyglet.app.run()
