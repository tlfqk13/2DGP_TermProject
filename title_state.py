from pico2d import *
import object as o
import game_framework
import main_state
import lobby_state

name = "TitleState"
background = None
char = None
title = None
oList = []

class button(o.object):
    def __init__(self, imageString, origin, future):
        o.object.__init__(self,imageString)
        self.origin = origin
        self.future = future
    def overlapButton(self, x, y):
        if self.x - self.imageWidth / 4 < x and self.x + self.imageWidth /4 > x and \
            self.y - self.imageHeight / 4 < y and self.y + self.imageHeight /4 > y:
            self.changeClipFrame(0, self.future)
        else:
            self.bottom = self.origin
    def clickButton(self,x,y):
        if self.x - self.imageWidth / 4 < x and self.x + self.imageWidth / 4 > x and \
                self.y - self.imageHeight / 4 < y and self.y + self.imageHeight / 4 > y:
            return True
        else:
            return False

def enter():
    global background,char,title
    title = o.object('resource/select03.png')
    background=o.object('resource/background.png')
    oList.append(button('resource/select03.png', 278,125))

    #oList.append(button('start.png', 300, 0))
    background.setPos(400,300)
    background.setSize(800,600)
    title.setPos(300,850)
    title.setSize(278,252)

    oList[0].setPos(100, 150)
    oList[0].setSize(100,100)
    oList[0].setClipSize(278,125)
    #oList[1].setPos(100, 50)
    #oList[1].setSize(100, 100)
    #oList[1].setClipSize(163, 155)

def exit():
    global background
    del background
    oList.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if event.type == SDL_MOUSEMOTION:
                x = event.x
                y = 600 - 1 - event.y
                oList[0].overlapButton(x,y)
                #oList[1].overlapButton(x,y)
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 600 - 1 - event.y
                if oList[0].clickButton(x, y) is True:
                    game_framework.change_state(lobby_state)
                    break
                #if oList[1].clickButton(x, y) is True:
                 #   game_framework.quit()

def draw():
    clear_canvas()
    title.draw()
    background.draw()

    for i in range(len(oList)-2):
        oList[i].update()
    oList[0].clip_draw()
#    oList[1].clip_draw()
    update_canvas()

def update():
    pass