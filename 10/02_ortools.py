from ortools.linear_solver import pywraplp

def lue(tiedosto: str) -> list:
    koneet = []
    with open(tiedosto) as f:
        for r in f:
            r = r.strip().split(" ")
            valot  = []
            valo = r[0][1:-1]
            for i in range(len(valo)):
                valot.append(int(i)) if valo[i] == "#" else i
            
            napit = []
            for nappi in r[1:-1]:
                napit.append([int(luku) for luku in nappi[1:-1].split(",")]) 

            joltit = [int(i) for i in r[-1][1:-1].split(",")]
            koneet.append({"valot": valot, "napit": napit, "joltit": joltit})
    return koneet

def matriisiksi(napit: list[list[int]], joltit: list[int]) -> tuple[tuple[tuple[int, ...]], tuple[int, ...]]:
    matriisi = []
    for nappi in napit:
        matriisi.append(tuple(1 if i in nappi else 0 for i in range(len(joltit))))
    
    return tuple(matriisi), tuple(joltit)

def ratkaise_ortools(vektorit, joltit):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return float('inf')

    # 2. LUODAAN MUUTTUJAT
    # Meillä on yhtä monta muuttujaa kuin vektoreita.
    # x[i] kertoo, montako kertaa vektoria i painetaan.
    # Arvo on kokonaisluku (IntVar) välillä 0 ... ääretön.
    x = []
    for i in range(len(vektorit)):
        x.append(solver.IntVar(0, solver.infinity(), f'x_{i}'))

    # 3. LUODAAN RAJOITTEET (Constraints)
    # Jokaista ulottuvuutta (jolt-saraketta) kohden summan pitää täsmätä.
    num_ulottuvuudet = len(joltit)
    
    for j in range(num_ulottuvuudet):
        # Rakennetaan lauseke:
        # (vektori_0[j] * x_0) + (vektori_1[j] * x_1) ... == tavoite[j]
        constraint_expr = solver.Sum([x[i] * vektorit[i][j] for i in range(len(vektorit))])
        
        # Lisätään rajoite ratkaisijaan
        solver.Add(constraint_expr == joltit[j])

    # 4. ASETETAAN TAVOITE (Objective)
    # Haluamme minimoida painallusten kokonaismäärän: sum(x)
    solver.Minimize(solver.Sum(x))

    # 5. RATKAISTAAN
    status = solver.Solve()

    # 6. TULKITAAN TULOS
    if status == pywraplp.Solver.OPTIMAL:
        # Ratkaisu löytyi! Lasketaan tulos yhteen.
        # solution_value() palauttaa floatin, pyöristetään intiksi.
        kokonaismaara = sum(int(muuttuja.solution_value()) for muuttuja in x)
        return kokonaismaara
    else:
        return float('inf')

# --- PÄÄOHJELMA ---

koneet = lue("input.txt")
ratkaisuja = 0
kone_i = 0

print("Aloitetaan ratkaisu OR-Toolsilla...")

for kone in koneet:
    vektorit, joltit = matriisiksi(kone["napit"], kone["joltit"])
    
    # Kutsu ratkaisijaa
    koneen_ratkaisu = ratkaise_ortools(vektorit, joltit)
    
    if koneen_ratkaisu != float("inf"):
        print(f"Kone {kone_i}: {koneen_ratkaisu} painallusta")
        ratkaisuja += koneen_ratkaisu
    else:
        print(f"Kone {kone_i}: Ei ratkaisua")
        
    kone_i += 1

print(f"Yhteensä: {ratkaisuja}")
