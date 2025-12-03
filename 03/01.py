def joltit(akusto: str) -> int:
    for i in range(9, 0, -1):
        if (ekan_paikka := akusto[:-1].find(str(i))) >= 0:
            eka = (i, ekan_paikka)
            break
    if eka[1] == len(akusto) - 2:
        toka = (int(akusto[-1]), len(akusto) - 1)
    else:
        for j in range(9, 0, -1):
            if (tokan_paikka := akusto[eka[1] + 1:].find(str(j))) >= 0:
                toka = (j, eka[1] + 1 + tokan_paikka)
                break

    return eka[0] * 10 + toka[0]

jolttisumma = 0
with open("input.txt") as f:
    for r in f:
        jolttisumma += joltit(r.strip())

print(jolttisumma)
