from implementation import *
import time

class SquareGrid:
    # Ancho y largo de la grilla
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.walls = []
    # Verificar si el id está dentro de la grilla
    def in_bounds(self,id):
        (x,y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    # Si es posible pasar por ahí
    def passable(self,id):
        return id not in self.walls
    # Definir los vecinos del punto
    def neighbors(self,id):
        (x,y) = id
        results = [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]
        if (x+y) % 2 == 0:
            results.reverse() # Solo por aesthethics
        results = filter(self.in_bounds,results)
        results = filter(self.passable,results)
        return results

class GridWithWeights():
    def __init__(self,width,height):
        super().__init__(width,height)
        self.weights = {}
    def cost(self,from_node,to_node):
        return self.weights.get(to_node,1)
