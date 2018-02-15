
def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

import handleInput
from choices import choices, Draw
from steiner import Steiner
from Drawing import DrawingSteiner, test_draw
grap, method, extraInfo = handleInput.loadInput('mst.txt') #czytanie pliku
result = choices.get(method) #odnajdywanie wlasciwiej metody
data = result(grap, extraInfo) #pozyskiwanie danych z algorytmow
Draw(grap,method,data) #obrazowanie wyniku na ekranie
tabGraph = Steiner(data, extraInfo)
data.prepare()
DrawingSteiner(data, tabGraph)
print(grap.edgesIndex)
print(data.edgesIndex)
a = diff(grap.edgesIndex, data.edgesIndex)
print(a)
