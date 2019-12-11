from pico2d import *
from bubble import Bubble
import game_world
import game_framework

TIME_PER_ACTION=0.2
ACTION_PER_TIME=1.0/TIME_PER_ACTION
FRAMES_PER_ACTION=4

RIGHT_DOWN,LEFT_DOWN,RIGHT_UP,LEFT_UP,UP_UP,DOWN_DOWN,UP_DOWN,DOWN_UP,\
    DASH_LDOWN,DASH_LUP,DASH_RDOWN,DASH_RUP,\
    KEY_BUBBLE,KEY_ITEM=range(14)

key_event_table={
    (SDL_KEYDOWN,SDLK_RIGHT):RIGHT_DOWN,
    (SDL_KEYDOWN,SDLK_LEFT):LEFT_DOWN,
    (SDL_KEYUP,SDLK_RIGHT):RIGHT_UP,
    (SDL_KEYUP,SDLK_LEFT):LEFT_UP,
    (SDL_KEYUP,SDLK_LSHIFT):DASH_LUP,
    (SDL_KEYDOWN,SDLK_LSHIFT):DASH_LDOWN,
    (SDL_KEYDOWN,SDLK_RSHIFT):DASH_RDOWN,
    (SDL_KEYUP,SDLK_RSHIFT):DASH_RUP,
    (SDL_KEYUP,SDLK_UP):UP_UP,
    (SDL_KEYDOWN,SDLK_UP):UP_DOWN,
    (SDL_KEYDOWN,SDLK_DOWN):DOWN_DOWN,
    (SDL_KEYUP,SDLK_DOWN):DOWN_UP,
    (SDL_KEYDOWN,SDLK_m):KEY_BUBBLE,
    (SDL_KEYDOWN,SDLK_n):KEY_ITEM
}



class CBoy:

    def __init__(self):
        self.IsDead=False
        self.x, self.y = 500,350
        self.L_image = load_image('resource/Left.png')
        self.R_image=load_image('resource/Right.png')
        self.Up_image=load_image('resource/Up.png')
        self.Down_image=load_image('resource/Down.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.y_dir=1
        self.vector_y=250
        self.velocity = 0
        self.y_velocity=0
        self.speed=600
        self.radius=60
        self.frame=0
        self.timer=0

    def collide(a, b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def Bubble(self):
        bubble=Bubble(self.x,self.y)
        #game_world.add_gameobject()object(bubble,2)


    def update(self):
        if self.IsDead:
            return -1

        self.frame=(self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%4
        self.x=clamp(64,self.x,720-64)

        return 0


    def get_boy(self):
        return object[1]

    def get_boyX(self):
        return self.x

    def get_boyY(self):
        return self.y

    def draw(self):
        self.L_image.clip_draw(int(self.frame) * 44, 0, 44, 52, self.x, self.y)

    def handle_events(self):


    def stop(self):
         self.velocity=0

         if(self.dir==1):
             self.velocity=1

