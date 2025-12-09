from itertools import combinations

tiedosto = "input.txt"

with open(tiedosto) as f:
    kulmat = [tuple(int(luku) for luku in (r.strip().split(","))) for r in f]

suurin = 0
for eka, toka in combinations(kulmat, 2):
    if (ala := (abs(eka[0] - toka[0]) + 1) * (abs(eka[1] - toka[1]) +1)) > suurin:
        suurin = ala

print(f"Suurin pinta-ala kahden ruudun kulmista on {suurin}")
