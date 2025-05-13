import tkinter as tk
from brush import b_color, b_width

lastx = None 
lasty = None

def save_position(event):
    """Save the last position of the mouse."""
    global lastx, lasty
    lastx, lasty = event.x, event.y

def draw(event, cv):
    """Draw a line from last position to current position."""
    cv.create_line(lastx, lasty, event.x, event.y, 
                  fill=b_color, 
                  width=b_width,
                  capstyle=tk.ROUND, 
                  joinstyle=tk.BEVEL)
    save_position(event)

def dot(event, cv):
    """Draw a circle from event."""
    save_position(event)
    draw(event, cv)

def setup_canvas(parent):
    """Create and configure the canvas."""
    cv = tk.Canvas(parent, bg="#03fc17", height=800, width=800)
    
    # Bind events
    cv.bind("<Button-1>", lambda e: dot(e, cv))
    cv.bind("<B1-Motion>", lambda e: draw(e, cv))
    
    return cv

def change_background_color(cv, color_hex):
    """Change canvas background color."""
    cv.configure(background=color_hex)