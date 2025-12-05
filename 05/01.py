with open("input.txt") as f:
    tuoreiden_rajat = []
    ainekset = []
    for r in f:
        if r == "\n":
            break
        tuoreiden_rajat.append(tuple((int(luku) for luku in r.strip().split("-"))))
    for r in f:
        ainekset.append(int(r.strip()))

    print(tuoreiden_rajat)
    print(ainekset)

tuoreet = []
for aine in ainekset:
    tuore = False
    for (alku, loppu) in tuoreiden_rajat:
        if aine >= alku and aine <= loppu:
            tuore = True
            break
    if tuore:
        tuoreet.append(aine)

print(f"Tuoreita aineksia oli {len(tuoreet)}")
