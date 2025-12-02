with open("input.txt") as f:
    rajat = f.readline().strip().split(",")

vialliset = []
for raja in rajat:
    alku, loppu = (int(luku) for luku in raja.split("-"))
    for i in range(alku, loppu + 1):
        id = str(i)
        if id[:len(id) // 2] == id[len(id) // 2:]:
            vialliset.append(int(id))

print(f"Vialliset ID:t {vialliset}")
print(f"Viallisten ID:iden summa: {sum(vialliset)}")
