pares = 0

for _ in range(5):  # lê 5 valores
    valor = int(input())
    if valor % 2 == 0:  # apenas UM IF
        pares += 1

print(f"{pares} valores pares")
