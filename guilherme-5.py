num1 = float(input('Digite o primeiro número: \n'))

while(True):
    num2 = float(input('Digite o segundo número: \n'))

    if(num2 == 0):
        print('Não é possível divisão por zero. Tente novamente')
    else:
        break

resultado = num1 / num2

print(f'Resultado: {resultado}')

