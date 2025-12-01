def rotate(pyor :str, lahto: int) -> int:
    if pyor[0] == "R":
        loppu = lahto + int(pyor[1:])
    elif pyor[0] == "L":
        loppu = lahto - int(pyor[1:])
    valmis = loppu % 100
    if loppu < 0:
        valmis = loppu + ((2 + (loppu // 100)) * 100)
    
    return valmis 

taulu = 50
nollia = 0
muita = 0

with open("input.txt") as f:
    for r in f:
        vanha = taulu
        taulu = rotate(r.strip(), taulu) % 100
        if taulu == 0:
            nollia += 1
        else:
            muita += 1
        
        # print(f"Käännetään {vanha} - {r.strip()} = {taulu}")
        
print(f"\nNollia oli {nollia}")
    
    
        
    
