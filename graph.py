from node import Node
from edge import Edge
import re
import sys

class Graph:
    def __init__(self, nodes, edges):
        self.name = 'Test'
        self.nodesAmount = nodes
        self.edgesAmount = edges
        self.nodes = []
        self.edges = []
        self.initNodes()
        self.initEdges()
        self.nodesIndex = list(range(1,nodes+1))
        self.edgesIndex = []
        self.lastEdgeIndex = 0
    def initNodes(self):
        for x in range(0, self.nodesAmount):
            self.nodes.append(Node(x+1))
    def initEdges(self):
        for x in range(0, self.edgesAmount):
            self.edges.append(Edge(x+1))
    def prepare(self):
        print("Wezly w wywolanym grafie")
        for x in range(0, self.nodesAmount):
            print(self.nodes[x].id)
        self.updateEdgeList()
        print("krawedzie w wywolanym grafie", self.edgesIndex)

    def updateEdgeList(self):
        for x in range(0, self.nodesAmount):
            self.edgesIndex = self.edgesIndex + self.nodes[x].connectionsAsList

    def addConnection(self, first, second, weight):
        if(self.lastEdgeIndex  == self.edgesAmount):
            self.edges.append(Edge(0))
            self.edgesAmount = self.edgesAmount + 1
            self.updateEdgeList()
            print('Weszłem')
        self.nodes[first-1].addConnection(second, weight)
        self.edges[self.lastEdgeIndex].firstNode = first
        self.edges[self.lastEdgeIndex].secondNode = second
        self.edges[self.lastEdgeIndex].weight = weight
        self.lastEdgeIndex = self.lastEdgeIndex + 1

    def addEdges(self, val):
        for x in range(self.edgesAmount-1, self.edgesAmount+val-1):
            self.edges.append(Edge(x+1))

    def getNeighbours(self, node):
        return self.nodes[node-1].getNeighbours()

    def getNodes(self):
        return self.nodes

    # def removeNode(self, index):
    #     self.removeConnections(index)
    #
    # def removeConnections(self, nodeIndex):
    #     print('len(self.edges', len(self.edges))
    #     removeList = []
    #     for x in range (0, len(self.edges)):
    #         print('x',x)
    #         if(self.edges[x].firstNode == nodeIndex):
    #             print("First node - x",x)
    #             removeList.append(x)
    #
    #         elif (self.edges[x].secondNode == nodeIndex):
    #             print("Second node - x", x)
    #             removeList.append(x)
    #     print("RemoveList", removeList)
    #     for y in range(0, len(removeList)):
    #         print("Removing:", y)
    #         self.edges.pop(removeList[y])


