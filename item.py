from rectangle import Rectangle
from circle import Circle

class Item:
    def __init__(self, itemType, y, x, canvas, paddle):
        self.type = itemType
        self.collider = Circle(y, x, 10)
        self.collider.setSpeed(2, 0)
        self.id = canvas.create_oval(-7, -7, 7, 7, fill="white", width=1) # 나중에 이미지로 교체
        self.canvas = canvas
        self.canvas.move(self.id, x, y)
        self.dead = 0
        self.eaten = 0
        self.paddle = paddle
        self.canvas_height = canvas.winfo_height()

    def update(self):
        self.collider.update(self.id, self.canvas) # 스피드값에 따른 이동

        # 패들에 닿았을 때
        paddle_pos = self.canvas.coords(self.paddle.id)
        if self.collider.x >= paddle_pos[0] and self.collider.x <= paddle_pos[2]:
            if self.collider.y + self.collider.radius >= paddle_pos[1] and self.collider.y - self.collider.radius <= paddle_pos[3]:
                self.eaten = 1
                self.canvas.delete(self.id)

        # 내려감
        if self.collider.y > self.canvas_height:
            self.dead = 1
            self.canvas.delete(self.id)

    def isDead(self):
        return self.dead

    def isEaten(self):
        return self.eaten
        