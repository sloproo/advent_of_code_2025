with open("input.txt") as f:
    palat = []
    for r in f:
        if r == "\n":
            continue
        if r[1] == ":":
            palanro = int(r[0])
            pala = [f.readline().strip() for _ in range(3)]
            palat.append(pala)
        if palanro == 5:
            f.readline()
            break
    kuuset = []
    for r in f:
        kenttapuoli, palapuoli = r.split(": ")
        ala = tuple(int(x) for x in kenttapuoli.split("x"))
        palat = [int(l) for l in palapuoli.strip().split(" ")]
        kuuset.append((ala, palat))

pass
