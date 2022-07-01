soma = 0
divisor = 1

num = int(input("Informe um numero: "))

while divisor  < num:
    if num % divisor == 0:
        soma += divisor
    divisor += 1

if soma == soma:
    print(num, " e perfeito")
else:
    print(num, " não eh perfeito")
