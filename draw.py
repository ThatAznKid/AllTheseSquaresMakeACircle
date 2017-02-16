from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if x0 > x1: #swap places
        temp1 = x0
        temp2 = y0
        x0 = x1
        y0 = y1
        x1 = temp1
        y1 = temp2
    try:
        slope = (y1 - y0) / (x1 - x0)
    except:
        if y1 > y0:
            x = x0
            y = y0
            A = y1 - y0
            B = -(x1 - x0)
            d = A + 2 * B
            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B
            pass            
        else:
            x = x0
            y = y0
            A = y1 - y0
            B = -(x1 - x0)
            d = A - 2 * B
            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B
                pass
        return
    if 0 <= slope <= 1:
         x = x0
         y = y0
         A = y1 - y0
         B = -(x1 - x0)
         d = 2 * A + B
         while x < x1:
             plot(screen, color, x, y)
             if d > 0:
                 y += 1
                 d += 2 * B
             x += 1
             d += 2 * A
         pass

    elif slope > 1:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = A + 2 * B
        while y < y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B
        pass
    elif -1 <= slope < 0:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = 2 * A - B
        while x < x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
        pass
    else:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = A - 2 * B
        while y > y1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
        pass
