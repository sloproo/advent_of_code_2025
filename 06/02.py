from math import prod

with open("input.txt") as f:
    rivit = []
    for r in f:
        if r.lstrip()[0] in "1234567890":
            rivit.append(r.replace("\n", ""))
        else:
            operaattorit = r.replace("\n", "")

kaikkiaan = []
pystyt = []
for i in range(len(rivit[0]) + 1):
    if i >= len(rivit[0]):
        if nyk_operaattori == "+":
            kaikkiaan.append(sum(pystyt))
        elif nyk_operaattori == "*":
            kaikkiaan.append(prod(pystyt))
        break

    if operaattorit[i] != " ":
        nyk_operaattori = operaattorit[i]
    pysty = "".join([rivi[i] for rivi in rivit])
    if pysty == " " * len(rivit) or pysty == "\n" * len(rivit):
        if nyk_operaattori == "+":
            kaikkiaan.append(sum(pystyt))
        elif nyk_operaattori == "*":
            kaikkiaan.append(prod(pystyt))
        pystyt = []
    
    else:
        pystyt.append(int(pysty))
        continue

print(f"Kaikkien laskutoimitusten tulosten summa on {kaikkiaan}")
print(sum(kaikkiaan))
