from functools import cache
import math

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

def luo_riittavyys_kartta(vektorit: tuple[tuple[int, ...]], ulottuvuuksia: int) -> tuple[tuple[int, ...]]:
    ulottuvuudet = []
    for i in range(len(vektorit) -1, -1, -1):
        tasta_eteenpain = []
        for j in range(ulottuvuuksia):
            for v in vektorit[i:]:
                if v[j] >= 1:
                    tasta_eteenpain.append(1)
                    break
            else:
                tasta_eteenpain.append(0)
        ulottuvuudet.append(tuple(tasta_eteenpain))
    return tuple(reversed(ulottuvuudet))
            
@cache
def backtrackaa(i: int, joltit: tuple[int, ...]) -> float:
    if all(x == 0 for x in joltit):
        return 0.0
    if i >= len(vektorit):
        return float("inf")
    for m, j in zip(riittavyys_kartta[i], joltit):
        if j > 0 and m == 0:
            return float("inf")
    
    max_vektoria = float("inf")
    for v, j in zip(vektorit[i], joltit):
        if v > j:
            max_vektoria = 0
        elif v > 0 and j // v > 0:
            max_vektoria = min(j // v, max_vektoria)
    if type(max_vektoria) != int:
        max_vektoria = 0

    paras_tulos = float("inf")

    seuraava_teho = vektorien_summat[i+1] if (i + 1) < len(vektorien_summat) else 0

    for n in range(max_vektoria, -1, -1):
        if n >= paras_tulos:
            continue
        
        seuraavat_joltit = vahenna_jolteista(joltit, vektorit[i], n)
        
        arvioitu_minimi_loppu = max(seuraavat_joltit) if seuraavat_joltit else 0
        
        # 2. UUSI ARVIO (Massa)
        # Lasketaan: Jolttien summa / Tehokkaimman jäljellä olevan vektorin summa
        if seuraava_teho > 0:
            arvioitu_massa = math.ceil(sum(seuraavat_joltit) / seuraava_teho)
        else:
            # Jos tehoa ei ole (0), mutta joltteja on -> mahdoton
            arvioitu_massa = float('inf') if any(seuraavat_joltit) else 0

        # Otetaan tiukempi (suurempi) näistä kahdesta
        lopullinen_arvio = max(arvioitu_minimi_loppu, arvioitu_massa)

        # Tarkistus
        if n + lopullinen_arvio >= paras_tulos:
            continue
        
        
        loppuosan_tulos = backtrackaa(i + 1, seuraavat_joltit)
        if n + loppuosan_tulos < paras_tulos:
            paras_tulos = n + loppuosan_tulos
    return paras_tulos
    

koneet = lue("input.txt")
ratkaisuja = 0
kone_i = 1
for kone in koneet:
    vektorit, joltit = matriisiksi(kone["napit"], kone["joltit"])
    vektorien_summat = tuple(sum(v) for v in vektorit)
    riittavyys_kartta = luo_riittavyys_kartta(vektorit, len(joltit))
    backtrackaa.cache_clear()
    koneen_paras_ratkaisu = float("inf")
    koneen_ratkaisu = backtrackaa(0, joltit)
    koneen_paras_ratkaisu = int(min(koneen_paras_ratkaisu, koneen_ratkaisu))
    ratkaisuja += koneen_paras_ratkaisu
    print(f"Koneen {kone_i} lyhyin ratkaisu ottaa {koneen_paras_ratkaisu} napinpainallusta")
    kone_i += 1
print(f"Napin painalluksia kaikkien koneiden parhaista ratkaisuista tuli {ratkaisuja}")


