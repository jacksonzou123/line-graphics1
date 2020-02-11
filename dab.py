from display import *
from draw import *

s = new_screen()
c = [ 255, 165, 0 ]

draw_line(150, 20 , 290, 346, s, c) #body
draw_line(210, 160, 320, 160, s, c) #one leg
draw_line(320, 160, 260, 20, s, c)

draw_line(280, 323, 390, 323, s, c)

draw_line(285, 335, 150, 430, s, c)
draw_line(390, 323, 315, 376, s, c)

draw_line(250, 363, 330, 329, s, c)
draw_line(250, 363, 284, 443, s, c)
draw_line(330, 329, 364, 409, s, c)
draw_line(284, 443, 364, 409, s, c)

save_ppm(s, "dab.ppm")
save_extension(s, "dab.png")
