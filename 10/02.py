import itertools
from functools import cache

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

def matriisiksi(napit: list[list[int]], joltit: list[int]) -> tuple[tuple[tuple[int, ...]], tuple[int, ...]]:
    matriisi = []
    for nappi in napit:
        matriisi.append(tuple(1 if i in nappi else 0 for i in range(len(joltit))))
    
    return tuple(sorted(matriisi, key= sum, reverse=True)), tuple(joltit)

def vahenna_jolteista(joltit: tuple[int, ...], vektori: tuple[int, ...], kerroin: int =1):
    return tuple(j - kerroin * v for j, v in zip(joltit, vektori))

def vahimmat_painallukset(kone: dict) -> int:

    painalluksia_vahintaan = max(kone["joltit"])
    for i in range(painalluksia_vahintaan, 1000):
        kokeiltavat_yhdistelmat = list(itertools.combinations_with_replacement(kone["napit"], i))
        jannitteet = [0 for _ in range(len(kone["joltit"]))]
        for nappiyhdistelma in kokeiltavat_yhdistelmat:
            painettavat_napit = set([luku for nappi in nappiyhdistelma for luku in nappi])
            nousevat_joltit = set(j for j in range(len(kone["joltit"])) if kone["joltit"][j] != 0)
            if painettavat_napit != nousevat_joltit:
                continue
            for nappi in nappiyhdistelma:
                for luku in nappi:
                    jannitteet[luku] += 1
                    if jannitteet[luku] > kone["joltit"][luku]:
                        break
                break
            
            if jannitteet == kone["joltit"]:
                print(f"Ratkaistu kone, jossa oli {len(kone['joltit'])} patteria")
                print(f"painalluksia vaadittiin {i}")
                return i
            else:
                jannitteet = [0 for _ in range(len(kone["joltit"]))]
    raise EOFError("Ei löytynyt toimivaa nappiyhdistelmää")
            
@cache
def backtrackaa(i: int, joltit: tuple[int, ...]) -> float:
    if all(x == 0 for x in joltit):
        return 0.0
    if i > len(vektorit):
        return float("inf")
    
    paras_tulos = float("inf")

    max_vektoria = float("inf")
    for v, j in zip(vektorit[i], joltit):
        if v > j:
            max_vektoria = 0
        elif v > 0 and j // v > 0:
            max_vektoria = min(j // v, max_vektoria)
    if type(max_vektoria) != int:
        max_vektoria = 0

    for n in range(max_vektoria, -1, -1):
        seuraavat_joltit = vahenna_jolteista(joltit, vektorit[i], n)
        taman_tulos = min(paras_tulos, backtrackaa(i + 1, seuraavat_joltit))
        taman_tulos += n
        paras_tulos = min(taman_tulos, paras_tulos)
    return paras_tulos
    

koneet = lue("alku.txt")
ratkaisuja = 0
for kone in koneet:
    vektorit, joltit = matriisiksi(kone["napit"], kone["joltit"])
    koneen_paras_ratkaisu = float("inf")
    koneen_ratkaisu = backtrackaa(0, joltit)
    koneen_paras_ratkaisu = min(koneen_paras_ratkaisu, koneen_ratkaisu)
    ratkaisuja += koneen_paras_ratkaisu
    print(f"Napin painalluksia tähän asti käsitellyistä koneista on {ratkaisuja}")


