N = int(input())  # quantidade de casos de teste

dentro = 0
fora = 0

for _ in range(N):  # apenas um conjunto de IF e ELSE
    X = int(input())
    if 10 <= X <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out")
