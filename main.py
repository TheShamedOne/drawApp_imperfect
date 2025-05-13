import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

import brush


def savePosn(event):
    """
    Save the last position of the mouse.
    """
    global lastx, lasty
    lastx, lasty = event.x, event.y


def draw(event):
    cv.create_line(lastx, lasty, event.x, event.y, fill=brush.b_color, width=brush.b_width, capstyle=tk.ROUND, joinstyle=tk.BEVEL)
    savePosn(event)


def dot(event):
    """
    Draw a circle from event
    """
    savePosn(event)
    draw(event)


def change_brush_color():
    """
    Uses colorchooser to get rgb values and set the brush color.
    """
    rgb_hex = colorchooser.askcolor()
    color_hex = rgb_hex[1]
    brush.change_color(color_hex)


def change_background_color():
    """
    Changes background color
    """
    rgb_hex = colorchooser.askcolor()
    color_hex = rgb_hex[1]
    cv.configure(background=color_hex)


def change_brush_size(new_size):
    """
    Sets brush size to slider value
    """
    brush.change_size(int(new_size))



root = tk.Tk()


# Create distinct frames

draw_window = tk.Frame(root)
draw_window.grid(column=0, row=0)

tool_window = tk.Frame(root)
tool_window.grid(column=1, row=0)


# create canvas

cv = tk.Canvas(draw_window, bg ="#03fc17", height=800, width=800)
cv.grid(column=0, row=0)
cv.bind("<Button-1>", dot)
cv.bind("<B1-Motion>", draw)


# create tool bar

brush_color = tk.Button(tool_window, text="Brush Color", command=change_brush_color)
brush_color.grid(column=0, row=0)
background_color = tk.Button(tool_window, text="Background Color", command=change_background_color)
background_color.grid(column=0, row=1)
brush_size = tk.Scale(tool_window, from_=1, to=100, length=500, label="Brush Size", command=change_brush_size)
brush_size.set(5)
brush_size.grid(column=0, row=2)


# set brush defaults

brush.change_size(brush_size.get())
brush.change_color("#000000") # black


# start loop

root.mainloop()