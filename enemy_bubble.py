from pico2d import *
import random
import game_world
import game_framework
from bubble_destroy import Bubble_destroy
from boy_death import Death
from boy_death_motion import Death_Motion
from boy import Boy

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Enemy_bubble:
    image=None
    b_image=None

    def __init__(self):
      self.frame=0
      self.image = load_image('resource/bubble_121.png')
      self.x,self.y=random.randint(100,600),random.randint(200,600)

      self.timer=300
      self.dir=1
      self.speed=random.randint(5,25)

    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def draw(self):
        self.frame=(self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%4
        self.image.clip_draw(int(self.frame)*40,0,40,68,self.x,self.y)
        draw_rectangle(*self.get_bb())

    def collide(self,a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def update(self):
        if self.y >120:
            self.y -= self.speed

        if self.y<100:
            pass

        if self.x>550:
            self.dir=-1
        if self.x<100:
            self.dir=1
        self.x+=self.dir*2
        #self.y-=self.dir*5



        self.timer-=1
        if (self.timer==0):
          game_world.remove_object(self)
          global bubble_destroys
          bubble_destroys=Bubble_destroy(self.x,self.y)
          game_world.add_object(bubble_destroys,4)
          bubble_destroysList=game_world.get_layer(4)
          game_world.remove_object(self)
          boyList=game_world.get_layer(1)
          boxList=game_world.get_layer(5)


          for i in range(len(bubble_destroysList)):
           if self.collide(boyList[0],bubble_destroysList[i]):
               print("collision1")
               global boy_death
               boy_death=Death(self.x,self.y)
               game_world.add_object(boy_death,6)
               game_world.remove_object(boyList[0])

          '''
          for i in range(len(boxList)):
           #game_world.add_object(bubble_destroys,4)
           if self.collide(bubble_destroysList[0],boxList[i]) :
                print("collsion2")
                game_world.remove_object(boxList[i])
                break

'''






