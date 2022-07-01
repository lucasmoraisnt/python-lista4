numero = 2464215017

dcDigitado = numero % 10
numero = numero // 10
soma = 0
fator = 2
while numero != 0:
    dig = numero % 10
    dig *= fator
    valor = (dig // 10) + (dig % 10)
    soma += valor
    numero //= numero
    if fator == 2:
        fator = 1
    else: 
        fator = 2

resto = soma % 10
dcCaculado = 0
if resto > 0:
    dcCaculado = 10 - resto

if dcDigitado == dcCaculado:
    print("Parabens, tudo certo!")
else: 
    print("Algo deu errado!")