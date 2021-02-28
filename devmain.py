from direct.showbase.ShowBase import ShowBase
from events import COVID_EVENTS
class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.map = self.loader.loadModel("map.bam")
        base.set_background_color(0,0,0)
        self.events = COVID_EVENTS(self.camera)
        self.disableMouse()
        self.map.setH(90)
        self.map.setR(-90)
        self.map.setY(100)
        self.map.reparentTo(self.render)
        self.keymap = {
            "RIGHT": False,
            "LEFT": False,
            "forward": False,
            "back": False,
            "right": False,
            "left": False,
            "up": False,
            "down": False,
            "lup": False,
            "ldown": False,
            "print": False
        }
        self.accept("arrow_up", self.updateKey, ["lup", True])
        self.accept("arrow_up-up", self.updateKey, ["lup", False])

        self.accept("arrow_down", self.updateKey, ["ldown", True])
        self.accept("arrow_down-up", self.updateKey, ["ldown", False])

        self.accept("arrow_right", self.updateKey, ["RIGHT",True])
        self.accept("arrow_right-up", self.updateKey, ["RIGHT",False])

        self.accept("arrow_left", self.updateKey, ["LEFT", True])
        self.accept("arrow_left-up", self.updateKey, ["LEFT", False])

        self.accept("w",self.updateKey,["forward",True])
        self.accept("w-up",self.updateKey,["forward",False])

        self.accept("a", self.updateKey, ["left", True])
        self.accept("a-up", self.updateKey, ["left", False])

        self.accept("s", self.updateKey, ["back", True])
        self.accept("s-up", self.updateKey, ["back", False])

        self.accept("d", self.updateKey, ["right", True])
        self.accept("d-up", self.updateKey, ["right", False])

        self.accept("r", self.updateKey, ["up", True])
        self.accept("r-up", self.updateKey, ["up", False])

        self.accept("f", self.updateKey, ["down", True])
        self.accept("f-up", self.updateKey, ["down", False])

        self.accept("p", self.updateKey, ["print", True])
        self.accept("p-up", self.updateKey, ["print", False])

        self.updateTask = taskMgr.add(self.update, "update")


    def updateKey(self, key, value):
        self.keymap[key] = value
    def update(self,task):
        if self.keymap["forward"]:
            self.camera.setY(self.camera, 2)
        if self.keymap["back"]:
            self.camera.setY(self.camera, -2)
        if self.keymap["left"]:
            self.camera.setX(self.camera, -2)
        if self.keymap["right"]:
            self.camera.setX(self.camera, 2)
        if self.keymap["up"]:
            self.camera.setZ(self.camera, 2)
        if self.keymap["down"]:
            self.camera.setZ(self.camera, -2)
        if self.keymap['LEFT']:
            self.camera.setH(self.camera, -2)
        if self.keymap["RIGHT"]:
            self.camera.setH(self.camera, 2)
        if self.keymap["RIGHT"]:
            self.camera.setH(self.camera, 2)
        if self.keymap["RIGHT"]:
            self.camera.setH(self.camera, 2)
        if self.keymap["lup"]:
            self.camera.setP(self.camera, 2)
        if self.keymap["ldown"]:
            self.camera.setP(self.camera, -2)
        if self.keymap["print"]:
            print("POSITION:")
            print(self.camera.getPos())
            print("ROTATION:")
            print(self.camera.getHpr())
        return task.cont

app = myApp()
app.run()