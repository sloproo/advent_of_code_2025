def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        ruudukko = []
        for r in f:
            ruudukko.append([m for m in r.strip()])
    return ruudukko

def naapurit(ruudukko: list, x: int, y: int) -> list:
    naapurilista = []
    korkeus = len(ruudukko)
    leveys = len(ruudukko[0])
    for y_naapuri in range(y-1, y+2):
        for x_naapuri in range(x-1, x+2):
            if y_naapuri >= 0 and x_naapuri >= 0 and \
            x_naapuri < leveys and y_naapuri < korkeus and \
            (x_naapuri != x or y_naapuri != y):
                naapurilista.append((x_naapuri, y_naapuri))
    return naapurilista

def siivoa(ruudukko: list, saavutettavat: list) -> list:
    for (x, y) in saavutettavat:
        ruudukko[y][x] = "."
    return ruudukko

ruudukko = lue("alku.txt")
poistettuja = 0

while True:
    saavutettavat = []
    for y in range(len(ruudukko)):
        for x in range(len(ruudukko[0])):
            if ruudukko[y][x] != "@":
                continue
            tukittuja = 0
            for x_naap, y_naap in naapurit(ruudukko, x, y):
                if ruudukko[y_naap][x_naap] == "@":
                    tukittuja += 1
            if tukittuja < 4:
                saavutettavat.append((x, y))

    print(f"Saavutettavia rullia on {len(saavutettavat)}")
    if saavutettavat == []:
        break
    ruudukko = siivoa(ruudukko, saavutettavat)
    poistettuja += len(saavutettavat)

print(f"Rullia saatiin poistettua yhteensä {poistettuja}")
