# 1061 - versão robusta (sem usar if/else)
import re
import sys

try:
    # linha 1 -> "Dia N"
    l1 = input().strip()
    dia_inicio = int(re.findall(r'\d+', l1)[0])

    # linha 2 -> "hh : mm : ss" ou "h m s"
    t1 = re.findall(r'\d+', input())
    h_inicio, m_inicio, s_inicio = map(int, t1)

    # linha 3 -> "Dia M"
    l3 = input().strip()
    dia_fim = int(re.findall(r'\d+', l3)[0])

    # linha 4 -> "hh : mm : ss" ou "h m s"
    t2 = re.findall(r'\d+', input())
    h_fim, m_fim, s_fim = map(int, t2)

except Exception:
    print("Entrada inválida. Use 4 linhas no formato: 'Dia N' e 'hh : mm : ss'.")
    sys.exit(1)

# converter para segundos
inicio_seg = dia_inicio*24*3600 + h_inicio*3600 + m_inicio*60 + s_inicio
fim_seg    = dia_fim  *24*3600 + h_fim*3600   + m_fim*60   + s_fim

duracao = fim_seg - inicio_seg

dias = duracao // (24*3600)
duracao = duracao % (24*3600)

horas = duracao // 3600
duracao = duracao % 3600

minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
