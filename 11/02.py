def avaa(tiedosto: str) -> dict:
    sanakirja = {}
    with open(tiedosto) as f:
        for r in f:
            sanakirja[r.split(": ")[0]] = r.split(": ")[1].strip().split(" ")
    return sanakirja

def pitkanimi(portti: str, dacfft: list[int]):
    return portti + "".join([str(i) for i in dacfft])

def syvemmalle(portti: str, portit: dict, ratkaistut: dict, kaydyt: list, 
               dacfft: list[int]) -> tuple[int, dict]:
    reitteja = 0
    if portti == "dac":
        dacfft[0] = 1
    elif portti == "fft":
        dacfft[1] = 1
    nyk_pitka = pitkanimi(portti, dacfft)
    kaydyt.append(nyk_pitka)
    if portti == "out":
        if dacfft == [1, 1]:
            reitteja += 1
            print(f"Löytyi kunnon reitti {kaydyt}")
        else:
            reitteja += 0
            # print(f"Lopussa muttei dacfft {kaydyt}")
        
        return (reitteja, ratkaistut)
    else:
        for maali in portit[portti]:
            if portti == "out":
                pass
            pitka = pitkanimi(maali, dacfft)
            if pitka in ratkaistut:
                reitteja += ratkaistut[pitka]
            if pitka in kaydyt:
                continue
            else:
                reitteja, ratkaistut = syvemmalle(maali, portit, ratkaistut, kaydyt, dacfft)
                
    ratkaistut[pitka] = reitteja
    return (reitteja, ratkaistut)

portit = avaa("alku2.txt")
kaydyt = [("svr00")]
reitteja = 0
ratkaistut = {}
dacfft = [0, 0]
# Halutut portit: "dac" ja "fft"

for portti in portit["svr"]:
    uusia_reitteja, ratkaistut = syvemmalle(portti, portit, ratkaistut, kaydyt, [0, 0])
    reitteja += uusia_reitteja

print(reitteja)

# 22 väärin
# 316 liian matala
