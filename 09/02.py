import itertools

def lue_kulmat(tiedosto: str) -> list:
    with open(tiedosto) as f:
        kulmat = [tuple(int(luku) for luku in (r.strip().split(","))) for r in f]
    return kulmat

def tee_janat(kulmat: list) -> list:
    janat = [(kulmat[i -1], kulmat[i]) for i in range(len(kulmat))]
    return janat

def ala(eka: tuple[int, int], toka: tuple[int, int]) -> int:
    return (abs(eka[0] - toka[0]) + 1) * (abs(eka[1] - toka[1]) +1)

def viivan_pisteet(eka: tuple[int, int], toka: tuple[int, int]) -> tuple:
    dx = abs(eka[0] - toka[0])
    dy = abs(eka[1] - toka[1])
    if dy == 0:
        return tuple((min(eka[0], toka[0]) + i, eka[1]) for i in range(dx +1))
    elif dx == 0:
        return tuple((eka[0], min(eka[1], toka[1]) + i) for i in range(dy +1))
    else:
        kulmakerroin = dy / dx
        return tuple((min(eka[0], toka[0]) + i, eka[1] + i * kulmakerroin) for i in range(dx +1))

def viisto_paasuuntaviivoiksi(eka: tuple[int, int], toka: tuple[int, int]) -> list:
    vertikaalinen = (toka[0], eka[1])
    horisontaalinen = (eka[0], toka[1])
    return [viivan_pisteet(eka, vertikaalinen), viivan_pisteet(eka, horisontaalinen), \
            viivan_pisteet(vertikaalinen, toka), viivan_pisteet(horisontaalinen, toka)]

def viisto_viivakoordinaateiksi(eka: tuple[int, int], toka: tuple[int, int]) -> list:
    vertikaalinen = (toka[0], eka[1])
    horisontaalinen = (eka[0], toka[1])
    return [(eka, vertikaalinen), (eka, horisontaalinen), \
                (vertikaalinen, toka), (horisontaalinen, toka)]

def kulmia_sisalla(eka: tuple[int, int], toka: tuple[int, int], kulmat: list) -> bool:
    for kulma in kulmat:
        if min(eka[0], toka[0]) < kulma[0] < max(eka[0], toka[0]) and \
            min(eka[1], toka[1]) < kulma[1] < max(eka[1], toka[1]):
            return True
    else:
        return False

def suunta(alku: tuple[int, int], loppu: tuple[int, int]) -> str:
    dx = abs(alku[0] - loppu[0])
    dy = abs(alku[1] - loppu[1])
    if dy == 0:
        return "H"
    elif dx == 0:
        return "V"
    else:
        raise ValueError("Viiva on viisto") 

def tormaako (v1_alku: tuple, v1_loppu: tuple, v2_alku: tuple, v2_loppu: tuple) -> bool:
    if suunta(v1_alku, v1_loppu) == suunta(v2_alku, v2_loppu):
        return False
    if suunta(v1_alku, v1_loppu) == "V":
        vert = (v1_alku, v1_loppu)
        hori = (v2_alku, v2_loppu)
    elif suunta(v1_alku, v1_loppu) == "H":
        hori = (v1_alku, v1_loppu)
        vert = (v2_alku, v2_loppu)
    else:
        raise ValueError("Viivat omituisesti eivät saman- eikä poikkisuuntaiset")
    if min(vert[0][1], vert[1][1]) < hori[0][1] < max(vert[0][1], vert[1][1]) and \
    min(hori[0][0], hori[1][0]) < vert[0][0] < max(hori[0][0], hori[1][0]):
        return True
    else:
        return False

def maksimit(kulmat: list) -> tuple[int, int]:
    max_x = 0
    max_y = 0
    for jana in janat:
        max_x = max(max_x, jana[0][0], jana[1][0])
        max_y = max(max_y, jana[0][1], jana[1][1])
    return (max_x, max_y)

def onko_sisalla(x: int, y: int, janat: list, max_x: int, max_y: int) -> bool:
    px = x + 0.5 if x < max_x // 2 else x - 0.5
    py = y + 0.5 if y < max_y // 2 else y - 0.5
    osumia = 0

    for jana in janat:
        if suunta(jana[0], jana[1]) == "H":
            continue
        else:
            if tormaako((px, py), (max_x * 2, py), jana[0], jana[1]):
                osumia += 1
    return True if osumia % 2 == 1 else False


def onko_mahdollinen(eka: tuple[int, int], toka: tuple[int, int], kulmat: list, 
                     janat: list, max_x: int, max_y: int) -> bool:
    if kulmia_sisalla(eka, toka, kulmat):
        return False
    if not onko_sisalla(((eka[0] + toka[0]) // 2), ((eka[1] + toka[1]) // 2), \
                        janat, max_x, max_y):
        return False
    viivakoordinaatit = viisto_viivakoordinaateiksi(eka, toka)
    for viiva in viivakoordinaatit:
        for jana in janat:
            if tormaako(viiva[0], viiva[1], jana[0], jana[1]):
                return False
    else:
        return True
    


if __name__ == "__main__":
    tiedosto = "input.txt"
    kulmat = lue_kulmat(tiedosto)
    janat = tee_janat(kulmat)
    max_x, max_y = maksimit(kulmat)
    kulmat.sort(key= lambda kulma: kulma[0])
    suurin_ala = 0

    alat = []
    for eka, toka in itertools.combinations(kulmat, 2):
        alat.append((eka, toka, (abs(eka[0] - toka[0]) + 1) * (abs(eka[1] - toka[1]) +1)))
    alat.sort(key= lambda ala: ala[2], reverse=True)
    pass

    for i in range(len(alat)):
        piste_1, piste_2 = alat[i][0:2]
        print(f"Käydään läpi kulmayhdistelmä #{i}, suurin ala tähän asti "
              + f"on {suurin_ala}")
        if not onko_mahdollinen(piste_1, piste_2, kulmat, janat, max_x, max_y):
            continue
        else:
            nykyisen_ala = ala(piste_1, piste_2)
            if nykyisen_ala > suurin_ala:
                print(f"Löytyi uusin suurin ala, {piste_1} - {piste_2}")
                suurin_ala = nykyisen_ala
    
    print(f"Huh, kaikki käyty läpi ja suurin ala on {suurin_ala}")
