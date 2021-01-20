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

root = Tk()
root.title("Bounce")
root.geometry("500x570")
root.resizable(0, 0)
#root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)

brickImg = Image.open(resourceManager.bubble)
brickImg = brickImg.resize((32, 32), Image.ANTIALIAS)
brickImg = ImageTk.PhotoImage(brickImg)

ballImg = Image.open(resourceManager.mainball)
ballImg = ballImg.resize((18, 18), Image.ANTIALIAS)
ballImg = ImageTk.PhotoImage(ballImg)

bgImage = ImageTk.PhotoImage(file=resourceManager.bgImage)
canvas.create_image(0, 0, image=bgImage, anchor='nw')
score = Label(height=50, width=80, text="Score: 00", font=resourceManager.font)
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
        canvas.delete("all")
        try:
            bgMusic.play()
        except:
            pass
        canvas.create_image(0, 0, image=bgImage, anchor='nw')
        paddle = Paddle(canvas, resourceManager.bar)
        bricks = []
        
        stageMgr = stageManager.StageManager()
        bricksRaw = stageMgr.getStage(currentStage)
        totalBrick = len(bricksRaw)
        for b in bricksRaw:
            bricks.append(Bricks(canvas, brickImg, b.y, b.x))
        
        balls = [Ball(canvas, ballImg, paddle, bricks, score)]

        #ball = Ball(canvas, BALL_COLOR[1], paddle, bricks, score)
        #ball.collider.setSpeed(-3.2, -4)
        #balls.append(ball)
        
        #ball = Ball(canvas, BALL_COLOR[2], paddle, bricks, score)
        #ball.collider.setSpeed(-3.6, -3)
        #balls.append(ball)
        
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