from circle import Circle
import item
import random
import resourceManager
import pyglet

class Ball:
    def __init__(self, canvas, img, paddle, bricks, score, items, itemImg):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.breakCount = 0
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_image(-9, -9, image=img, anchor='nw')
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        #print(start)
        self.collider = Circle(471, self.canvas.coords(paddle.id)[0] + 50, 9)
        self.collider.setSpeed(-start[0], start[0])
        self.canvas.move(self.id, self.collider.x, self.collider.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.items = items
        self.itemImg = itemImg

    def brick_hit(self):
        for brick in self.bricks:
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

                # 확률적 아이템 생성
                if random.randint(0, 2) == 0: # 1/3 확률로
                    self.items.append(item.Item(0, brick.collider.getMidY(), brick.collider.getMidX(), self.canvas, self.itemImg, self.paddle))

                breakSound = pyglet.media.load(resourceManager.break_sound)
                breakSound.play()

                # brick 없애기
                brick.destroy()
    
        
    def paddle_hit(self):
        if self.collider.ySpeed <= 0:
            return False
        paddle_pos = self.canvas.coords(self.paddle.id)
        if self.collider.x >= paddle_pos[0] and self.collider.x <= paddle_pos[2]:
            if self.collider.y + self.collider.radius >= paddle_pos[1] and self.collider.y + self.collider.radius <= paddle_pos[3]:
                barSound = pyglet.media.load(resourceManager.bartouch_sound)
                barSound.seek(0.25)
                barSound.play()
                return True
            return False
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
            wallSound = pyglet.media.load(resourceManager.walltouch_sound)
            wallSound.play()
        if self.collider.x + self.collider.radius >= self.canvas_width:
            self.collider.xSpeed = -abs(self.collider.xSpeed)
            wallSound = pyglet.media.load(resourceManager.walltouch_sound)
            wallSound.play()
        if self.paddle_hit():
            self.collider.ySpeed = -abs(self.collider.ySpeed)

    def getBreakCount(self):
        return self.breakCount
    def setBreakCount(self, num):
        self.breakCount = num
    def moveTo(self, y, x):
        dy = y - self.collider.y
        dx = x - self.collider.x
        self.canvas.move(self.id, dx, dy)
        self.collider.y = y
        self.collider.x = x