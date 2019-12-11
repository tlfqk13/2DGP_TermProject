import game_framework


# Object List
ObjLst = []

# Object
LstMap = []
LstPlayer = []
LstPlayerPet = []
LstPlayerBullet = []
LstMonster = []
LstMonsterBullet = []
LstItem = []
LstEffect = []
LstUI = []


ObjLst.append(LstPlayer)

ObjLst.append(LstMap)
ObjLst.append(LstMonster)
ObjLst.append(LstMonsterBullet)
ObjLst.append(LstItem)
ObjLst.append(LstEffect)
ObjLst.append(LstUI)

Event = 0

# GameObject Render
def draw():
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            GameObj.draw()

    pass


# KeyInput Event
def handle_events():
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            GameObj.handle_events()
    pass


# GameObject Update
def update():
    global Event
    global ObjLst

    for List in ObjLst:
        # num = len(List)
        # print(num)
        for GameObj in List:
            Event = GameObj.update()

            # 게임 오브젝트 사망시 제거.
            if Event == -1:
                List.remove(GameObj)
                del GameObj

    # CollisionMgr
    global LstPlayer
    global LstMonster
    global LstPlayerBullet
    global LstItem

    pass


# GameObject Render
def update():
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            GameObj.draw()

    pass


# GameObject Clear
def All_Delete_GameObject():
    global ObjLst

    # for List in ObjLst:
    #     for GameObj in List:
    #         List.remove(GameObj)
    #         del GameObj
    #         pass

    pass

# GameObject Add
def add_gameobject(GameObject, ObjID):
    global LstPlayer
    global LstPlayerPet
    global LstPlayerBullet
    global LstMonster
    global LstMonsterBullet
    global LstItem
    global LstEffect
    global LstUI

    if ObjID == "Player":
        LstPlayer.append(GameObject)

    if ObjID == "Map":
        LstMap.append(GameObject)
        pass

    if ObjID == "Monster":
        LstMonster.append(GameObject)
        pass

    if ObjID == "MonsterBullet":
        LstMonsterBullet.append(GameObject)
        pass

    if ObjID == "Item":
        LstItem.append(GameObject)
        pass

    if ObjID == "Effect":
        LstEffect.append(GameObject)

    if ObjID == "UI":
        LstUI.append(GameObject)

