def halkaisu(jakaja:list, x: int, y: int, kaydyt: dict) -> int:
    aikajanoja = 0
    for r in range(y, len(jakaja)):
        if (x, y) in kaydyt:
            return kaydyt[(x, y)]
        elif jakaja[r][x] == "^":
            aikajanoja += halkaisu(jakaja, x-1, r, kaydyt)
            aikajanoja += halkaisu(jakaja, x+1, r, kaydyt)  
            kaydyt[(x, y)] = aikajanoja
            return aikajanoja
    return 1
    
with open("input.txt") as f:
    jakaja =[r.strip() for r in f]

print(halkaisu(jakaja, jakaja[0].find("S"), 0, {}))
