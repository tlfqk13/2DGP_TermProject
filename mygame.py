import game_framework
import pico2d

import world_build_state as main_state

pico2d.open_canvas()
game_framework.run(main_state)
pico2d.close_canvas()

