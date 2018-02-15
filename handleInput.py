import re
from random import randint
from graph import Graph
import math
def calculateDistance(first, second):
    print('First.x', first.X)
    print('First.Y', first.Y)
    dist = int(math.sqrt(math.fabs(int(first.X) - int(second.Y))**2 + math.fabs(int(second.Y) - int(first.Y))**2))
    return dist
def loadInput(filename):
    f = open(filename, "r")
    result = []
    nodes = []
    edges = []
    extraInfo = {}
    linesTable = f.readlines()
    mustHave = []
    for x in range(0, len(linesTable) - 1):
        res = linesTable[x].find("WEZLY")
        if (res == 0):
            res = re.findall('\d+', linesTable[x])
            result.append(res[0])
            term = int(result[0])
            for y in range (x+1, term+x+2):
                found = linesTable[y].find("#")
                if(found == 0):
                    term = term + 1
                else:
                    node = re.findall('\d+', linesTable[y])
                    if(len(node) > 3):
                        if(int(node[3]) == 1):
                            mustHave.append(int(node[0]))
                    nodes.append(node)

        res1 = linesTable[x].find("LACZA")
        if (res1 == 0):
            res = re.findall('\d+', linesTable[x])
            result.append(res[0])
            term = int(result[1])
            for y in range (x+1, term+x+2):
                found = linesTable[y].find("#")
                if(found == 0):
                    term = term + 1
                else:
                    edge = re.findall('\d+', linesTable[y])
                    edges.append(edge)

        res2 = linesTable[x].find("ALGORYTM")
        if(res2 == 0):
            splitTable = linesTable[x].split()
            method = splitTable[2]
            if (method == 'MST'):
                extraInfo = mustHave

            if(method == 'SCIEZKA'):
                values = linesTable[x+1].split()
                while(values[0] == '#'):
                    x = x+1
                    values = linesTable[x+1].split()
                extraInfo = {'start': int(values[0]), 'goal': int(values[1])}
            elif (method == 'FLOYD'):
                linesToRead = []
                rang = len(linesTable)
                for y in range(x+1, rang):
                    arr = linesTable[y].split()
                    linesToRead.append(arr)
                    if (arr[0] == "#"):
                        print('arr[0] == #')
                        rang = rang + 1
                        linesToRead.pop()
                extraInfo = linesToRead


    f.close()
    grap = Graph(int(result[0]), int(result[1]))
    for x in range (0, len(nodes)):
        grap.nodes[x].X = nodes[x][1]
        grap.nodes[x].Y = nodes[x][2]

    for x in range(0, len(edges)):
        print("Edges[x]", edges[x])
        grap.addConnection(int(edges[x][1]), int(edges[x][2]), calculateDistance(grap.nodes[int(edges[x][1])-1], grap.nodes[int(int(edges[x][2]))-1]))

    print('ExtraInfo', extraInfo)
    return grap, method, extraInfo