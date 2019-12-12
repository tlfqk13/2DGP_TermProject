name="TitleState"
from pico2d import *
import game_framework
import world_build_state as main_state

image=None


def enter():
    global image
    image=load_image('resource/background_1.png')
    global bgm
    bgm=load_wav('resource/bg_0.wav')

def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)

def update():
    pass
def draw():
    clear_canvas()
    image.draw(400,300)
    bgm.play()
    update_canvas()
