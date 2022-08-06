from God.component import Component
from God.directions import *

#todo collision detection
def action(self, beings, SuperMetaGod_message):
    if SuperMetaGod_message == "d":
        self.components["x"] = self.components["x"] + 1
    if SuperMetaGod_message == "w":
        self.components["y"] = self.components["y"] - 1
    if SuperMetaGod_message == "a":
        self.components["x"] = self.components["x"] - 1
    if SuperMetaGod_message == "s":
        self.components["y"] = self.components["y"] + 1

class Fed:
    def __init__(self, base_line, current):
        self.base_line = base_line
        self.current = current
        self.hunger = self.base_line - self.current

def starve(fed):
    fed.current = fed.current - 0.05
    fed.hunger = fed.base_line - fed.current

def eat(fed):
    fed.current = fed.current + 0.5
    fed.hunger = fed.base_line - fed.current

class Beings:
    beings = []

    def __init__(self, gods_thoughts):
        width = gods_thoughts.spacetime_width
        height = gods_thoughts.spacetime_height
        random = gods_thoughts.randomness
        self.beings.append(Component({
            "name": "player",
            "look": "!",
            "color": (255, 255, 0),
            "x": int(width / 2),
            "y": int(height / 2),
            "is_player": True,
            "life": 10,
            "fed": Fed(1, 1)
        }, {
            "action": action,

        }, {
            "starve": starve
        }))
        self.beings.append(Component({
            "name": "food",
            "look": "Y",
            "color": (random.random_int(0, 255), random.random_int(0, 255), random.random_int(0, 255)),
            "x": int(random.random_int(5, width - 5)),
            "y": int(random.random_int(5, height - 5)),
            "is_player": False
        }, {

        }, {}))

    def update(self, beings, SuperMetaGod_message):
        for being in self.beings:
            being.update(self.beings)

            #todo optimize by having player segmented from other beings so that we dont have to search from him each iteration
            if being.components["is_player"] == True:
                being.trigger_update_transformations["action"](being, beings, SuperMetaGod_message)

    def render(self, map):
        for being in self.beings:
            map[being.components["y"]][being.components["x"]]=being.components["look"]
            if being.components["is_player"] == True:
                food = being.components["fed"].current
                map.append(f"Food = {food}")

