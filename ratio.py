from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.points = []
    
    def add_point(self, item: T):
        """
        Add a point to the list and sort it.
        """

        self.points.append(item)
        self.points.sort()
    
    def remove_point(self, item: T):
        self.points.remove(item)

    def ratio(self, x, y):
        """
        Return a list of all points that:
        Larger than at least x% of the elements in the list.
        Smaller than at least y% of the elements in the list.
        """
        first = ceil(len(self.points) * (x / 100))
        last = ceil(len(self.points) * (y / 100))
        result = []
        for i in range(first, len(self.points) - last):
            result.append(self.points[i])

        return result


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
