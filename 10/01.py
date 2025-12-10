import itertools

def lue(tiedosto: str) -> list:
    koneet = []
    with open(tiedosto) as f:
        for r in f:
            r = r.strip().split(" ")
            valot  = []
            valo = r[0][1:-1]
            for i in range(len(valo)):
                valot.append(int(i)) if valo[i] == "#" else i
            
            napit = []
            for nappi in r[1:-1]:
                napit.append([int(luku) for luku in nappi[1:-1].split(",")]) 

            joltit = [int(i) for i in r[-1][1:-1].split(",")]
            koneet.append({"valot": valot, "napit": napit, "joltit": joltit})
    return koneet

def vahimmat_painallukset(kone: dict) -> int:
    for i in range(len(kone["napit"])):
        kokeiltavat_yhdistelmat = list(itertools.combinations(kone["napit"], i))
        palavat_lamput = []
        for nappiyhdistelma in kokeiltavat_yhdistelmat:
            for nappi in nappiyhdistelma:
                for luku in nappi:
                    if luku in palavat_lamput:
                        palavat_lamput.remove(luku)
                    else:
                        palavat_lamput.append(luku)
            palavat_lamput.sort()
            if palavat_lamput == kone["valot"]:
                return i
            else:
                palavat_lamput = []
    raise EOFError("Ei löytynyt toimivaa nappiyhdistelmää")
            
koneet = lue("input.txt")

painalluksia = 0
for kone in koneet:
    painalluksia += vahimmat_painallukset(kone)
print(f"Kaikkien koneiden kaikkien lamppujen sytyttämiseen riittää " +
      f"{painalluksia} napinpainallusta")
print(f"Eli siis {painalluksia}\n")
print(painalluksia)
