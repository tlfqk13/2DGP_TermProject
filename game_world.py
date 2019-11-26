
# layer 0: Background Objects
# layer 1: character
# layer 2 : Bubble
# layer 3 : item, wall
# layer 4 : Bubble_destroy
# layer 5 :  box
# layer 6 : bubble_death
# layer 7 : bubble_death_motion

objects = [[],[],[],[],[],[],[],[]]
object2=[[],[],[],[],[],[],[]]

def add_object(o, layer):
    objects[layer].append(o)
def add_objetct_stage2(o,layer):
    object2[layer].append(o)

def add_objects(l, layer):
    objects[layer] += l

def get_layer(layer):
    return objects[layer]

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    for o in all_objects():
        del o
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

