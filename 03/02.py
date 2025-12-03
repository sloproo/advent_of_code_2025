def laske_joltit(akut: str) -> str:
    joltit = ""
    for paikka in range(1, 13):
        jaljella = 12 - paikka
        if len(akut) == jaljella:
            joltit += akut
            return joltit
        for i in range(9, 0, -1):
            jatkopaikka = akut.find(str(i))
            if jatkopaikka != -1 and jatkopaikka < len(akut)  -jaljella:
                joltit += str(i)
                akut = akut[jatkopaikka +1:]
                break
    return int(joltit)

kaikki = 0
with open("input.txt") as f:
    for r in f:
        kaikki += laske_joltit(r.strip())

print(f"Jolttien summa on: {kaikki}")
