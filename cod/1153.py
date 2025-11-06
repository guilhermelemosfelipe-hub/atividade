n = int(input())
fatorial = 1
contador = n

while contador > 1:
    fatorial *= contador
    contador -= 1

print(fatorial)
