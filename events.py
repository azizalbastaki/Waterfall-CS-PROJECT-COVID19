class COVID_EVENTS():
    def __init__(self, camera):
        self.camera = camera
    def move(self,x,y,z):
        self.camera.setPos(x,y,z)
    def rotate(self,h,p):
        self.camera.setP(p)
        self.camera.setH(h)

    def event1(self):
        pass