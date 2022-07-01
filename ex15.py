n = int(input("Informe o tamanho da sequência: "))

num = int(input("Num: "))

maximo = 1
contadorMax = 1
contadorSeque = 1
anterior = num

while contadorSeque<n:
    num = int(input("Num: "))
    if num > anterior:
        contadorMax += 1
    else:
        if maximo < contadorMax:
            maximo = contadorMax
        contadorMax = 1
    anterior = num
    contadorSeque += 1
print("O segmento crescente maximo tem tamanho ", maximo)