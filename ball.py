from circle import Circle
import random

class Ball:
    def __init__(self, canvas, color, paddle, bricks, score):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_oval(-7, -7, 7, 7, fill=color, width=1)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        #print(start)
        self.collider = Circle(460, 240, 7)
        self.collider.setSpeed(-start[0], start[0])
        self.canvas.move(self.id, self.collider.x, self.collider.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

    def brick_hit(self):
        for brick_line in self.bricks:
            for brick in brick_line:
                if self.collider.checkCollisionWithRectangle(brick.collider):
                    ## 이곳에 블럭 충돌시 발생하는 이벤트 삽입



                    self.hit += 1
                    self.score.configure(text="Score: " + str(self.hit))
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

    def draw(self):
        prevY = self.collider.y
        prevX = self.collider.x
        pos = self.canvas.coords(self.id)
        
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        self.collider.update()
        self.brick_hit()
        if self.collider.y - self.collider.radius <= 0:
            self.collider.ySpeed = abs(self.collider.ySpeed)
        if self.collider.y + self.collider.radius >= self.canvas_height: # 아래로 떨어진 경우
            self.bottom_hit = True
        if self.collider.x - self.collider.radius <= 0:
            self.collider.xSpeed = abs(self.collider.xSpeed)
        if self.collider.x + self.collider.radius >= self.canvas_width:
            self.collider.xSpeed = -abs(self.collider.xSpeed)
        if self.paddle_hit():
            self.collider.ySpeed = -abs(self.collider.ySpeed)
        self.canvas.move(self.id, self.collider.x -  prevX, self.collider.y - prevY)
        

        