with open("alku.txt") as f:
    tuoreet = []
    ainekset = []
    for r in f:
        if r == "\n":
            break
        tuoreet.append(tuple((int(luku) for luku in r.strip().split("-"))))
    for r in f:
        ainekset.append(int(r.strip()))

    print(tuoreet)
    print(ainekset)

