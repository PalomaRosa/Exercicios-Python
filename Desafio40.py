#Calculo de IMC

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc <= 25:
    print('Você está no seu peso ideal!')
elif imc <= 30:
    print('Você está em SOBREPESO!')
elif imc <= 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE Mórbida!')
