with open("alku.txt") as f:
    tuoreiden_rajat = []
    ainekset = []
    for r in f:
        if r == "\n":
            break
        tuoreiden_rajat.append(tuple((int(luku) for luku in r.strip().split("-"))))

siivotut_tuoreet = []
for alku, loppu in tuoreiden_rajat:
    for siivottu_alku, siivottu_loppu in siivotut_tuoreet:
        uusi_alku = siivottu_alku
        uusi_loppu = siivottu_loppu
        if alku < siivottu_alku and alku < siivottu_loppu and loppu >= siivottu_alku:
            uusi_alku = alku
            if loppu > siivottu_loppu and loppu > siivottu_alku and alku <= siivottu_loppu:
                uusi_loppu = loppu
        if uusi_alku != siivottu_alku or uusi_loppu != siivottu_loppu:
            siivotut_tuoreet.remove((siivottu_alku, siivottu_loppu))
            siivotut_tuoreet.append((uusi_alku, uusi_loppu))
            break
    else:
        siivotut_tuoreet.append((alku, loppu))
      

print(siivotut_tuoreet)
