import collections
# Definir a un grafo simple
class SimpleGraph:
    # un diccionario que contiene cada nodo y los vecinos
    # No contiene peso en los 'edges'
    def __init__(self):
        self.edges = {}
    def neighbors(self,id):
        return self.edges[id]

# Definir el Queue
class Queue:
    # Fila de evaluacion
    # Vacia, agrega o elimina los valores de espera
    def __init__(self):
        self.elements = collections.deque()
    def empty(self):
        return len(self.elements) == 0
    def put(self,x):
        return self.elements.append(x)
    def get(self):
        return self.elements.popleft()

# Ejemplo de evaluación Depth Breath First
example_graph =  SimpleGraph()
example_graph.edges = {
    'A':['B'],
    'B':['A','C','D'],
    'C':['A'],
    'D':['A','E'],
    'E':['B']}

def breath_first_search(graph,start):
    # Imprimir lo que vemos
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r"%current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

breath_first_search(example_graph,'A')
