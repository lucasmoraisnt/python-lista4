dinheiro = float(input("Montante: "))
juros = float(input("Juros: "))
tempo = int(input("Tempo: "))

while tempo > 0:
    dinheiro = dinheiro * (1 + juros / 100)
    tempo -= 1

print("O valor final aplicado eh de {:.2f}".format(dinheiro))