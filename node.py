import sys

class Node():
    def __init__(self, value, X=0, Y=0):
        self.id = value
        self.X = X
        self.Y = Y
        self.distance = 10000
        self.isVisited = False
        self.previous = None
        self.charValue = chr(self.id + 64)
        self.connections = {}
        self.connectionsAsList = []

    def returnId(self):
        return self.id

    def returnChar(self):
        return self.charValue

    def addConnection(self, withNode, val):
        self.connections[withNode] = val
        self.connectionsAsList.append((self.id,withNode))

    def getNeighbours(self):
        neighboursArray = self.connections
        print('nArray', neighboursArray)
        return neighboursArray

    def getNeighbour(self, index):
        return index

    def getDistance(self):
        return self.distance

    def setDistance(self, dist):
        self.distance = dist

    def setVisited(self, value):
        self.visited = value