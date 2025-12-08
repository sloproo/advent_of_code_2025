from math import sqrt, prod
import itertools

tiedosto = "input.txt"

def etaisyys(eka: tuple[int, int,int], toka: tuple[int, int,int]) -> float:
    return sqrt(sum([(eka[i] - toka[i]) ** 2  for i in range(3)]))

def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        boksit = [tuple(int(n) for n in r.strip().split(",")) for r in f]
    return boksit

kytkemattomat = lue(tiedosto)

etaisyydet = {}
yhdistelmat = list(itertools.combinations(kytkemattomat, 2))
for yh in list(itertools.combinations(kytkemattomat, 2)):
    etaisyydet[(yh[0], yh[1])] = etaisyys(yh[0], yh[1])

etat_laji = [((eta[0], eta[1], etaisyydet[eta])) for eta in sorted(etaisyydet, key=lambda e: etaisyydet[e])]

piirit  = [{etat_laji[0][0], etat_laji[0][1]}]
i = 0

while len(piirit) != 1 or len(kytkemattomat) != 0:
    i += 1
    eka = etat_laji[i][0]
    toka = etat_laji[i][1]
    for boksi in [eka, toka]:
        if boksi in kytkemattomat:
            kytkemattomat.remove(boksi)
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

print(f"Kaksi viimeiseksi kytkettyä boksia ovat {eka} ja {toka}")
print(f"Niiden x-koordinaattien tulo on {eka[0] * toka[0]}")
