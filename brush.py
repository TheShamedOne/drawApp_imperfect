class Brush:
    def __init__(self, initial_color="#000000", initial_width=5):
        self.b_color = initial_color
        self.b_width = initial_width

    def change_size(self, value: int):
        """Change the brush width"""
        self.b_width = value

    def change_color(self, hex_value: str):
        """Change the brush color"""
        self.b_color = hex_value