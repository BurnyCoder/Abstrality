from God.physical_reality import PhysicalReality
from Technical.random_gen import RandomGen


class GodsThoughts:
    spacetime_width = 20
    spacetime_height = 20
    randomness = RandomGen()


class God:
    def __init__(self):
        self.gods_thoughts = GodsThoughts()
        self.physical_reality = PhysicalReality(self.gods_thoughts)

    def act(self, SuperMetaGod_message):
        self.physical_reality.update(SuperMetaGod_message)

    def render(self):
        map = []
        self.physical_reality.render(map)
        for row in map:
            for point in row:
                print(point, end=" ")
            print("\n", end=" ")
