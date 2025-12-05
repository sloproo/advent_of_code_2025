with open("input.txt") as f:
    rajat = []
    for r in f:
        if r == "\n":
            break
        rajat.append(tuple((int(luku) for luku in r.strip().split("-"))))

rajat.sort()


yhdistetyt = [rajat[0]]
for i in range(1, len(rajat)):
    eka = rajat[i][0]
    toka = rajat[i][1]
    if yhdistetyt[-1][1] + 1 >= eka:
        print(f"Yhdistetään {yhdistetyt[-1]} ja {rajat[i]}")
        eka = min(yhdistetyt[-1][0], eka)
        toka = max(yhdistetyt[-1][1], toka)
        yhdistetyt[-1] = (eka, toka)
        muutoksia = True
    else:
        print(f"{yhdistetyt[-1]} ja {rajat[i]} eivät leikkaa, lisätään jälkimmäinen")
        yhdistetyt.append(rajat[i])
rajat = yhdistetyt.copy()


tuoreita = 0
for alue in yhdistetyt:
    # print(f"Alueelta {alue[0]} - {alue[1]} tulee tuoreita yhteensä {alue[1] - alue[0] + 1}")
    tuoreita += alue[1] - alue[0] + 1

print(f"Tuoreita mahdollisia ID:itä on: {tuoreita}")
