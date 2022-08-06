class Message:
    def __init__(self, is_done, from_who, to_who, what, where):
        self.from_who = from_who
        self.to_who = to_who
        self.what = what
        self.where = where

class Component:
    def __init__(self, components, update_transformations, auto_update_transformations):
        self.components = components
        self.trigger_update_transformations = update_transformations
        self.auto_update_transformations = auto_update_transformations

    def update(self, beings):
        for key, function in self.auto_update_transformations.items():
            if key == "starve":
                function(self.components["fed"])