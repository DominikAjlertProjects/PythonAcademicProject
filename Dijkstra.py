from graph import Graph
from node import Node
from edge import Edge

def generateGraph(path, graph1):
    originalGraph = {}
    print("Graph1", graph1)
    for x in range (0, len(graph1.nodes)):
        originalGraph[x+1] = graph1.nodes[x].connections

    originalGraph = addReversePath(originalGraph)
    print("originalGraph", originalGraph)
    print("path)", path)
    graph = Graph(graph1.nodesAmount, graph1.edgesAmount)
    for x in range (0,len(graph1.nodes)):
        graph.nodes[x].X = graph1.nodes[x].X
        graph.nodes[x].Y = graph1.nodes[x].Y
        # print("graph.nodes[x].X", graph.nodes[x].X)
        # print("graph.nodes[x].y", graph.nodes[x].Y)

    for x in range (0, len(path)-1):
        # print("Adding", x)
        graph.addConnection(path[x], path[x+1], originalGraph[path[x]][path[x+1]])

    return graph

def addReversePath(graph):
    for nodeId, arr in graph.items():
        for withNode, weight in arr.items():
            graph[withNode][nodeId] = graph[nodeId][withNode]
    return graph

def dijkstra(graph1, extraData = {}):
    shortest_path = {}
    graph = {}
    start = extraData['start']
    goal = extraData['goal']
    for x in range (0, len(graph1.nodes)):
        graph[x+1] = graph1.nodes[x].connections

    graph = addReversePath(graph)
    originalGraph = graph
    print(originalGraph)
    print(graph)
    predecessor = {}
    unvisitedNodes = graph
    inf = 9999999
    path = []

    for node in unvisitedNodes:
        shortest_path[node] = inf
    shortest_path[start] = 0

    while unvisitedNodes:
        minNode = None
        for node in unvisitedNodes:
            if minNode is None:
                minNode = node
            elif shortest_path[node] < shortest_path[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_path[minNode] < shortest_path[childNode]:
                shortest_path[childNode] = weight + shortest_path[minNode]
                predecessor[childNode] = minNode
        unvisitedNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_path[goal] != inf:
        print('Shortest distance is', shortest_path[goal])
        print('And the path is', str(path))
    # print('graph1', graph1)
    return generateGraph(path, graph1)



