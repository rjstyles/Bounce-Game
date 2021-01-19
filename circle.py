class Circle:
    def __init__(self, y, x, radius):
        self.y = y
        self.x = x
        self.radius = radius
    def checkCollisionWithCircle(self, anotherCircle): # 다른 원과 충돌하는지 체크
        dx = self.x - anotherCircle.x
        dy = self.y - anotherCircle.y
        self.radius + anotherCircle.radius