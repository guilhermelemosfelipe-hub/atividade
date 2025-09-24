salario = float(input())

if salario <= 2000.00:
    print("Isento")
else:
    imposto = 0.0

    if salario > 2000.00:
        valor = min(salario, 3000.00) - 2000.00
        if valor > 0:
            imposto += valor * 0.08
    else:
        imposto += 0.0

    if salario > 3000.00:
        valor = min(salario, 4500.00) - 3000.00
        if valor > 0:
            imposto += valor * 0.18
    else:
        imposto += 0.0

    if salario > 4500.00:
        valor = salario - 4500.00
        imposto += valor * 0.28
    else:
        imposto += 0.0

    print(f"R$ {imposto:.2f}")
