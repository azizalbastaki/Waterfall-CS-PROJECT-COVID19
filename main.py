from direct.showbase.ShowBase import ShowBase

class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.map = self.loader.loadModel("map.bam")
        base.set_background_color(0,0,0)
        self.map.setH(90)
        self.map.setR(-90)
        self.map.setY(100)
        self.map.reparentTo(self.render)
app = myApp()
app.run()