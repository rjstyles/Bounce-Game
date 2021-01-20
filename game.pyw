from tkinter import *
import time
import random
import rankdb
from ball import Ball
from bricks import Bricks
from circle import Circle
from paddle import Paddle
import stageManager
import resourceManager
from PIL import ImageTk, Image
import pyglet
from item import Item

canvasWidth = 500
canvasHeight = 500

root = Tk()
root.title("Bounce")
root.geometry("500x570")
root.resizable(0, 0)
#root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)

brickImg = Image.open(resourceManager.bubble)
brickImg = brickImg.resize((32, 32), Image.ANTIALIAS)
brickImg = ImageTk.PhotoImage(brickImg)

ballImg = Image.open(resourceManager.mainball)
ballImg = ballImg.resize((18, 18), Image.ANTIALIAS)
ballImg = ImageTk.PhotoImage(ballImg)

bgImage = ImageTk.PhotoImage(file=resourceManager.bgImage)
canvas.create_image(0, 0, image=bgImage, anchor='nw')
score = Label(height=50, width=80, text="Score: 0", font=resourceManager.font)
score.pack(side="left")
root.update()
bgMusic = pyglet.media.load(resourceManager.bgMusic)

playing = False
breakCount = 0
totalBrick = 0
currentStage = 0

def start_game(event):
    global playing
    global breakCount
    global currentStage
    global totalBrick
    if playing is False:
        playing = True
        score.configure(text="Score: 00")
        canvas.delete("all") # 현재의 canvas 내용을 모두 지우기
        try:
            bgMusic.play()
        except:
            pass

        canvas.create_image(0, 0, image=bgImage, anchor='nw') # 배경 이미지 

        # paddle 생성(플레이어)
        paddle = Paddle(canvas, resourceManager.bar)

        # 벽돌 생성
        bricks = []
        stageMgr = stageManager.StageManager()
        bricksRaw = stageMgr.getStage(currentStage)
        totalBrick = len(bricksRaw)
        for b in bricksRaw:
            bricks.append(Bricks(canvas, brickImg, b.y, b.x))

        # 아이템 담기
        items = []
        
        # 공 생성
        balls = [Ball(canvas, ballImg, paddle, bricks, score, items)]

        root.update_idletasks()
        root.update()

        time.sleep(1)
        while 1:
            if paddle.pausec !=1:
                try:
                    canvas.delete(m)
                    del m
                except:
                    pass
                if len(balls) > 0:
                    for b in balls:
                        b.update()
                        breakCount += b.getBreakCount()
                        b.setBreakCount(0)
                        if b.bottom_hit == True:
                            balls.remove(b)
                    for i in items:
                        i.update()
                        if i.isEaten():
                            if i.type == 0:
                                b = Ball(canvas, ballImg, paddle, bricks, score, items)
                                b.collider.setSpeed(random.random() - 4, (random.random() - 0.5) * 7)
                                balls.append(b)
                            items.remove(i)
                        if i.isDead():
                            items.remove(i)
                    if breakCount == totalBrick:
                        canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Consolas 24 ")
                        root.update_idletasks()
                        root.update()
                        playing = False
                        break
                    score.configure(text="Score: " + str(breakCount))
                    paddle.draw()
                    root.update_idletasks()
                    root.update()
                    time.sleep(0.01)
                else:
                    canvas.create_text(250, 250, text="GAME OVER!!", fill="red", font="Consolas 24 ")
                    root.update_idletasks()
                    root.update()
                    playing = False
                    break
            else:
                try:
                    if m==None:pass
                except:
                    m=canvas.create_text(250, 250, text="PAUSE!!", fill="green", font="Consolas 24 ")
                root.update_idletasks()
                root.update()
        rankdb.rank(breakCount)

root.bind_all("<Return>", start_game)
canvas.create_text(250, 250, text="Press Enter to start Game!!", fill="red", font="Consolas 18")
j=canvas.find_all()
root.mainloop()