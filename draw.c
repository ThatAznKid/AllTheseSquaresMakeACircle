#include <stdio.h>
#include <stdlib.h>

#include "ml6.h"
#include "display.h"
#include "draw.h"

//Insert your line algorithm here
void draw_line(int x0, int y0, int x1, int y1, screen s, color c) {

  int dy = y1 - y0;
  int dx = x0 - x1;
  int D = (2 * dy) + dx;

  int x = x0;
  int y = y0;
  
  while (x < x1) {
    plot(s, c, x, y);
    if (D > 0) {
      y++;
      D += 2 * dx;
    }
    x++;
    D += 2 * dy;
  }

}

