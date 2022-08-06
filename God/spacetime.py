from God.beings import Beings

class SpaceTime:
    def __init__(self, gods_thoughts):
        self.width = gods_thoughts.spacetime_width
        self.height = gods_thoughts.spacetime_height
        self.beings = Beings(gods_thoughts)
        """self.positions = {}
        self.map_beings_to_positions()

    def map_beings_to_positions(self):
        for being in self.beings.beings:
            self.positions[(being.components["x"], being.components["y"])] = being"""

    def update(self, SuperMetaGod_message):
        self.beings.update(self.beings, SuperMetaGod_message)

    def render(self, map):
        for i in range(self.height):
            map.append(['.' for i in range(self.width)])
        self.beings.render(map)