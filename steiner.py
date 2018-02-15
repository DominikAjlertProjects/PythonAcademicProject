from Dijkstra import dijkstra
from Kruskal import MST
from Floyd import floyd
from Drawing import ExtractWeight

#def change():

def Steiner (given, tab2):
    #nodes = given.nodesIndex
    graps = []
    grap = given
    ints = len(tab2)-1
    for x in range (0, ints):
        new = dijkstra(grap, {'start': tab2[x], 'goal': tab2[x+1]})
        graps.append(new)
    return graps





