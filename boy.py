from pico2d import *

# Boy Event
RIGHT_DOWN,LEFT_DOWN,RIGHT_UP,LEFT_UP,UP_UP,DOWN_DOWN,UP_DOWN,DOWN_UP,\
    DASH_LDOWN,DASH_LUP,DASH_RDOWN,DASH_RUP,\
    LCTRL=range(13)

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
    (SDL_KEYDOWN,SDLK_LCTRL):LCTRL
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
        boy.timer=1000
    @staticmethod
    def exit(boy,event):
        if event==LCTRL:
            boy.bomb()
        pass
    @staticmethod
    def do(boy):
        boy.frame=(boy.frame+1)%8
        boy.timer-=10
        #if boy.timer==0:
            #boy.add_event(SLEEP_TIMER)
    @staticmethod
    def draw(boy):
        if boy.dir==1:
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
        else:
            boy.L_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
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
        if event==LCTRL:
            boy.bomb()
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
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
        else:
            boy.L_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)

        if boy.y_velocity==1:
           boy.Up_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
        elif boy.y_velocity==-1 or 0:
            boy.Down_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)


class SleepState:
    @staticmethod
    def enter(boy,event):
        boy.frame = 0
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:boy.L_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
        else:
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)

class DashState:
    @staticmethod
    def enter(boy, event):
        boy.frame=0
        boy.time=0
        boy.speed=5
    @staticmethod
    def exit(boy, event):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.time=(boy.time+1)%75
        if boy.time==0:
            boy.speed=1
        boy.x+=boy.velocity*boy.speed
        boy.x = clamp(25, boy.x, 800 - 25)
    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.R_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
        else:
            boy.L_image.clip_draw(boy.frame * 44, 0, 44, 62, boy.x, boy.y)
     #SLEEP_TIMER: SleepState
next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_DOWN:RunState,UP_UP:RunState,DOWN_DOWN:RunState,DOWN_UP:RunState,
                DASH_RDOWN: IdleState, DASH_RUP: IdleState,
                DASH_LDOWN: RunState, DASH_LUP: RunState,
                LCTRL:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_DOWN: IdleState, UP_UP: IdleState, DOWN_DOWN: IdleState, DOWN_UP: IdleState,
               DASH_RDOWN: DashState, DASH_RUP: RunState, DASH_LDOWN: DashState, DASH_LUP: RunState,
               LCTRL:RunState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                DASH_RDOWN: RunState, DASH_RUP: RunState, DASH_LDOWN: RunState, DASH_LUP: RunState,
                LCTRL:IdleState},
   # SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, }
}


class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2,250
        self.L_image = load_image('Left.png')
        self.R_image=load_image('Right.png')
        self.Up_image=load_image('Up.png')
        self.Down_image=load_image('Down.png')
        self.dir = 1
        self.y_dir=1
        self.vector_y=250
        self.velocity = 0
        self.y_velocity=0
        self.frame=0
        self.timer=0
        # fill here
        self.event_que=[]
        self.cur_state=IdleState
        self.cur_state.enter(self,None)

    def update_state(self):
        if len(self.event_que)>0:
            event=self.event_que.pop()
            self.cur_state.exit(self.event)
            self.cur_state=next_state_table[self.cur_state][event]
            self.cur_state.enter(self.event)
    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0,event)
        pass


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
        pass


    def handle_event(self, event):
        if(event.type,event.key) in key_event_table:
            key_event=key_event_table[(event.type,event.key)]
            self.add_event(key_event)
        pass

    def bomb(self):
        print('bomb')