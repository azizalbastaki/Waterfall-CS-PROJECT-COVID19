class COVID_EVENTS():
    def __init__(self, camera):
        self.camera = camera
    def move(self,x,y,z):
        self.camera.setPos(x,y,z)
    def rotate(self,h,p):
        self.camera.setP(p)
        self.camera.setH(h)

    def moverot(self,x,y,z,h,p,r):
        self.move(x,y,z)
        self.rotate(h,p,r)
    def event1(self):
        self.moverot(-5.54144, 83.5459, 4,-60, 0, 0)
    def event2(self):
        self.moverot(38.1309, 92.2387, 6,74.0001, 0, 0)