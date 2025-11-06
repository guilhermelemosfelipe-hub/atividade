x = int(input())
y = int(input())

if x > y:
    x, y = y, x  # if 1 para garantir ordem correta

soma = 0
atual = x

while atual <= y:
    if atual % 13 != 0:  # if 2 para ignorar múltiplos de 13
        soma += atual
    atual += 1

print(soma)
