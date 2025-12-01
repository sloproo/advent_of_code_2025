def rotate(pyor :str, lahto: int) -> int:
    if pyor[0] == "R":
        loppu = lahto + int(pyor[1:])
        valmis = loppu % 100
        # print(valmis)    
        return valmis
    if pyor[0] == "L":
        loppu = lahto - int(pyor[1:])
        if loppu < 0:
            valmis = loppu + ((2 + (loppu // 100)) * 100)
        else:
            valmis = loppu
        # print(valmis)
        return valmis

taulu = 50
nollia = 0
with open("input.txt") as f:
    for r in f:
        taulu = rotate(r.strip(), taulu)
        if taulu == -100:
            print("SATA")
        if taulu == 0:
            nollia += 1
            # print("Nollakohta")

print(f"Nollia oli {nollia}")
    
    
        
    
