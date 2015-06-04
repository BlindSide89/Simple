__author__ = 'BlindSide'
from GraphNode import *
import igraph

node = GraphNode()
node2 = GraphNode()

node2.changeColor("red")
node.newNeighbor(node2)

print(node.neighbor.color)

print(igraph.__version__)

g = igraph.Graph()

g.add_vertices(3)

g.add_edges([(0,1),(1,2)])

igraph.summary(g)

layout = g.layout("kk")

igraph.plot(g,layout = layout)

