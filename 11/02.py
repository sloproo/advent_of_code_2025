def avaa(tiedosto: str) -> dict:
    sanakirja = {}
    with open(tiedosto) as f:
        for r in f:
            sanakirja[r.split(": ")[0]] = r.split(": ")[1].strip().split(" ")
    return sanakirja

def pitkanimi(portti: str, dacfft: list[int]):
    return portti + "".join([str(i) for i in dacfft])

def syvemmalle(portti: str, portit: dict, ratkaistut: dict, kaydyt: list) -> tuple[int, dict]:
    uudet_kaydyt = kaydyt.copy()
    uudet_kaydyt.append(portti)
    dac_kayty = "dac" in uudet_kaydyt
    fft_kayty = "fft" in uudet_kaydyt

    portti_statuksella = str((portti, dac_kayty, fft_kayty))
    if portti_statuksella in ratkaistut:
        return (ratkaistut[portti_statuksella], ratkaistut)
    if portti == "out":
        # print(f"Maalissa, reitti takana: {uudet_kaydyt}")
        if (dac_kayty and fft_kayty):
            reitteja = 1
            # print(f"Oli fft ja dac, lisätään 1")
        else:
            reitteja = 0
     
    else:
        reitteja = 0
        for maali in portit[portti]:
            if maali in uudet_kaydyt:
                print("Nyt kävi näin")
                continue
            else:
                uusia, ratkaistut = syvemmalle(maali, portit, ratkaistut, uudet_kaydyt)
                reitteja += uusia
    ratkaistut[portti_statuksella] = reitteja
    # print(f"Ratkaistu on {str(uudet_kaydyt)}: {ratkaistut[str(uudet_kaydyt)]}")
    return (reitteja, ratkaistut)

portit = avaa("input.txt")
kaydyt = ["svr"]
reitteja = 0
ratkaistut = {}

for portti in portit[kaydyt[0]]:
    uusiareitteja, ratkaistut = syvemmalle(portti, portit, ratkaistut, kaydyt)
    reitteja += uusiareitteja

print(reitteja)
