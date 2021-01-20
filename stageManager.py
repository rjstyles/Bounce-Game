import random

class BrickRaw:
    def __init__(self, y, x, brickType):
        self.y = y
        self.x = x
        self.brickType = brickType # 현재는 색상을 구분, 추후에 어떤 타입으로 구분할지 토론
        
class StageManager:
    def __init__(self):
        self.stageNumber = 1 # 스테이지 최대 횟수 지정(미구현, 아직은 항상 1스테이지에서 끝남)
        self.stages = []
        
        # 1스테이지
        currentStage = []
        for i in range(0, 5):
            for j in range(0, 15):
                currentStage.append(BrickRaw(32 * i + 15, 32 * j + 15, random.randint(0, 17))) # y위치, x위치, 타입(현재는 색상을 의미)
        self.stages.append(currentStage) # 스테이지 목록에 추가

        # 2스테이지(예시)
        # y=300, x=300이고 블럭타입 1인 블럭 하나만 존재.
        currentStage = [] # BrickRaw가 들어갈 목록
        currentStage.append(BrickRaw(300, 300, 1)) # y위치, x위치, 타입(현재는 색상을 의미함)
        self.stages.append(currentStage) # 스테이지 목록에 추가

        # 3스테이지
        currentStage = [] # BrickRaw가 들어갈 목록
        # 여기에 스테이지의 구성을 입력합니다.
        self.stages.append(currentStage) # 스테이지 목록에 추가



    def getStage(self, num):
        return self.stages[num]