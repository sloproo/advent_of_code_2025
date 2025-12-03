def joltit(akusto: str) -> str:
    joltit = ""
    jatkopaikka = -1
    for paikka in range(0, 12):
        if len(akusto) == 12 - paikka:
            joltit += akusto
            return joltit
        for i in range(9, 0, -1):
            if (jatkopaikka := akusto[:-(10 - paikka)].find(str(i))) >= 0:
                joltit += str(i)
                akusto = akusto[jatkopaikka +1:]
                break
            pass
    return joltit


with open("alku.txt") as f:
    for r in f:
        print(f"{joltit(r.strip())}")

