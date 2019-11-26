from pico2d import *
import game_framework

playtime=0.0

def enter():
    global image
    image=load_image('resource/b0s2w-n8tki.png')

def exit():
    global image
    del image
    image=None

    global playtime
    playtime=0.0


def handle_events():
    events=get_events()

    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else :
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()

def update():
    global playtime
    playtime=get_time()
    print(playtime)

    #물폭탄 생성

