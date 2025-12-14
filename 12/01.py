def lue(tiedosto: str):
    with open("input.txt") as f:
        palat = []
        for r in f:
            if r == "\n":
                continue
            if r[1] == ":":
                palanro = int(r[0])
                pala = [f.readline().strip() for _ in range(3)]
                palat.append(pala)
            if len(palat) == 6:
                f.readline()
                break
        palat = tuple(palat)
        kuuset = []
        for r in f:
            kenttapuoli, palapuoli = r.split(": ")
            ala = tuple(int(x) for x in kenttapuoli.split("x"))
            palalista = [int(l) for l in palapuoli.strip().split(" ")]
            kuuset.append((ala, palalista))
    return palat, kuuset

palat, kuuset = lue("input.txt")

ruutumaarat = []
for pala in palat:
    ruudut = "".join([rivi for rivi in pala]).count("#")
    ruutumaarat.append(ruudut)
ruutumaarat = tuple(ruutumaarat)

for kuusi in kuuset:
    tilaa = kuusi[0][0] * kuusi[0][1]
    ruutuja_vaaditaan = ruutumaarat[i] * 

