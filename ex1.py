somaPar = 0
num = int(input("Informe num da sequencia: "))

while num != 0:
    if num % 2 == 0:
        somaPar = somaPar + num
    num= int(input("Informe num da sequencia: "))

print("A soma dos pares e {}".format(somaPar))
