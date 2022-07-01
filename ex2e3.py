soma = 0 
n = int(input("Informe a qtd de alunos: "))
conta = 1

contaMenos5 = 0
contaMais5 = 0

while conta <= n:
    nota = float(input("Informe a nota do aluno: "))
    soma = soma + nota
    if nota < 5:
        contaMenos5 = contaMenos5 + 1
    else:
        contaMais5 = contaMais5 + 1

media = soma / n
print("A media da turma e {}".format(media))
print("{} foi a qtd de alunos que tiraram menos que 5".format(contaMenos5))
print("{} foi a qtd de alunos que tiraram mais ou igual a 5".format(contaMais5))
