from rectangle import Rectangle

class Bricks:
    def __init__(self, canvas, color, y, x):
        self.color = color
        self.canvas = canvas
        self.id = canvas.create_oval(-10, -10, 10, 10, fill=color, width=2)
        self.collider = Rectangle(y, x, 10)
        canvas.move(self.id, x, y)
    def destroy(self):
        self.collider.destroy()
        self.canvas.delete(self.id)