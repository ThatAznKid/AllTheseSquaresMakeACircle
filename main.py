from display import *
from draw import *

screen = new_screen()
color = [ 255, 0, 255 ]

#making intial square
draw_line ( screen, 100, 100, 100, 300, color )
draw_line ( screen, 100, 300, 300, 300, color )
draw_line ( screen, 300, 300, 300, 100, color )
draw_line ( screen, 300, 100, 100, 100, color )

#making second square 
draw_line ( screen, 150, 150, 150, 350, color )
draw_line ( screen, 150, 350, 350, 350, color )
draw_line ( screen, 350, 350, 350, 150, color )
draw_line ( screen, 350, 150, 150, 150, color )

#completing cube
draw_line ( screen, 100, 100, 150, 150, color )
draw_line ( screen, 100, 300, 150, 350, color )
draw_line ( screen, 300, 300, 350, 350, color )
draw_line ( screen, 300, 100, 350, 150, color )


display(screen)
save_extension(screen, 'img.png')
