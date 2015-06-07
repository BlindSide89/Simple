__author__ = 'Fabian'

from igraph import *
import random

class Cascade(object):

    def __init__(self):
        self.x = 1

    def doCascades(self, g: Graph, seedNum=2, threshold=0.3):

        for x in g.vs:
            x["innovation"] = "old"
            x["color"] = "red"
            x["willAdapt"] = "no"
        for e in g.es:
            e["color"] = "black"

        l = len(g.vs.indices)
        index = 0
        while index < seedNum:
            r = random.randint(0, l-1)
            if not g.vs[r]["innovation"] == "new":
                g.vs[r]["innovation"] = "new"
                g.vs[r]["color"] = "green"
                g.es[g.adjacent(g.vs[r])]["color"] = "green"
                index += 1
            print("HUUUUI")
        graphlayout = g.layout("drl")
        plot(g, './cascade.png', layout=graphlayout)

        flag = True
        int_name = 0
        while flag:
            counter = 0
            for x in range(0, len(g.vs.indices)):       #Im ersten Schritt werden alle Knoten überprüft ob sie 'wechseln'
                if g.vs[x]["innovation"] == "old":      #Wenn ein Knoten noch die Innovation old hat wird die Adapt Funktion aufgerufen
                    counter += self.willAdapt(g, x, threshold)
            if counter == 0:
                flag = False
                continue
            for x in range(0, len(g.vs.indices)):       #Erst im zweiten Schritt wechseln die Knoten dann tatsächlich.
                if g.vs[x]["willAdapt"] == "yes":       #Wechselt ein Knoten werden seine Attribute angepasst
                    g.vs[x]["innovation"] = "new"
                    g.vs[x]["color"] = "green"
                    g.es[g.adjacent(g.vs[x])]["color"] = "green"        #Alle adjazenten Kanten des wechselnden Knotens werden ebenfalls eingefärbt

            plot(g, './cascade' + int_name.__str__() + '.png', layout=graphlayout)
            int_name += 1
        return int_name

    def willAdapt(self, graph: Graph, vertice: int, condition):

        adaptiveNeighbors = 0
        nbor = graph.neighbors(vertice)

        for y in range(0, len(nbor)):
            if graph.vs[nbor[y]]["innovation"] == "new":
                adaptiveNeighbors += 1

        adaptives = adaptiveNeighbors/len(nbor)  ####DIVIDE BY ZERO
        if adaptives >= condition:
            graph.vs[vertice]["willAdapt"] = "yes"
            return 1
        else:
            graph.vs[vertice]["willAdapt"] = "no"
            return 0


    def createRandomGraph(self, vnum: int, limit: int=0):
        g = Graph()
        for i in range(0, vnum):
            g.add_vertex(innovation="old", color="red", willAdapt="no")
            if i == 0:
                continue

            r = random.randint(0, i-1)
            g.add_edge(r, i)
            if i >= 3:
                r = random.randint(0, i-1)
                if g.get_eid(r, i, directed=False, error=False) == -1:
                    g.add_edge(r, i)

        plot(g, "current.png", layout=g.layout("drl"))
        return g

    def printGraph(self, graph):
        plot(graph, "current.png", layout=graph.layout("drl"))


