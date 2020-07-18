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

# Algoritmo de búsqueda
def depth_first_search_2(graph,start,goal):
    # Return came_from
    frontier = Queue()
    frontier.put(start) # Vector que analizar los puntos a evaluar
    came_from = {} # Diccionario que evalúa los puntos de donde viene
    came_from[start] = None # Punto anterior
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
            # Dibujar funcionamiento del algoritmo
            # draw_grid(g,width =2,point_to=came_from,start=(8,7),goal=goal)
            # time.sleep(0.01)
            # print("\n\n\n")
    return came_from



g = SquareGrid(30,15)
g.walls = DIAGRAM1_WALLS # Long List
# draw_grid(g)
parents = depth_first_search_2(g,(8,7),(9,0))
draw_grid(g,width =2,point_to=parents,start=(8,7),goal=(9,0))
