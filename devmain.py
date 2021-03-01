from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from events import COVID_EVENTS
import time
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
        self.textObject = OnscreenText(text='Abdulaziz, Aryan, Aryan', pos=(-0.5, 0.02), scale=0.07, fg=(1,1,1,1))
        self.index = 0
        self.locations = [(-5.54144, 83.5459, 4),(38.1309, 92.2387, 6),(7.32384, 83.0931, -21.9361),(-58.9405, 77.6933, 8),(-5.54144, 83.5459, 4),(-0.551874, 89.3768, 11.1167),(0,0,0),(38.1309, 92.2387, 6),(0,0,0),(0,0,0),(13.8376, 89.0417, 2),(0,0,0),(13.8376, 89.0417, 2),(-6, 82, 10),(30.3025, 79.8459, 4),(13.8376, 89.0417, 2),(0,0,0),(-74.525, 73.5155, 0), (0,0,0),(0, 21.5453, -59.4061),(-26, 70, 10), (6, 85.605, -36.3569),(4.03577, 92.0972, 10)]
        self.rotations = [(-60, 0, 0),(74.0001, 0, 0),(-40, 50, 2.65647e-06),(-56, 0, 0),(-60, 0, 0),(-46, -28, -1.93392e-06),(0, 0, 0),(74.0001, 0, 0),(0, 0, 0),(0, 0, 0),(4.00003, 0, 0),(0, 0, 0),(4.00003, 0, 0),(0, 0, 0),(36, 0, 0),(4.00003, 0, 0),(0, 0, 0),(-67.9999, 0, 0),(0, 0, 0),(0, 42, 0),(0, 0, 0),(0, 62, 0),(54, 0, 0)]
        self.texts = ["Wuhan Municipal Health Commission, China, reported a cluster of cases of pneumonia of unknown cause in Wuhan, Hubei Province. A novel coronavirus was eventually identified. \n \n There was no evidence at the time stating that the virus was contagious. The Huanan Seafood wholesale market closed down the next day.","On January 11th, a 61-year-old man died just after one of China's biggest holidays, when hundreds of millions of people travel across the country.","The first case of the novel coronavirus was found in Thailand, this is the first outside China. Within a week later, South Korea, Japan and the United States has detected its first case.","Three additional cases of what is now the 2019 novel coronavirus are reported in Thailand and Japan, causing the CDC to begin screenings at JFK International, San Francisco International, and Los Angeles International airports. A Washington state resident becomes the first person in the United States with a confirmed case of the coronavirus","Trains and planes stopped leaving and entering the city. \n Subways, buses and ferries stopped operating; the city was in lockdown.","First case in the UAE , also the first case in the middle east , 73 y/o chinese woman","The World Health Organization declared a 'public health emergency of international concern'. The Trump administration restricted travel from China the next day. ","Dr. Li Wenliang, a Chinese doctor, died after contracting the coronavirus, he was hailed as a hero by many for trying to ring early alarms that infections could spin out of control. \n In early January, the authorities reprimanded him, and he was forced to sign a statement denouncing his warning Dr. Li’s death provoked anger and frustration at how the Chinese government mishandled the situation.","The W.H.O. proposed an official name for the disease the virus causes: Covid-19, an acronym that stands for coronavirus disease 2019. The name makes no reference to any of the people, places, or animals associated with the coronavirus, given the goal to avoid stigma.","South Korea, Iran, China, Italy, Singapore, Japan and Hong Kong experience a massive spike of cases at the time, Travelers in the UAE that were in the mentioned countries within the last 28 days must isolate. The UAE had 13 cases at the time. \n \n China had 77,658 cases of COVID-19 and a death toll of 2,663. ","The UAE announces that schools would be closed for 4 weeks, the first 2 to be the spring break and the last two would be online learning, online learning has later been extended to the end of the academic year. ","World health organisation declares COVID-19  a pandemic  and trump declares COVID-19 a national imergency, unlocking billions of dollars to fund the fight for this disease. Travel ban on non-US citizens to enter the country","11 day sterilization in the UAE",""]
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
            self.index +=1
            self.camera.setPos(self.locations[self.index])
            self.camera.setHpr(self.rotations[self.index])
            self.textObject.text = self.texts[self.index]
            time.sleep(0.1)
        if self.keymap["back"]:
            self.camera.setY(self.camera, -2)
        if self.keymap["print"]:
            print("POSITION:")
            print(self.camera.getPos())
            print("ROTATION:")
            print(self.camera.getHpr())
        return task.cont

app = myApp()
app.run()