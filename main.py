import tkinter as tk
import canvas
import tools

def main():
    # Create main window
    root = tk.Tk()
    
    # Create frames
    draw_window = tk.Frame(root)
    draw_window.grid(column=0, row=0)
    
    tool_window = tk.Frame(root)
    tool_window.grid(column=1, row=0)
    
    # Create canvas 
    cv = canvas.setup_canvas(draw_window)
    cv.grid(column=0, row=0)
    
    # Create toolbar
    tools.create_toolbar(tool_window, cv)
    
    # Start application
    root.mainloop()

if __name__ == "__main__":
    main()