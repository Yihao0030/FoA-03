from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.beehives = []

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.beehives = hive_list
    
    def add_beehive(self, hive: Beehive):
        self.beehives.append(hive)
    
    def harvest_best_beehive(self):
        """
        Harvest the best beehive, and return the number of emeralds harvested.
        """
        res = 0
        best = None

        for i in range(len(self.beehives)):
            if min(self.beehives[i].capacity, self.beehives[i].volume)*self.beehives[i].nutrient_factor > res:
                res = min(self.beehives[i].capacity, self.beehives[i].volume)*self.beehives[i].nutrient_factor
                best = i

        if self.beehives[best].capacity > self.beehives[best].volume:
            self.beehives[best].volume = 0
            return res
        else:
            self.beehives[best].volume -= self.beehives[best].capacity
            return res