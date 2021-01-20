import math
from rectangle import Rectangle

class Circle:
    def __init__(self, y, x, radius):
        self.y = y
        self.x = x
        self.radius = radius
        self.ySpeed = 0
        self.xSpeed = 0
    def checkCollisionWithRectangle(self, rect): # 다른 사각형과 충돌하는지 체크

        success = False
        '''
        ry = rect.top
        rx = rect.left
        dist = math.sqrt((ry - self.y) * (ry - self.y) + (rx - self.x) * (rx - self.x))
        if dist < self.radius:
            success = True
        
        ry = rect.top
        rx = rect.right
        dist = math.sqrt((ry - self.y) * (ry - self.y) + (rx - self.x) * (rx - self.x))
        if dist < self.radius:
            success = True
        
        ry = rect.bottom
        rx = rect.left
        dist = math.sqrt((ry - self.y) * (ry - self.y) + (rx - self.x) * (rx - self.x))
        if dist < self.radius:
            success = True
        
        ry = rect.bottom
        rx = rect.right
        dist = math.sqrt((ry - self.y) * (ry - self.y) + (rx - self.x) * (rx - self.x))
        if dist < self.radius:
            success = True
        '''
        sx = self.x - self.radius
        sy = self.y
        if rect.left <= sx and sx <= rect.right and rect.top <= sy and sy <= rect.bottom:
            success = True
        
        sx = self.x + self.radius
        sy = self.y
        if rect.left <= sx and sx <= rect.right and rect.top <= sy and sy <= rect.bottom:
            success = True
        
        sx = self.x
        sy = self.y - self.radius
        if rect.left <= sx and sx <= rect.right and rect.top <= sy and sy <= rect.bottom:
            success = True
        
        sx = self.x
        sy = self.y + self.radius
        if rect.left <= sx and sx <= rect.right and rect.top <= sy and sy <= rect.bottom:
            success = True
        
        return success

    def setSpeed(self, ySpeed, xSpeed): # 스피드 설정
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
    def update(self, id, canvas):
        self.y += self.ySpeed
        self.x += self.xSpeed
        canvas.move(id, self.xSpeed, self.ySpeed)