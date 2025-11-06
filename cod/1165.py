n = int(input())

for _ in range(n):
    x = int(input())
    eh_primo = True
    i = 2

    while i < x:
        if x % i == 0:      # if 1
            eh_primo = False
            break            # obrigatório
        i += 1

    if x == 1:              # if 2
        eh_primo = False

    if eh_primo:            # if 3
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
