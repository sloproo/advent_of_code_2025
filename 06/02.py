from math import prod

with open("input.txt") as f:
    rivit = []
    for r in f:
        if r.lstrip()[0] in "1234567890":
            rivit.append(r.replace("\n", "L"))
        else:
            operaattorit = r.replace("\n", "L")

kaikkiaan = 0
pystyt = []
for i in range(len(rivit[0])):
    if operaattorit[i] == "+" or operaattorit[i] == "*":
        nyk_operaattori = operaattorit[i]
    pysty = "".join([rivi[i] for rivi in rivit])
    
    if pysty == " " * len(rivit) or pysty == "L" * len(rivit):
        if nyk_operaattori == "+":
            kaikkiaan += sum(pystyt)
        elif nyk_operaattori == "*":
            kaikkiaan += prod(pystyt)
        pystyt = []
    else:
        pystyt.append(int(pysty))
        continue

print(f"Kaikkien laskutoimitusten tulosten summa on {kaikkiaan}")
