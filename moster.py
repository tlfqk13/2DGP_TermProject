from pico2d import *
import random
import game_framework

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class CMonster:
    image = [None, None, None]
    image_HpBar = None
    image_HpBarEmpty = None

    def __init__(self, PosX, PosY, ScaleX, ScaleY, Hp, Speed, Radius, Exp, FileName):
        if CMonster.image[0] is None:
            CMonster.image[0] = load_image("Resource/Monster/Enemy01.png")

        if CMonster.image[1] is None:
            CMonster.image[1] = load_image("Resource/Monster/Enemy02.png")

        if CMonster.image[2] is None:
            CMonster.image[2] = load_image("Resource/Monster/Enemy03.png")

        if CMonster.image_HpBarEmpty is None:
            CMonster.image_HpBarEmpty = load_image("Resource/UI/MonsterHpBarEmpty_2.png")

        if CMonster.image_HpBar is None:
            CMonster.image_HpBar = load_image("Resource/UI/MonsterHpBar_2.png")

        self.IsDead = False
        self.frame = random.randint(0, 3)
        self.x, self.y = PosX, PosY
        self.scaleX, self.scaleY = ScaleX, ScaleY
        self.speed = Speed
        self.radius = Radius
        self.hp = Hp
        self.max_hp = self.hp
        self.exp = Exp
        self.filename = FileName

        # HpBar 변수.
        self.hpRadio = 0.0
        self.originCX = 70
        self.hpCX = 70.0
        self.hpCY = 11
        self.hpPosX = self.x

        pass

    def handle_events(self):
        pass

    def update(self):
        global Lst_CoinLottery

        if self.IsDead:
            return -1

        # Animation
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        # Move
        self.y = self.y - self.speed * game_framework.frame_time

        # OffSet
        if self.y <= 0:
            self.IsDead = True
            pass

        # Check Hp
        if self.hp <= 0:
            self.hp = 0
            self.IsDead = True

        # Hp Ratio
        self.hpRadio = self.hp / self.max_hp
        self.hpCX = self.originCX * self.hpRadio
        self.hpPosX = self.x - (self.originCX - self.hpCX) / 2

        return 0


        pass

    def draw(self):
        index = 0

        if self.filename == "Enemy01.png":
            index = 0
        elif self.filename == "Enemy02.png":
            index = 1
        elif self.filename == "Enemy03.png":
            index = 2

        if not self.IsDead:
            CMonster.image[index].clip_draw(int(self.frame) * 76, 0, 76, 51, self.x, self.y, self.scaleX, self.scaleY)

            CMonster.image_HpBarEmpty.clip_draw(0, 0, 72, 10, self.x, self.y - 50)
            CMonster.image_HpBar.clip_draw(0, 0, int(self.hpCX), self.hpCY, self.hpPosX, self.y - 50)
        pass

    def deadObject(self):
        self.IsDead = True
        pass

    pass
