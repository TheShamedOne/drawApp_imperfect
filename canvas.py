import tkinter as tk

class Canvas:
    def __init__(self, parent, bg_color="#03fc17", height=800, width=800):
        self.canvas = tk.Canvas(parent, bg=bg_color, height=height, width=width)
        self.lastx = None
        self.lasty = None
        self._setup_bindings()

    def _setup_bindings(self):
        """Set up mouse event bindings"""
        self.canvas.bind("<Button-1>", self.dot)  
        self.canvas.bind("<B1-Motion>", self.draw)

    def grid(self, **kwargs):
        """Expose the grid geometry manager"""
        self.canvas.grid(**kwargs)

    def configure(self, **kwargs):
        """Expose the configure method of the canvas"""
        self.canvas.configure(**kwargs)

    def create_line(self, *args, **kwargs):
        """Expose the create_line method of the canvas"""
        self.canvas.create_line(*args, **kwargs)

    def save_position(self, event):
        """Save the last position of the mouse."""
        self.lastx, self.lasty = event.x, event.y

    def draw(self, event):
        """Draw a line from last position to current position"""
        from .brush import b_color, b_width # Import here to avoid circular import
        
        self.create_line(
            self.lastx, 
            self.lasty, 
            event.x, 
            event.y, 
            fill=b_color, 
            width=b_width, 
            capstyle=tk.ROUND, 
            joinstyle=tk.BEVEL
        )
        self.save_position(event)

    def dot(self, event):
        """Draw a circle from event"""
        self.save_position(event)
        self.draw(event)

    def change_background_color(self, color_hex):
        """Changes background color"""
        self.configure(background=color_hex)