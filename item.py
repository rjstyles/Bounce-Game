from rectangle import Rectangle

class Item:
    def __init__(self, code, y, x, canvas):
        self.type = code
        self.collider = Rectangle(y, x, 7)
        self.ySpeed = 2
        self.xSpeed = 0
        self.id = canvas.create_oval(-7, -7, 7, 7, fill="white", width=1)
        self.canvas = canvas