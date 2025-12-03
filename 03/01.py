akusto = "234234234234278"
akut = 0
for i in range(9, 0, -1):
    ekan_paikka = akusto[:-1].find(str(i))
    for j in range(i, 0, -1):
        if str(j) in akusto[ekan_paikka + 1:]:
            akut = int(str(i) + str(j))
            break
    if akut > 0:
        break
    
print(akut)
