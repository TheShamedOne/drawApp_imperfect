import tkinter as tk
from tkinter import colorchooser
import brush
import canvas

def create_toolbar(parent, cv):
    """Create the toolbar with all controls."""
    
    # Create buttons
    brush_color_btn = tk.Button(parent, text="Brush Color", 
                              command=lambda: change_brush_color())
    background_color_btn = tk.Button(parent, text="Background Color", 
                                   command=lambda: change_background_color(cv))
    
    # Create size slider
    brush_size = tk.Scale(parent, from_=1, to=100, length=500,
                         label="Brush Size", command=change_brush_size)
    brush_size.set(5)  # Default size
    
    # Layout widgets
    brush_color_btn.grid(column=0, row=0)
    background_color_btn.grid(column=0, row=1) 
    brush_size.grid(column=0, row=2)
    
    # Set defaults
    brush.change_size(brush_size.get())
    brush.change_color("#000000")  # Default: black

def change_brush_color():
    """Use colorchooser to set brush color."""
    rgb_hex = colorchooser.askcolor()
    if rgb_hex[1]:  # Check if not cancelled
        brush.change_color(rgb_hex[1])

def change_background_color(cv):
    """Use colorchooser to set canvas background."""
    rgb_hex = colorchooser.askcolor()
    if rgb_hex[1]:  # Check if not cancelled
        canvas.change_background_color(cv, rgb_hex[1])

def change_brush_size(new_size):
    """Update brush size from slider."""
    brush.change_size(int(new_size))