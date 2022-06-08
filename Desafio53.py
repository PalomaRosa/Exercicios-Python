# Analisador completo

# Programa que irá ler o nome, idade e sexo de 4 pessoas. E no final do programa, irá exibir
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somapess = 0
somaida = 0
total = 0
totfem = 0
maisvelho = 0
nomevelho = ''

for pessoa in range(1,5):
    print('-'*5, '{}ª pessoa'.format(pessoa), '-'*5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    somapess += 1
    somaida += idade

    if sexo == 'M' and pessoa == 1:
        maisvelho = idade
        jovem = idade
        nomevelho = nome

    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        totfem += 1


mediaida = somaida / pessoa
print('\nA média de idade do grupo é de {} anos'.format(mediaida))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totfem))



