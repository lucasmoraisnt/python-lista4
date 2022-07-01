n = int(input("Informe a qtd de numes da sequencia: "))

conta = 1

contaPos = 0
contaNeg = 0

while conta <= n:
    num = float(input("Informe um numero da sequencia: "))
    if num < 0:
        contaNeg = contaNeg + 1
    elif num > 0:
        contaPos = contaPos + 1

print("{} foi a qtd de numeros negativos".format(contaNeg))
print("{} foi a qtd de numeros positivos".format(contaPos))
