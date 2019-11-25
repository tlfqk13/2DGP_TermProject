from pico2d import *
import object as o
import game_framework
import main_state

name = "Lobby_State"
background = None
oList = []

class button(o.object):
    def __init__(self, imageString, origin, future):
        o.object.__init__(self,imageString)
        self.origin = origin
        self.future = future
    def overlapButton(self, x, y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
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
    global background,title
    title = o.object('resource/start.png')
    background=o.object('resource/select.png')

    oList.append(button('resource/mao.png', 300, 180))
    oList.append(button('resource/dao.png', 320, 240))
    #oList.append(button('pre_char_s.png',135,150))
    #oList.append(button('pre_char_s.png',300,150))

    background.setPos(400,300)
    background.setSize(800,600)
    title.setPos(300,850)

    oList[0].setPos(130,360)
    oList[0].setSize(180,180)
    oList[0].setClipSize(300,180)

    oList[1].setPos(320, 360)
    oList[1].setSize(180, 180)
    oList[1].setClipSize(300,240)
    #oList[2].setPos(135, 150)
    #oList[2].setSize(180, 180)
    #oList[2].setClipSize(150, 240)
    #oList[3].setPos(300, 150)
    #oList[3].setSize(180, 180)
    #oList[3].setClipSize(300,240)

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
                oList[1].overlapButton(x,y)
                #oList[2].overlapButton(x, y)
                #oList[3].overlapButton(x, y)
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 600 - 1 - event.y
                if oList[0].clickButton(x, y) is True:
                    game_framework.change_state(main_state)
                    break
                if oList[1].clickButton(x, y) is True:
                    game_framework.change_state(main_state)
                    break
                #if oList[2].clickButton(x, y) is True:
                    #game_framework.change_state(main_state)
                    #break
                #if oList[3].clickButton(x, y) is True:
                    #game_framework.change_state(main_state)
                    #break


def draw():
    clear_canvas()
    title.draw()
    background.draw()



    for i in range(len(oList)-2):
        oList[i].update()
    oList[0].clip_draw()
    oList[1].clip_draw()
    #oList[2].clip_draw()
    #oList[3].clip_draw()
    update_canvas()

def update():
    pass