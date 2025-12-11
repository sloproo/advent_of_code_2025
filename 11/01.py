def avaa(tiedosto: str) -> dict:
    sanakirja = {}
    with open(tiedosto) as f:
        for r in f:
            sanakirja[r.split(": ")[0]] = r.split(": ")[1].strip().split(" ")
    return sanakirja

def syvemmalle(portti: str, portit: dict, ratkaistut: dict, kaydyt: list) -> tuple[int, dict, list]:
    reitteja  = 0
    for maali in portit[portti]:
        if maali in ratkaistut:
            reitteja += ratkaistut[maali]
        elif maali == "out":
            reitteja += 1
        else:
            reitteja += syvemmalle(maali, portit, ratkaistut, kaydyt)[0]
    ratkaistut[portti] = reitteja
    return (reitteja, ratkaistut, kaydyt)

portit = avaa("input.txt")
kaydyt = ["you"]
reitteja = 0
ratkaistut = {}

for portti in portit["you"]:
    uusiareitteja, ratkaistut, kaydyt = syvemmalle(portti, portit, ratkaistut, kaydyt)
    reitteja += uusiareitteja

print(reitteja)
