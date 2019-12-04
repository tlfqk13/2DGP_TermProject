from pico2d import *
from bubble import Bubble


import game_world

# Boy Event
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

# Boy States
class IdleState:
    @staticmethod
    def enter(boy,event):
        if event ==RIGHT_DOWN:
            boy.velocity+=1
        elif event==LEFT_DOWN:
            boy.velocity-=1
        elif event==RIGHT_UP:
            boy.velocity-=1
        elif event==LEFT_UP:
            boy.velocity+=1
        if event ==UP_DOWN:
            boy.y_velocity+=1
        elif event==DOWN_DOWN:
            boy.y_velocity-=1
        elif event==UP_UP:
            boy.y_velocity-=1
        elif event==DOWN_UP:
            boy.y_velocity+=1

    @staticmethod
    def exit(boy,event):
        if event==KEY_BUBBLE:
            boy.Bubble()
        if event==KEY_ITEM:
            pass
            #boy.Bubble_destroy()
    @staticmethod
    def do(boy):
        boy.frame=(boy.frame+1)%8
        boy.timer-=1
        #if boy.timer==0:
            #boy.add_event(SLEEP_TIMER)
    @staticmethod
    def draw(boy):
        if boy.dir==1:
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)
        else:
            boy.L_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)
# fill here
class RunState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == UP_DOWN:
                boy.y_velocity += 1
        elif event == DOWN_DOWN:
                boy.y_velocity -= 1
        elif event == UP_UP:
                boy.y_velocity -= 1
        elif event == DOWN_UP:
                boy.y_velocity += 1

        boy.dir = boy.velocity
        boy.y_dir= boy.y_velocity

    @staticmethod
    def exit(boy, event):
        if event==KEY_BUBBLE:
            boy.Bubble()

        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        boy.y+= boy.y_velocity
        boy.y = clamp(25, boy.y, 600 - 25)
    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)
        else:
            boy.L_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)

        if boy.y_velocity==1:
           boy.Up_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)
        elif boy.y_velocity==-1 or 0:
            boy.Down_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)

class DashState:
    @staticmethod
    def enter(boy, event):
       pass
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def do(boy):
      pass
    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)
        else:
            boy.L_image.clip_draw(boy.frame * 44, 0, 44, 52, boy.x, boy.y)
     #SLEEP_TIMER: SleepState
next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_DOWN:RunState,UP_UP:RunState,DOWN_DOWN:RunState,DOWN_UP:RunState,
                DASH_RDOWN: IdleState, DASH_RUP: IdleState,
                DASH_LDOWN: RunState, DASH_LUP: RunState,
                KEY_BUBBLE:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_DOWN: IdleState, UP_UP: IdleState, DOWN_DOWN: IdleState, DOWN_UP: IdleState,
               DASH_RDOWN: DashState, DASH_RUP: RunState, DASH_LDOWN: DashState, DASH_LUP: RunState,
               KEY_BUBBLE:RunState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                DASH_RDOWN: RunState, DASH_RUP: RunState, DASH_LDOWN: RunState, DASH_LUP: RunState,
                KEY_BUBBLE:IdleState},
   # SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, }
}


class Boy:

    def __init__(self):
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
        self.speed=1
        self.frame=0
        self.timer=0
        self.event_que=[]
        self.cur_state=IdleState
        self.cur_state.enter(self,None)

    def __getstate__(self):
        state = {'x' : self.x, 'y' : self.y, 'dir' : self.dir,
                 'cur_state' : self.cur_state}
        return state

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
        game_world.add_object(bubble,2)


    def add_event(self, event):
        self.event_que.insert(0,event)

    def update(self):

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def get_boy(self):
        return object[1]

    def get_boyX(self):
        return self.x

    def get_boyY(self):
        return self.y

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

         if(self.dir==1):
             self.velocity=1

    def boy_speed(self):
        pass