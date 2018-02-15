from node import Node
from graph import Graph
from edge import Edge

def MST(given, extraInfo={}):
    # This will store the resultant MST
    i = 0  # An index variable, used for sorted edges
    e = 0  # An index variable, used for result[]
    temp = given.edges
    temp = sorted(temp, key=lambda temp: temp.weight)
    for x in range(0, given.edgesAmount):
        print("uzyskano drzewo o takich kraw: ", temp[x].firstNode, temp[x].secondNode, temp[x].weight)
    TreeNumber = []
    result = Graph(given.nodesAmount, given.nodesAmount-1)
    for n in range(0, given.nodesAmount):
        TreeNumber.append(n+1)
    while e < given.nodesAmount-1:

        u = temp[i].firstNode
        v = temp[i].secondNode
        w = temp[i].weight
        print("dane wartosci", u, v, w)
        i = i + 1
        x = TreeNumber[u-1]
        y = TreeNumber[v-1]
        print("uzyskalem",x,y)
        if x != y:
            print("wykryto rozne drzewa, lacze...")
            e = e + 1
            result.addConnection(u, v, w)

            if x < y:
                for i1 in range(0, given.nodesAmount):
                    print("sprawdzam", i1, " szukamy", y)
                    if TreeNumber[i1] == y:
                        print("dopasowano", i1, "z wartoscia", y, "poprawiam na", x)
                        TreeNumber[i1] = x
            elif x > y:
                for i2 in range(0, given.nodesAmount):
                    print("sprawdzam", i2, " szukamy", y)
                    if TreeNumber[i2] == x:
                        print("dopasowano", i2, "z wartoscia", x, "poprawiam na", y)
                        TreeNumber[i2]=y
        print("wartosci wezlow", i, TreeNumber)

    return result



