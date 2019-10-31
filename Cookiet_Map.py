from pico2d import *
import os

os.getcwd()
os.chdir('C:\\2DGP\\2DGP_TermProject')

open_canvas(850,650)

cookie_tile00=load_image('cookie_tile_00.png')
cookie_tile01=load_image('cookie_tile_01.png')
cookie_block_02=load_image('cookie_block_03.png')
cookie_object_00=load_image('cookie_object_01.png')
ui_mainexit=load_image('ui_mainexit.png')
character=load_image('unit_118.png')

tile_list_x=[]
tile_list_y=[]

for i in range(25,1000,50):
    tile_list_x.append(i)

for i in range(25,1000,60):
    tile_list_y.append(i)

oddlist=tile_list_x[0::2]
evenlist=tile_list_x[1::2]


idx=0
dir=0
print(tile_list_x)
print(tile_list_y)
frame=0
x=800/2
running=True
arrow=2

while(running):
    for i in range(0,8+1):
        for idx in range(0,17+1):
         cookie_tile00.draw_now(oddlist[i],tile_list_x[idx])
         cookie_tile01.draw_now(evenlist[i],tile_list_x[idx])
         #cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[idx],925)
         #cookie_block_02.clip_draw(0,60,60,70,tile_list_x[idx],625)
         #cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[idx],25)
        for k in range(1,6):
            cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k], 275)
            cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k], 175)
            cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k], 75)
        for z in range(1,5):
            cookie_block_02.clip_draw(0,60,60,70,75,tile_list_x[z])
            #cookie_block_02.clip_draw(0, 60, 60, 70, 175, tile_list_x[z])
            cookie_block_02.clip_draw(0, 60, 60, 70, 275, tile_list_x[z])

        for idx_1 in range(1,3):
            cookie_object_00.draw_now(oddlist[idx_1],225)
            cookie_object_00.draw_now(oddlist[idx_1],125)


        for k_1 in range(1, 6):
          cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1], 575)
          cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1], 475)
          cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1], 375)

        for z_1 in range(8, 11):
          cookie_block_02.clip_draw(0, 60, 60, 70, 75, tile_list_x[z_1])
          # cookie_block_02.clip_draw(0, 60, 60, 70, 175, tile_list_x[z])
          cookie_block_02.clip_draw(0, 60, 60, 70, 275, tile_list_x[z_1])

        for idx_2 in range(1, 3):
          cookie_object_00.draw_now(oddlist[idx_2], 525)
          cookie_object_00.draw_now(oddlist[idx_2], 425)


        for k_1 in range(8, 12):
         cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1], 575)
         cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1], 475)
         cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1], 375)
        for z_1 in range(1, 6):
         cookie_block_02.clip_draw(0, 60, 60, 70, 375, tile_list_x[z_1])
         # cookie_block_02.clip_draw(0, 60, 60, 70, 175, tile_list_x[z])
         cookie_block_02.clip_draw(0, 60, 60, 70, 575, tile_list_x[z_1])

        for idx_2 in range(4,6):
         cookie_object_00.draw_now(oddlist[idx_2], 525)
         cookie_object_00.draw_now(oddlist[idx_2], 425)

        for k_1 in range(8, 11):
         cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1],275)
         cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1],175)
         cookie_block_02.clip_draw(0, 60, 60, 70, tile_list_x[k_1],75)

        for z_1 in range(7, 12):
         cookie_block_02.clip_draw(0, 60, 60, 70, 375, tile_list_x[z_1])
         # cookie_block_02.clip_draw(0, 60, 60, 70, 175, tile_list_x[z])
         cookie_block_02.clip_draw(0, 60, 60, 70, 575, tile_list_x[z_1])

        for idx_2 in range(4,6):
         cookie_object_00.draw_now(oddlist[idx_2], 225)
         cookie_object_00.draw_now(oddlist[idx_2], 125)



