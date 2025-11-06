while True:
    notas_validas = 0
    soma = 0.0

    while notas_validas < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            soma += nota
            notas_validas += 1
        else:
            print("nota invalida")

    media = soma / 2
    print(f"media = {media:.2f}")

    print("novo calculo (1-sim 2-nao)")
    x = int(input())

    while x != 1 and x != 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())

    if x == 2:
        break
