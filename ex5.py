n = int(input("Contar divisores: "))
conta = 0

div = 1

while div <= n:
    if n % div == 0:
        conta = conta + 1

print("{} e a qtd de divisores de {}".format(conta, n))
