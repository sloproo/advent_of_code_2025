with open("input.txt") as f:
    rajat = f.readline().strip().split(",")

vialliset = []
for raja in rajat:
    alku, loppu = (int(luku) for luku in raja.split("-"))
    for i in range(alku, loppu + 1):
        jakajat = [jakaja for jakaja in range(1, len(str(i))) if len(str(i)) % jakaja == 0]
        for j in jakajat:
            id = str(i)
            if id[:j] * (len(id) // j) == id:
                vialliset.append(int(id))
                break

print(f"Viallisten ID:iden summa: {sum(vialliset)}")
