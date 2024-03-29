from pico2d import *
import random
import game_framework

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

time_CreateBullet = 0.0
time_UpdateCreateBullet = 0.2


class Boss:
    def __init__(self, Target=None):
        self.IsDead = False
        self.frame = 0
        self.x, self.y = 360,400
        self.scaleX, self.scaleY = 300, 256
        self.speed = 100
        self.radius = 128
        self.hp = 10000
        self.max_hp = self.hp
        self.exp = 1000
        self.dir=1
        self.font=load_font('ENCR10B.TTF', 16)

        if Target is not None:
            self.target = Target
        else:
            self.target = None

        self.image = load_image("resource/Boss01.png")
        self.image_HpBarEmpty = load_image("resource/MonsterHpBarEmpty_0.png")
        self.image_HpBar = load_image("resource/MonsterHpBar_0.png")

        # HpBar 변수.
        self.hpRadio = 0.0
        self.originCX = 116
        self.hpCX = 116.0
        self.hpCY = 12
        self.hpPosX = self.x

        pass

    def handle_Events(self):
        pass

    def update(self):
        if self.IsDead:
            return -1


        # Animation
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        # Move
        if self.y >570:
            self.y -= self.speed * game_framework.frame_time

        # Hp Ratio
        self.hpRadio = self.hp / self.max_hp
        self.hpCX = self.originCX * self.hpRadio
        self.hpPosX = self.x - (self.originCX - self.hpCX) / 2

        # Create Bullet
        #self.CreateBullet()

        if self.x>550:
            self.dir=-1
        if self.x<100:
            self.dir=1
        self.x+=self.dir*5

        return 0
        pass


    def draw(self):
        if not self.IsDead:
            self.image.clip_draw(int(self.frame) * 300, 0, 300, 256, self.x, self.y, self.scaleX, self.scaleY)

            #self.image_HpBarEmpty.clip_draw(0, 0, 116, 12, self.x, self.y - 140)
            #self.image_HpBar.clip_draw(0, 0, int(self.hpCX), self.hpCY, self.hpPosX, self.y - 140)
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x-55,self.y+50, '(HP: %3.2f)' % self.hp, (255, 255, 0))

    def get_hp(self):
        return self.hp

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

