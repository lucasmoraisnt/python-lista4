import random

sorteado = random.randint(1, 1001)
tentativas = 1
chute = int(input("Tentativa: "))

while chute != sorteado:
    if chute < sorteado:
        print("Tente um número maior!")
    elif chute > sorteado:
        print("Tente um número menor!")
    chute = int(input("Tentativa: "))
    tentativas += 1
print("Parabens, você acertou!")
print(tentativas, " chutes")