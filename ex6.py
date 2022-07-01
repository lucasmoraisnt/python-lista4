nota = int(input("Cand: "))
maior = nota
menor = nota

conta = 2

contaAte20 = 0
conta20a50 = 0
contaAcima50 = 0

while conta <= 70:
    nota = int(input("Cand: "))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    
    if nota <= 20:
        contaAte20 = contaAte20 + 1
    elif nota <= 50:
        conta20a50 = conta20a50 + 1
    else:
        contaAcima50 = contaAcima50 + 1
    
    conta = conta + 1

print("A maior nota eh", maior)
print("A menor nota eh", menor)

print("Ate 20 questões {:.2f}".format(contaAte20 * 100 / 70))
print("Entre 20 e 50 questões {:.2f}".format(conta20a50 * 100 / 70))
print("Acima de 50 questões {:.2f}".format(contaAcima50 * 100 / 70))
