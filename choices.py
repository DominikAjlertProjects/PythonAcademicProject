from Dijkstra import dijkstra
from Kruskal import MST
from Floyd import floyd
from Drawing import DrawingFloyd, SimpleDraw

choices = {'SCIEZKA': dijkstra, 'MST': MST, 'FLOYD': floyd}

def Draw(grap, what, data):
    if what == "FLOYD":
        grap.prepare()
        DrawingFloyd(grap, data)
    elif what == "SCIEZKA" or "MST":
        grap.prepare()
        data.prepare()
        SimpleDraw(grap, data, False)
    else:
        print("file error, end")