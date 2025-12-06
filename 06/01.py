from math import prod

with open("input.txt") as f:
    eka_rivi = f.readline().strip().split()
    sarakkeet = {int(i): [int(eka_rivi[i])] for i in range(len(eka_rivi))}
    for r in f:
        rivi = r.strip().split()
        if rivi[0][0] in "0123456789":
            for i in range(len(rivi)):
                sarakkeet[i].append(int(rivi[i]))
        else:
            for i in range(len(rivi)):
                operaattorit = {i: rivi[i] for i in range(len(rivi))}

kaikkiaan = 0
for i in range(len(sarakkeet)):
    if operaattorit[i] == "+":
        kaikkiaan += sum(sarakkeet[i])
    elif operaattorit[i] == "*":
        kaikkiaan += prod(sarakkeet[i])

print(kaikkiaan)

