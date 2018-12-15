import pyglet
from pyglet.window import mouse
from pyglet import clock
from pyglet.window import key
import os
import sys




window = pyglet.window.Window(width=1440, height=900)
window.set_caption('Difffernz')

# caaa = pyglet.image.load('caaa.png')
# caaa_sprite = pyglet.sprite.Sprite(caaa,x=926,y=471)


heart = pyglet.resource.image('heart.jpg')

                    #import pictures

#easy_level
easy1 = pyglet.resource.image('findtheoddemoji.jpg')


#medium level
medium1 = pyglet.resource.image('emoji2.jpg')
medium2 = pyglet.resource.image('emoji3.jpg')
medium3 = pyglet.resource.image('geometry.jpg')
medium4 = pyglet.resource.image('geometry2.jpg')


#hard_level
hard1 = pyglet.resource.image('pikachu.jpg')
hard2 = pyglet.resource.image('emoji4.jpg')
hard3 = pyglet.resource.image('sun.jpg')


#result_noti
you_win = pyglet.resource.image('you_win.jpg')
you_lose = pyglet.resource.image('you_lost.png')

                    #import sounds

#sound_effect
fail_sound = pyglet.media.load('failsfx.wav',  streaming=False)
correct_sound = pyglet.media.load('coolsfx.wav', streaming=False)
puzzle_backgroud = pyglet.media.load('puzzle_backgroud.wav', streaming=True)



pyglet.options['audio'] = ('directsound', 'openal', 'pulse')

stage_level = [None,easy1,medium1,medium2,medium3,medium4,hard1,hard2,hard3, None]
heart_display = [None,heart,heart,heart]
puzzle_backgroud.play()

class Puzzle(object):
    def __init__(self):
        self.stage = 1
        self.heart = 3
        self.answer_list_x = dict()
        self.answer_list_x = dict()
        self.temp = 0
        self.game_stat = ''
        self.time = 0
        self.score = 0



puzzle = Puzzle()


stage_label = pyglet.text.Label(str(puzzle.stage),
                                font_name = 'Space Age',
                                bold = True,
                                font_size = 40,
                                x=720, # origin - left
                                y=50, # origin - bottom
                                anchor_x='center',
                                anchor_y='center')

time_label = pyglet.text.Label('Time',font_size = 20, x = 20, y = 20)


puzzle.answer_list_x = {1:[730,862] , 2:[308,400], 3:[1140,1230],
                        4:[540,900] , 5:[121,500], 6:[200,300],
                        7:[1025,1078]}


puzzle.answer_list_y = {1:[430,563] , 2:[236,330], 3:[241, 320],
                        4:[185,591] , 5:[141,697], 6:[410, 500],
                        7:[490,548]}




@window.event
def on_draw():
    # print('1P
    window.clear()

    x = 0

    if puzzle.game_stat == 'WIN':
        you_win.blit(300,200)

    elif puzzle.game_stat == 'LOSE':
        you_lose.blit(250,200)

    else:
        for i in range (1,puzzle.heart+1):
            heart_display[i].blit(x, 850)
            x += 50

        if (puzzle.stage == 8):
            stage_level[puzzle.stage].blit(200,0)
        else:
            stage_level[puzzle.stage].blit(85,100)

        time_label.text = 'TIME LEFT ' + str(5 - puzzle.time)
        time_label.draw()

        stage_label.text = 'STAGE ' + str(puzzle.stage)
        stage_label.draw()


def reset():
    puzzle.game_stat = ''
    puzzle.stage = 1
    puzzle.heart = 3
    puzzle.time = 0


def check_result(x,y, stage):

    # print('STAGE is', stage)
    stage = puzzle.stage

    x_start = puzzle.answer_list_x[puzzle.stage][0]
    x_end = puzzle.answer_list_x[puzzle.stage][1]
    # print('X',x_start,x_end)
    y_start = puzzle.answer_list_y[puzzle.stage][0]
    y_end = puzzle.answer_list_y[puzzle.stage][1]


    #Current stage_level


    if x_start < x and x < x_end and y_start < y and y < y_end:
        correct_sound.play()
        if stage + 1 == 8:
            puzzle.game_stat = 'WIN'
            puzzle.score += 100
            # file_object  = open('~/lchi/pyglet/score.txt', 'rw' )
            # file_object.write(score)
        else:
            puzzle.stage += 1
        puzzle.time = 0

    else:
        fail_sound.play()
        puzzle.heart -= 1
        if puzzle.heart == 0:
            puzzle.game_stat = 'LOSE'
            sys.exit()


@window.event
def on_mouse_press(x, y, button, modifiers):

    # print('mouse pressed')
    # print(x,y)
    if puzzle.game_stat == 'WIN':
        sys.exit()
    if puzzle.game_stat != 'LOSE':
        check_result(x,y,puzzle.stage)

    if puzzle.game_stat == 'LOSE':
        if 440 < x < 650 and 269 < y < 360:
            sys.exit()

        if 800< x < 1020 and 230 < y < 360:
            reset()


def update_time(time):
    puzzle.time += 1
    if puzzle.time == 5:
       puzzle.game_stat = 'LOSE'
    print(puzzle.time)


clock.schedule_interval(update_time,1)
pyglet.app.EventLoop()
pyglet.app.run()
