from pico2d import *

import game_world
from bubble_destroy import Bubble_destroy
from boy_death import Death
from item import Item
from boss import Boss

from boy_death_motion import Death_Motion

#from boy import Boy



class Bubble:
    image=None
    b_image=None

    def __init__(self,x=0,y=0):
      self.frame=0
      self.image = load_image('resource/bubble_116.png')
      self.x,self.y=x,y
      self.timer=200


    def collide(self,a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def draw(self):
        self.frame=(self.frame+1)%4
        self.image.clip_draw(self.frame*40,0,40,68,self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer-=1
        if (self.timer==0):
          game_world.remove_object(self)
          global bubble_destroys,boss_Hp
          bubble_destroys=Bubble_destroy(self.x,self.y)
          game_world.add_object(bubble_destroys,4)
          bubble_destroysList=game_world.get_layer(4)
          boyList=game_world.get_layer(1)
          boxList=game_world.get_layer(5)
          bossList=game_world.get_layer(1)
          #boss_Hp=Boss.get_hp()

          for i in range(len(bubble_destroysList)):
           if self.collide(boyList[0],bubble_destroysList[i]):
               print("collision1")
               global boy_death
               boy_death=Death(self.x,self.y)
               game_world.add_object(boy_death,6)
               game_world.remove_object(boyList[0])
          for i in range(len(bubble_destroysList)):
              if self.collide(bossList[1],bubble_destroysList[i]):
                 # boss_Hp-=10
                  print("collision3")



          for i in range(len(boxList)):
           #game_world.add_object(bubble_destroys,4)
           if self.collide(bubble_destroysList[0],boxList[i]) :
                print("collsion2")
                game_world.remove_object(boxList[i])
                global items
                items = Item(self.x-30,self.y)
                game_world.add_object(items, 3)
                break








