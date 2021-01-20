from rectangle import Rectangle

class Bricks:
    def __init__(self, canvas, img, y, x):
        self.canvas = canvas
        self.id = canvas.create_image(-16, -16, image=img, anchor='nw')
        self.collider = Rectangle(y, x, 16)
        canvas.move(self.id, x, y)
    def destroy(self):
        self.collider.destroy()
        self.canvas.delete(self.id)