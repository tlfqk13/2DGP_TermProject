import objectMgr
import random
import item
import math
import boy



def check_Collsion(Dst,Src):
    Distance = math.sqrt(pow(Dst.x - Src.x, 2) + pow(Dst.y - Src.y, 2))
    Sum_Radius = Dst.radius + Src.radius

    if Distance <= Sum_Radius:
        return True
    else:
        return False
    pass


#monster&Player 충돌

def collision_monster_player(DstList,SrcList):
    for Dst in DstList:
        for Src in SrcList:
            if check_Collsion(Dst,Src) :
                return True
    return False


def collision_monster_PlayerBubble(DstList,SrcList,Player):

    for Dst in DstList:
        for Src in SrcList:
            if check_Collsion(Dst,Src):
                Src.DeadObject()

                Dst.hp-=Src.damage

            if Dst.hp <= 0:
                Dst.IsDead = True
                Player.exp += Dst.exp

def collision_player_Item(DstList,SrcList):

    for Dst in DstList:
        for Src in SrcList:
            if check_Collsion(Dst, Src):
                # Item 제거.
                Src.IsDead = True
                # Item == Coin01
                if Src.filename == "item_coin0.png":
                    Dst.coin_cnt += 1
                elif Src.filename == "item_coin1.png":
                    Dst.coin_cnt += 10
                elif Src.filename == "item_coin2.png":
                    Dst.coin_cnt += 50
                elif Src.filename == "item_coin3.png":
                    Dst.coin_cnt += 100

                # Item
                if Src.filename == "item_magnet.png":
                    player.bIsMagnet = True
                    player.time_magnet = 0.0

                if Src.filename == "item_dualshot.png":
                    player.bIsBulletPowerUp = True
                    player.time_bullet_power_up = 0.0

                if Src.filename == "item_egg.png":
                    player.pet_cnt += 1

                if Src.filename == "item_invincible.png":
                    player.bIsLaser = True
                    player.time_laser = 0.0

                pass
    pass
