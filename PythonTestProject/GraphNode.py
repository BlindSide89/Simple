__author__ = 'Fabian'

#Class Test
class GraphNode(object):
        #define GraphNode
        def __init__(self):
            self.name = "Hello"
            self.edge = 0
            self.color = "blue"
            self.neighbor = 0
        def changeColor(self, newColor):
            self.color = newColor
        def newNeighbor(self, neighbor):
            self.neighbor = neighbor