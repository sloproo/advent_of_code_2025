def rotate(pyor :str, alku: int) -> tuple[int, int]:
    suunta = pyor[0]
    if suunta == "R":
        kaannos = int(pyor[1:])
    elif suunta == "L":
        kaannos = -int(pyor[1:])
    nollia = abs(kaannos) // 100
    loppu = (alku + kaannos) % 100

    if loppu == 0:
        nollia += 1
    elif (suunta == "R" and loppu < alku) or (alku != 0 and suunta == "L" and loppu > alku):
        nollia += 1
    return (loppu, nollia)
    

taulu = 50
nollia = 0

with open("input.txt") as f:
    for r in f:
        vanha = taulu
        taulu, uusia_nollia = rotate(r.strip(), taulu)
        nollia += uusia_nollia
        
        # print(f"Käännetään {vanha} - {r.strip()} = {taulu}")
        # print(f"Uusia nollia tuli {uusia_nollia}")
        
print(f"\nNollia oli yhteensä {nollia}")
    
    
        
    
