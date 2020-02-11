from display import *
from draw import *

s = new_screen()
c = [ 255, 165, 0 ]

draw_line(200, 400 ,300, 400, s, c)
draw_line(200, 300 ,300, 300, s, c)
draw_line(200, 300 ,200, 400, s, c)
draw_line(300, 300 ,300, 400, s, c)

draw_line(250, 300 ,250, 100, s, c)

save_ppm(s, "dab.ppm")
save_extension(s, "dab.png")
