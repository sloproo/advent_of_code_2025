import os

for i in range(1, 13):
    try:
        os.mkdir(f"{i :02d}")
    except OSError:
        print(f"Hakemisto {i :02d} oli jo")
    else:
        print(f"Hakemisto {i :02d} luotu")
    for j in range(1, 3):
        if not os.path.exists(f"{i :02d}/{j :02d}.py"):
            try:
                with open(f"{i :02d}/{j :02d}.py", mode="w") as f:
                    f.write("# alku\n")
            except OSError:
                print(f"Virhe tiedoston {i :02d}/{j :02d}.py tekemisessä")
    if not os.path.exists(f"{i :02d}/alku.txt"):
        try:
            with open(f"{i :02d}/alku.txt", mode="w") as f:
                f.write("# alku\n")
        except OSError:
            print(f"Virhe tiedoston {i :02d}/alku.txt tekemisessä")
            
            
