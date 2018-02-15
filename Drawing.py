import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
the = 0
colors = ['g', 'r', 'c', 'm', 'y', 'k', 'w']
def convert(OurGraph):
    print("Zamieniam", OurGraph.name ,"na Graf interpretowany przez biblio graficzną...")
    Converted=nx.empty_graph()
    Converted.add_nodes_from(OurGraph.nodesIndex)
    Converted.add_edges_from(OurGraph.edgesIndex)
    print("Uzyskano Graf o Węzłach:", OurGraph.nodesIndex, "i Krawędziach:", OurGraph.edgesIndex)

    return Converted
def ExtractWeight(OurGraph):
    temp = {}
    for x in range(0,OurGraph.edgesAmount):
        temp[(OurGraph.edges[x].firstNode, OurGraph.edges[x].secondNode)]=OurGraph.edges[x].weight
    return temp

def test_draw(given):
    print("Wywolano Funkcje rysowania")
    ToDraw=convert(given)
    Weights1=ExtractWeight(given)
    pos=nx.shell_layout(ToDraw) #shell position definiuje ulozenie wezlow na naszym grafie w taki typowy pseudo-okragly ksztalt
    pos2=nx.random_layout(ToDraw) #random position robi dokladnie to co brzmi czyli rzuca przypadkowo wezlami
    plt.figure(1)
    nx.draw_networkx_nodes(ToDraw,pos,node_color='b',node_size=500,alpha=0.8)
    nx.draw_networkx_labels(ToDraw,pos,font_size=16) #wazne! Pozycjonowanie w pisaniu etykiet oraz przypinaniu krawedzi musi == pozycjonowaniu wezlow (co w sumie dosc logiczne)
    nx.draw_networkx_edge_labels(ToDraw, pos, edge_labels=Weights1, label_pos=0.4, font_size=16)
    nx.draw_networkx_edges(ToDraw, pos, edge_color='b')
    print("Wywolano Okno")
    plt.show()
    print("Zakonczono wyswietlanie okna")
def SimpleDraw(given1,given2,separate):
    print("Wywolano Funkcje rysowania z Wyróżnioną ścieżką")
    ToDraw = convert(given1)
    copy = convert(given2)
    ToHighlight = nx.empty_graph()
    ToHighlight.add_edges_from(copy.edges)
    Weights1 = ExtractWeight(given1)
    Weights2 = ExtractWeight(given2)
    XYpositions = {
        1: (2, 7), 2: (6, 6), 3: (1, 2), 4: (4, 4), 5: (7, 2)
    # opcja sztywnego zakodowania koordynatow X, Y grafu, zostalo do ogarniecia
    }
    pos = nx.shell_layout(ToDraw)  # shell position definiuje ulozenie wezlow na naszym grafie w taki typowy pseudo-okragly ksztalt
    pos2 = nx.random_layout(ToDraw)  # random position robi dokladnie to co brzmi czyli rzuca przypadkowo wezlami
    plt.figure(1)
    nx.draw_networkx_nodes(ToDraw, pos, node_color='black', node_size=500, alpha=0.8)
    nx.draw_networkx_labels(ToDraw, pos, font_size=16, font_color='white')# wazne! Pozycjonowanie w pisaniu etykiet oraz przypinaniu krawedzi musi == pozycjonowaniu wezlow (co w sumie dosc logiczne)
    nx.draw_networkx_edge_labels(ToDraw, pos, edge_labels=Weights1, label_pos=0.4, font_size=16)
    nx.draw_networkx_edges(ToDraw, pos, edge_color='black', width=2)
    if separate:
        plt.figure(2)
        nx.draw_networkx_nodes(ToHighlight, pos, node_color='r', node_size=300, alpha=0.8)
    if separate:
        nx.draw_networkx_labels(ToHighlight, pos, font_size=16)
        nx.draw_networkx_edge_labels(ToHighlight, pos, edge_labels=Weights2, label_pos=0.4, font_size=16)
    nx.draw_networkx_edges(ToHighlight, pos, edge_color='r', width=4)
    print("Wywolano Okno")
    plt.show()
    print("Zakonczono wyswietlanie okna")

def DrawingFloyd (see, u):
    ToDraw = convert(see)
    Weights1 = ExtractWeight(see)
    pos = nx.shell_layout(ToDraw)  # shell position definiuje ulozenie wezlow na naszym grafie w taki typowy pseudo-okragly ksztalt
    plt.figure(1)
    nx.draw_networkx_nodes(ToDraw, pos, node_color='black', node_size=700, alpha=0.4)
    nx.draw_networkx_labels(ToDraw, pos, font_size=16, font_color='white')
    nx.draw_networkx_edge_labels(ToDraw, pos, edge_labels=Weights1, label_pos=0.4, font_size=16)
    nx.draw_networkx_edges(ToDraw, pos, edge_color='black', width=2, alpha=0.4)
    Moon = []
    for on in range(the, len(u)):
        Dark = nx.empty_graph()
        for side in range(the, len(u[on])-1 ):
            Dark.add_edge(u[on][side],u[on][side + 1])
            print("trasa numer: ", on+1 ,u[on][side],u[on][side + 1])
        Moon.append(Dark)
    print("uzyskano tyle sciezek:", len(Moon))

    for x in range(the, len(Moon)):
        i=x
        if i>6:
            i=i-8
        r= 10*0.8**i
        print(r)
        nx.draw_networkx_edges(Moon[x], pos, edge_color=colors[i], width= r, alpha=0.8)
        nx.draw_networkx_nodes(Moon[x], pos, node_color=colors[i], node_size= r*90, alpha=0.7)
    plt.show()
def DrawingSteiner(grap, tabGrap):
    grap.prepare()
    for i in range(0, len(tabGrap)):
        tabGrap[i].prepare()
    ToDraw = convert(grap)
    Weights1 = ExtractWeight(grap)
    pos = nx.shell_layout(ToDraw)  # shell position definiuje ulozenie wezlow na naszym grafie w taki typowy pseudo-okragly ksztalt
    plt.figure(1)
    nx.draw_networkx_nodes(ToDraw, pos, node_color='black', node_size=300, alpha=0.4)
    nx.draw_networkx_labels(ToDraw, pos, font_size=16, font_color='white')
    nx.draw_networkx_edge_labels(ToDraw, pos, edge_labels=Weights1, label_pos=0.4, font_size=16)
    nx.draw_networkx_edges(ToDraw, pos, edge_color='black', width=1, alpha=0.4)
    tempDraw = nx.empty_graph()
    for i in range (0, len(tabGrap)):
        print("BBBB",tabGrap[i].nodesIndex)
        temp2Draw = convert(tabGrap[i])
        tempDraw.add_edges_from(temp2Draw.edges)
    nx.draw_networkx_nodes(tempDraw, pos, node_color='r', node_size=500, alpha=0.8)
    nx.draw_networkx_edges(tempDraw, pos, edge_color='r', width=2, alpha=0.4)
    plt.show()







