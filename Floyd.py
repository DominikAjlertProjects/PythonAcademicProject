from graph import Graph
from node import Node
from edge import Edge

def addReversePath(graph):
    for nodeId, arr in graph.items():
        for withNode, weight in arr.items():
            graph[withNode][nodeId] = graph[nodeId][withNode]
    return graph

def returnPath(arr, pred):
    start = arr[0]
    goal = arr[1]
    path = []
    # print("pred[start]", pred[int(start)])
    search = 0
    path.append(int(start))
    while search != int(goal):
        if search == 0:
            search = start

        if(search == -1):
            print('Breaking')
            break

        if(search == int(goal)):
            path.append(search)
            print('Breaking')
            break;

        # print("pred[start][search]", pred[int(start)][int(search)])
        search = pred[int(goal)][int(search)]
        path.append(search)
        print('Search', search)

    return path

def floyd(graph1, extraData = {}):
    graph = {}
    for x in range (0, len(graph1.nodes)):
        graph[x+1] = graph1.nodes[x].connections

    graph = addReversePath(graph)
    dist = {}
    pred = {}

    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = 1000
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u

    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v]  # route new path through t


    path = []
    for x in range(0, len(extraData)):
        path.append(returnPath(extraData[x], pred))

    print('Path:', path)
    print(pred)
    return path

