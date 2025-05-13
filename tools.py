import tkinter as tk
from tkinter import colorchooser

class ToolBar:
    def __init__(self, parent, canvas, brush):
        self.parent = parent
        self.canvas = canvas
        self.brush = brush
        self._create_widgets()

    def _create_widgets(self):
        """Create all toolbar widgets"""
        # Brush color button
        self.brush_color_btn = tk.Button(
            self.parent, 
            text="Brush Color", 
            command=self.change_brush_color
        )
        self.brush_color_btn.grid(column=0, row=0)

        # Background color button  
        self.bg_color_btn = tk.Button(
            self.parent,
            text="Background Color",
            command=self.change_background_color
        )
        self.bg_color_btn.grid(column=0, row=1)

        # Brush size slider
        self.brush_size = tk.Scale(
            self.parent,
            from_=1,
            to=100,
            length=500,
            label="Brush Size",
            command=self.change_brush_size
        )
        self.brush_size.set(5)  # Default size
        self.brush_size.grid(column=0, row=2)

    def change_brush_color(self):
        """Use color chooser to set brush color"""
        rgb_hex = colorchooser.askcolor()
        color_hex = rgb_hex[1]
        self.brush.change_color(color_hex)

    def change_background_color(self):
        """Use color chooser to set canvas background"""
        rgb_hex = colorchooser.askcolor()
        color_hex = rgb_hex[1]
        self.canvas.change_background_color(color_hex)

    def change_brush_size(self, new_size):
        """Sets brush size to slider value"""
        self.brush.change_size(int(new_size))

    def get_brush_size(self):
        """Get current brush size value"""
        return self.brush_size.get()