from pico2d import *
from bubble import Bubble


import game_world

# girl Event
RIGHT_DOWN,LEFT_DOWN,RIGHT_UP,LEFT_UP,UP_UP,DOWN_DOWN,UP_DOWN,DOWN_UP,\
    DASH_LDOWN,DASH_LUP,DASH_RDOWN,DASH_RUP,\
    RCTRL=range(13)


key_event_table={
    (SDL_KEYDOWN,SDLK_d):RIGHT_DOWN,
    (SDL_KEYDOWN,SDLK_a):LEFT_DOWN,
    (SDL_KEYUP,SDLK_d):RIGHT_UP,
    (SDL_KEYUP,SDLK_a):LEFT_UP,
    (SDL_KEYUP,SDLK_LSHIFT):DASH_LUP,
    (SDL_KEYDOWN,SDLK_LSHIFT):DASH_LDOWN,
    (SDL_KEYDOWN,SDLK_RSHIFT):DASH_RDOWN,
    (SDL_KEYUP,SDLK_RSHIFT):DASH_RUP,
    (SDL_KEYUP,SDLK_w):UP_UP,
    (SDL_KEYDOWN,SDLK_w):UP_DOWN,
    (SDL_KEYDOWN,SDLK_s):DOWN_DOWN,
    (SDL_KEYUP,SDLK_s):DOWN_UP,
    (SDL_KEYDOWN,SDLK_RCTRL):RCTRL
}

# girl States
class IdleState:
    @staticmethod
    def enter(girl,event):
        if event == RIGHT_DOWN:
            girl.velocity+=1
        elif event == LEFT_DOWN:
            girl.velocity-=1
        elif event==RIGHT_UP:
            girl.velocity-=1
        elif event==LEFT_UP:
            girl.velocity+=1
        if event ==UP_DOWN:
            girl.y_velocity+=1
        elif event==DOWN_DOWN:
            girl.y_velocity-=1
        elif event==UP_UP:
            girl.y_velocity-=1
        elif event==DOWN_UP:
            girl.y_velocity+=1
        girl.timer=4
    @staticmethod
    def exit(girl,event):
        if event==RCTRL:
            girl.Bubble()
            #girl.Bubble_destroy()
    @staticmethod
    def do(girl):
        girl.frame=(girl.frame+1)%8
        girl.timer-=1
        #if girl.timer==0:
            #girl.add_event(SLEEP_TIMER)
    @staticmethod
    def draw(girl):
        if girl.dir==1:
            girl.R_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)
        else:
            girl.L_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)
# fill here
class RunState:
    @staticmethod
    def enter(girl, event):
        if event == RIGHT_DOWN:
            girl.velocity += 1
        elif event == LEFT_DOWN:
            girl.velocity -= 1
        elif event == RIGHT_UP:
            girl.velocity -= 1
        elif event == LEFT_UP:
            girl.velocity += 1
        elif event == UP_DOWN:
                girl.y_velocity += 1
        elif event == DOWN_DOWN:
                girl.y_velocity -= 1
        elif event == UP_UP:
                girl.y_velocity -= 1
        elif event == DOWN_UP:
                girl.y_velocity += 1

        girl.dir = girl.velocity
        girl.y_dir= girl.y_velocity

    @staticmethod
    def exit(girl, event):
        if event==RCTRL:
            girl.Bubble()

        pass
    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 8
        girl.timer -= 1
        girl.x += girl.velocity
        girl.x = clamp(25, girl.x, 800 - 25)
        girl.y+= girl.y_velocity
        girl.y = clamp(25, girl.y, 600 - 25)
    @staticmethod
    def draw(girl):
        if girl.velocity == 1:
            girl.R_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)
        else:
            girl.L_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)

        if girl.y_velocity==1:
           girl.Up_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)
        elif girl.y_velocity==-1 or 0:
            girl.Down_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)

class DashState:
    @staticmethod
    def enter(girl,event):
        girl.frame=0
        girl.time=0
        girl.speed=5
    @staticmethod
    def exit(girl, event):
        pass
    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 8
        girl.time=(girl.time+1)%75
        if girl.time==0:
            girl.speed=1
        girl.x+=girl.velocity*girl.speed
        girl.x = clamp(25, girl.x, 800 - 25)
    @staticmethod
    def draw(girl):
        if girl.velocity == 1:
            girl.R_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)
        else:
            girl.L_image.clip_draw(girl.frame * 44, 0, 44, 62, girl.x, girl.y)
     #SLEEP_TIMER: SleepState
next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_DOWN:RunState,UP_UP:RunState,DOWN_DOWN:RunState,DOWN_UP:RunState,
                DASH_RDOWN: IdleState, DASH_RUP: IdleState,
                DASH_LDOWN: RunState, DASH_LUP: RunState,
                RCTRL:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_DOWN: IdleState, UP_UP: IdleState, DOWN_DOWN: IdleState, DOWN_UP: IdleState,
               DASH_RDOWN: DashState, DASH_RUP: RunState, DASH_LDOWN: DashState, DASH_LUP: RunState,
               RCTRL:RunState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                DASH_RDOWN: RunState, DASH_RUP: RunState, DASH_LDOWN: RunState, DASH_LUP: RunState,
                RCTRL:IdleState},
   # SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, }
}


class Girl:

    def __init__(self):
        self.x, self.y = 800 // 2,250
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
        self.frame=0
        self.timer=0
        self.event_que=[]
        self.cur_state=IdleState
        self.cur_state.enter(self,None)


    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def Bubble(self):
        bubble=Bubble(self.x,self.y)
        game_world.add_object(bubble,1)

    def add_event(self, event):
        self.event_que.insert(0,event)

    def update(self):

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass


    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)'
                       % get_time(),(255, 255, 0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if(event.type,event.key) in key_event_table:
            key_event=key_event_table[(event.type,event.key)]
            self.add_event(key_event)


    def stop(self):
        self.velocity=0