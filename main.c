#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ml6.h"
#include "display.h"
#include "draw.h"

int main() {

  screen s;
  color c;
 
  
  c.red = 0;
  c.green = MAX_COLOR;
  c.blue = 0;
  
  clear_screen(s);

  int x = 0;
	
  for (x = 0; x < XRES; x+=10) { 
    c.red = x/2;
    c.green = x/3;
    c.blue = x/4;
    
    draw_line(0, 0, x, YRES, s, c);
  }

  display(s);
  save_extension(s, "lines.png");
}  
