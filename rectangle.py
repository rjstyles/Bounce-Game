class Rectangle:
    def __init__(self, y, x, halfLength):
        self.left = x - halfLength
        self.right = x + halfLength
        self.top = y - halfLength
        self.bottom = y + halfLength
    def destroy(self):
        self.left = -9999
        self.right = -9999
        self.top = -9999
        self.bottom = -9999