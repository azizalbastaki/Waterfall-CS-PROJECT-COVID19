from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker
class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.map = self.loader.loadModel("map.bam")
        self.map = CardMaker()
        base.set_background_color(0,0,0)
        self.map.setH(90)
        self.map.setR(-90)
        self.map.setY(100)
        self.map.reparentTo(self.render)
        self.keymap = {
            "NEXT": False,
            "PREVIOUS": False
        }

        tex = self.loader.loadTexture("1.png")
        #self.map.setTexture(tex)
        self.accept("arrow_right", self.updateKey, ["NEXT",True])
        self.accept("arrow_right-up", self.updateKey, ["NEXT",False])

        self.accept("arrow_left", self.updateKey, ["PREVIOUS", True])
        self.accept("arrow_left-up", self.updateKey, ["PREVIOUS", False])

    def updateKey(self, key, value):
        self.keymap[key] = value
        print(key)
app = myApp()
app.run()