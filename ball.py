from circle import Circle
import random

class Ball:
    def __init__(self, canvas, color, paddle, bricks, score):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.breakCount = 0
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_oval(-7, -7, 7, 7, fill=color, width=1)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        #print(start)
        self.collider = Circle(480, 240, 7)
        self.collider.setSpeed(-start[0], start[0])
        self.canvas.move(self.id, self.collider.x, self.collider.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

    def brick_hit(self):
        for brick_line in self.bricks:
            for brick in brick_line:
                if self.collider.checkCollisionWithRectangle(brick.collider):
                    ## 이곳에 블럭 충돌시 발생하는 이벤트 삽입

                    # 충돌 위치에 따른 x 또는 y속도 반전
                    rect = brick.collider
                    rectMidX = rect.left + (rect.right - rect.left) / 2
                    rectMidY = rect.top + (rect.bottom - rect.top) / 2
                    distY = abs(rectMidY - self.collider.y)
                    distX = abs(rectMidX - self.collider.x)
                    if distX > distY:
                        self.collider.xSpeed = -self.collider.xSpeed
                    else :
                        self.collider.ySpeed = -self.collider.ySpeed

                    # 없앤 공 수 증가
                    self.breakCount += 1

                    # brick 없애기
                    brick.destroy()
    
        
    def paddle_hit(self):
        if self.collider.ySpeed <= 0:
            return False
        paddle_pos = self.canvas.coords(self.paddle.id)
        if self.collider.x >= paddle_pos[0] and self.collider.x <= paddle_pos[2]:
            if self.collider.y + self.collider.radius >= paddle_pos[1] and self.collider.y + self.collider.radius <= paddle_pos[3]:
                #print("paddle hit")
                return True
            return False

    def update(self):
        prevY = self.collider.y
        prevX = self.collider.x
        pos = self.canvas.coords(self.id)
        
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        self.collider.update(self.id, self.canvas) # 현재의 x, y값을 x, y스피드만큼 증가
        self.brick_hit() # 벽돌과 충돌체크
        if self.collider.y - self.collider.radius <= 0:
            self.collider.ySpeed = abs(self.collider.ySpeed)
        if self.collider.y + self.collider.radius >= self.canvas_height: # 아래로 떨어진 경우
            self.bottom_hit = True
            self.canvas.delete(self.id)
        if self.collider.x - self.collider.radius <= 0:
            self.collider.xSpeed = abs(self.collider.xSpeed)
        if self.collider.x + self.collider.radius >= self.canvas_width:
            self.collider.xSpeed = -abs(self.collider.xSpeed)
        if self.paddle_hit():
            self.collider.ySpeed = -abs(self.collider.ySpeed)

    def getBreakCount(self):
        return self.breakCount
    def setBreakCount(self, num):
        self.breakCount = num