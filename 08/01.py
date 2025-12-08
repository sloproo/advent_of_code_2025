from math import sqrt, prod
import itertools

tiedosto = "input.txt"
if tiedosto  == "input.txt":
    kytkentoja = 1000
elif tiedosto == "alku.txt":
    kytkentoja = 10


def etaisyys(eka: tuple[int, int,int], toka: tuple[int, int,int]) -> float:
    return sqrt(sum([(eka[i] - toka[i]) ** 2  for i in range(3)]))

def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        boksit = [tuple(int(n) for n in r.strip().split(",")) for r in f]
    return boksit

boksit = lue("input.txt")

etaisyydet = {}
yhdistelmat = list(itertools.combinations(boksit, 2))
for yh in list(itertools.combinations(boksit, 2)):
    etaisyydet[(yh[0], yh[1])] = etaisyys(yh[0], yh[1])

etat_laji = [((eta[0], eta[1], etaisyydet[eta])) for eta in sorted(etaisyydet, key=lambda e: etaisyydet[e])]

piirit  = [{etat_laji[0][0], etat_laji[0][1]}]
for i in range(1, kytkentoja):
    eka = etat_laji[i][0]
    toka = etat_laji[i][1]
    ekan_piiri, tokan_piiri = None, None
    for piiri in piirit:
        if eka in piiri:
            ekan_piiri = piiri
        if toka in piiri:
            tokan_piiri = piiri
        if ekan_piiri != None and tokan_piiri != None:
            if ekan_piiri == tokan_piiri:
                break
            else:
                uusi = ekan_piiri.union(tokan_piiri)
                piirit.remove(ekan_piiri)
                piirit.remove(tokan_piiri)
                piirit.append(uusi)
                break
    else:
        if ekan_piiri != None and tokan_piiri == None:
            ekan_piiri.add(toka)
        elif ekan_piiri == None and tokan_piiri != None:
            tokan_piiri.add(eka)
        else:
            piirit.append({eka, toka})

piirit.sort(key=len, reverse=True)
print(f"Kolmen suurimman piirin kokojen tulo on {prod([len(p) for p in piirit[:3]])}")
