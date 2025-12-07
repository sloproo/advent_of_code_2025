with open("input.txt") as f:
    jakaja =[r.strip() for r in f]

sateet = {jakaja[0].find("S")}
halkaisuja = 0

for r in jakaja:
    uudet_sateet = set()
    for sade in sateet:
        if r[sade] == "^":
            uudet_sateet.update({sade-1, sade+1})
            halkaisuja += 1
        else:
            uudet_sateet.add(sade)
    sateet = uudet_sateet

print(halkaisuja)
    