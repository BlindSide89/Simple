__author__ = 'Fabian'

from igraph import *
import random

class Cascade(object):

    def __init__(self):
        self.x = 1

    def doCascades(self):
        g = Graph.Famous("Coxeter") #Coxeter
        #g = Graph.Erdos_Renyi(n=10, m=13)
        #g = Graph([(0,1), (0,2), (0,3), (1,2), (2,3), (1,3), (0,4), (4,5), (5,6), (6,4)])


        g.vs["innovation"] = ["old"]
        g.vs["willAdapt"] = ["no"]


        l = len(g.vs.indices)
        r = random.randint(0, l-1)
        g.vs[r]["innovation"] = "new"
        g.es[g.adjacent(g.vs[r])]["color"] = "green"

        color_dict = {"old": "red", "new": "green"}
        g.vs["color"] = [color_dict[gender] for gender in g.vs["innovation"]]
        layout = g.layout("kk")
        plot(g, './coexed.png', layout=layout)


        for p in range(0, 5):
            for x in range(0, len(g.vs.indices)):       #Im ersten Schritt werden alle Knoten überprüft ob sie 'wechseln'
                if g.vs[x]["innovation"] == "old":      #Wenn ein Knoten noch die Innovation old hat wird die Adapt Funktion aufgerufen
                    self.willAdapt(g, x, 0.3)

            for x in range(0, len(g.vs.indices)):       #Erst im zweiten Schritt wechseln die Knoten dann tatsächlich.
                if g.vs[x]["willAdapt"] == "yes":       #Wechselt ein Knoten werden seine Attribute angepasst
                    g.vs[x]["innovation"] = "new"
                    g.vs[x]["color"] = "green"
                    g.es[g.adjacent(g.vs[x])]["color"] = "green"        #Alle adjazenten Kanten des wechselnden Knotens werden ebenfalls eingefärbt

            #g.vs["color"] = [color_dict[gender] for gender in g.vs["innovation"]]
            plot(g, './coexed' + p.__str__() + '.png', layout=layout)


    def willAdapt(self, graph: Graph, vertice: int, condition):

        adaptiveNeighbors = 0
        nbor = graph.neighbors(vertice)


        for y in range(0, len(nbor)):
            if graph.vs[nbor[y]]["innovation"] == "new":
                adaptiveNeighbors += 1

        adaptives = adaptiveNeighbors/len(nbor)  ####DIVIDE BY ZERO
        if adaptives >= condition:
            graph.vs[vertice]["willAdapt"] = "yes"
        else:
            graph.vs[vertice]["willAdapt"] = "no"