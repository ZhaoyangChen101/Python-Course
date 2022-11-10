try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

import math


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h, color='red'):
    # create_oval needs coordinates of top left and bottom right of a bounding rectangle
    page.create_oval(g - radius, h - radius, g + radius, h + radius, outline=color, fill='')
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100  # 这个很巧妙-如何将range来循环小数。
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)



def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')
    # locals()返回该function内的所有变量。
    print(locals())


# canvas 没有画点的方法，可以用长度为一的线来表示。
def plot(canvas, x_coordinate, y_coordinate):
    canvas.create_line(x_coordinate, -y_coordinate, x_coordinate + 1, -y_coordinate - 1, fill='red')


main_window = tkinter.Tk()

main_window.title("Parabola")
main_window.geometry("640x480")

canvas1 = tkinter.Canvas(main_window, width=640, height=480)
canvas1.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(main_window, width=320, height=480, background="pink")
# canvas2.grid(row=0, column=1)
#
# print(repr(canvas1), repr(canvas2))
draw_axes(canvas1)
# draw_axes(canvas2)

parabola(canvas1, 100)
parabola(canvas1, 200)

circle(canvas1, 100, 100, 100, 'green')
circle(canvas1, 100, 100, -100, 'orange')
circle(canvas1, 100, -100, 100, 'black')
circle(canvas1, 100, -100, -100, 'blue')
circle(canvas1, 10, 30, 30)
circle(canvas1, 10, 30, -30)
circle(canvas1, 10, -30, 30)
circle(canvas1, 10, -30, -30)
circle(canvas1, 30, 0, 0)


main_window.mainloop()
