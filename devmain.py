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
        self.textObject = OnscreenText(text='Abdulaziz, Aryan, Aryan', pos=(0, -0.7), scale=0.035, fg=(1,1,1,1))
        self.index = 0
        self.cases= [1,20,10,200,100,10000,50000,140,40,95279,132492,344205,387040,428219,542097,40449479,1041649,2973512,77454227,75761114,77484283,44811,79546,8331151]
        self.cases.sort()
        self.locations = [(20, 74, 8),(20, 74, 8),(7.32384, 83.0931, -21.9361),(-58.9405, 77.6933, 8),(-5.54144, 83.5459, 4),(-0.551874, 89.3768, 11.1167),(0,0,0),(38.1309, 92.2387, 6),(0,0,0),(0,0,0),(13.8376, 89.0417, 2),(0,0,0),(13.8376, 89.0417, 2),(-6, 82, 10),(30.3025, 79.8459, 4),(13.8376, 89.0417, 2),(0,0,0),(-74.525, 73.5155, 0), (0,0,0),(0, 21.5453, -59.4061),(-26, 70, 10), (6, 85.605, -36.3569),(4.03577, 92.0972, 10),(0,0,0)]
        self.rotations = [(0, 0, 0),(0,0,0),(-40, 50, 2.65647e-06),(-56, 0, 0),(-60, 0, 0),(-46, -28, -1.93392e-06),(0, 0, 0),(74.0001, 0, 0),(0, 0, 0),(0, 0, 0),(4.00003, 0, 0),(0, 0, 0),(4.00003, 0, 0),(0, 0, 0),(36, 0, 0),(4.00003, 0, 0),(0, 0, 0),(-67.9999, 0, 0),(0, 0, 0),(0, 42, 0),(0, 0, 0),(0, 62, 0),(54, 0, 0),(0,0,0)]
        self.locations[22] = (-2, 90, 10)
        self.rotations[22] = (0,0,0)
        self.texts = ["December 21 2019 \n Wuhan Municipal Health Commission, China, reported a cluster of cases of pneumonia of unknown cause in Wuhan, Hubei Province. A novel coronavirus was eventually identified. \n \n There was no evidence at the time stating that the virus was contagious. The Huanan Seafood wholesale market closed down the next day.","January 11 2020 \n a 61-year-old man died just after one of China's biggest holidays,\n when hundreds of millions of people travel across the country.","January 14 2020 \nThe first case of the novel coronavirus was found in Thailand, this is the first outside China. Within a week later, South Korea, Japan and\n the United States has detected its first case.","January 21 2020 \n Three additional cases of what is now the 2019 novel coronavirus are reported in Thailand and Japan,\n causing the CDC to begin screenings at JFK International, San Francisco International, and Los Angeles International airports.\n A Washington state resident becomes the first person in the United States with a confirmed case of the coronavirus","January 23 2020 \n Trains and planes stopped leaving and entering the city. \n Subways, buses and ferries stopped operating; the city was in lockdown.","January 29 2020 \n First case in the UAE, also the first case in the middle east, 73 y/o chinese woman","31 January 2020 \n The World Health Organization declared a 'public health emergency of international concern'. The Trump administration restricted travel from China the next day. "," February 7 2020 \n Dr. Li Wenliang, a Chinese doctor, died after contracting the coronavirus,\n he was hailed as a hero by many for trying to ring early alarms that infections could spin out of control. \n In early January, the authorities reprimanded him, and he was forced to sign a statement denouncing his warning \nDr. Li’s death provoked anger and frustration at how the Chinese government mishandled the situation.","February 11 2020 \n The W.H.O. proposed an official name for the disease the virus causes: COVID-19, an acronym that stands for coronavirus disease 2019. The name makes no reference\n to any of the people, places, or animals associated with the coronavirus, given the goal to avoid stigma.","February 24 2020 \n South Korea, Iran, China, Italy, Singapore, Japan and Hong Kong experience a massive spike of cases at the time,\n Travelers in the UAE that were in the mentioned countries within the last 28 days must isolate. The UAE had 13 cases at the time. \n \n China had 77,658 cases of COVID-19 and a death toll of 2,663. ","March 4 2020 \n The UAE announces that schools would be closed for 4 weeks, \nthe first 2 to be the spring break \nand the last two would be online learning, online learning has later been extended to the end of the academic year. ","March 12 2020 \n World health organisation declares COVID-19  a pandemic  and trump declares COVID-19 a national emergency, unlocking billions of dollars to fund the fight for this disease.\n Travel ban on non-US citizens to enter the country","March 22 2020\n 11 day sterilization in the UAE","March 23 2020\n The initial announcement, however, was done by Boris Johnson, with agreement from the other three heads of government. At 8:30 p.m. on 23 March 2020,\n The British population was instructed to stay home, except for exercise once a day (such as running, walking or cycling), shopping for essential items, any medical need,\n providing care to a vulnerable person, or travelling to work where the work in question was vital and could not be done from home.","24 March 2020 \nthe Government of India under Prime Minister Narendra Modi ordered a nationwide lockdown for 21 days.","March 26 2020\n UAE introduces Night curfew","April 2 2020\n World COVID-19 cases cross 1 million cases, with at least 51,000 people killed due to the virus.","April 26 2020 \n 24 days later, the total death toll for COVID-19 passed 200,000.","October 19 2020 \n COVID-19 cases topped 40 million worldwide\n more than 1.1 million people had been killed by the virus worldwide","June 17 2020\n WHO announced that the hydroxychloroquine arm of the Solidarity trial to find an effective COVID-19 treatment was being stopped. \nThe decision was based on the fact that hydroxychloroquine did not reduce mortality for hospitalised COVID-19 patients.","December 11 2020 \n The FDA approved a vaccine from Pfizer for emergency use. ","December 18 2020 \nNational authorities in South Africa announced the detection of a new variant of SARS-CoV-2 rapidly spreading in three provinces of South Africa.\n South Africa named this variant 501Y.V2, because of a N501Y mutation.","December 21 2020 \n UK announces a new strain of COVID-19 which is more contagious","THE END \n THE PANDEMIC \n DIRECTORS - ABDULAZIZ, ARYAN, ARYAN"]
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
            "print": False,
            "rotate_l": False,
            "rotate_r": False
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

        self.accept("]", self.updateKey, ["rotate_l", True])
        self.accept("]-up", self.updateKey, ["rotate_l", False])

        self.accept("[", self.updateKey, ["rotate_r", True])
        self.accept("[-up", self.updateKey, ["rotate_r", False])

        self.updateTask = taskMgr.add(self.update, "update")


    def updateKey(self, key, value):
        self.keymap[key] = value
    def checkColor(self):
        if self.cases[self.index] > 100:
            self.map.setColor(0.4, 0.2, 0.2, 0.5)
        if self.cases[self.index] > 1000:
            self.map.setColor(0.7, 0.1, 0.1, 0.5)
        if self.cases[self.index] > 10000:
            self.map.setColor(0.7, 0, 0, 0.5)
        if self.cases[self.index] > 100000:
            self.map.setColor(0.9, 0, 0, 0.5)
        if self.cases[self.index] > 1000000:
            self.map.setColor(1.0, 0, 0, 0.5)

    def update(self,task):
        if self.keymap["RIGHT"]:
            self.index +=1
            self.camera.setPos(self.locations[self.index])
            self.camera.setHpr(self.rotations[self.index])
            self.checkColor()
            self.textObject.text = "Worldwide cases: " + str(self.cases[self.index]) + "\n" + self.texts[self.index]
            time.sleep(0.2)
        if self.keymap["LEFT"]:
            self.index -=1
            self.camera.setPos(self.locations[self.index])
            self.checkColor()
            self.camera.setHpr(self.rotations[self.index])
            self.textObject.text = "Worldwide cases: " + str(self.cases[self.index]) + "\n" + self.texts[self.index]

            time.sleep(0.2)

        if self.keymap["forward"]:
            self.camera.setY(self.camera, 2)
        if self.keymap["back"]:
            self.camera.setY(self.camera, -2)

        if self.keymap["right"]:
            self.camera.setX(self.camera, 2)
        if self.keymap["left"]:
            self.camera.setX(self.camera, -2)

        if self.keymap["up"]:
            self.camera.setZ(self.camera, 2)
        if self.keymap["down"]:
            self.camera.setZ(self.camera, -2)

        if self.keymap["rotate_l"]:
            self.camera.setH(self.camera, 2)
        if self.keymap["rotate_r"]:
            self.camera.setH(self.camera, -2)

        if self.keymap["print"]:
            print(self.index)
            print("POSITION:")
            print(self.camera.getPos())
            print("ROTATION:")
            print(self.camera.getHpr())
        return task.cont

app = myApp()
app.run()