import tkinter as tk
from canvas import Canvas
from tools import ToolBar
from brush import Brush

def main():
    # Create main window
    root = tk.Tk()

    # Create frames
    draw_window = tk.Frame(root)
    draw_window.grid(column=0, row=0)

    tool_window = tk.Frame(root)
    tool_window.grid(column=1, row=0)

    # Initialize components
    brush = Brush()
    canvas = Canvas(draw_window)
    canvas.grid(column=0, row=0)
    toolbar = ToolBar(tool_window, canvas, brush)

    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()