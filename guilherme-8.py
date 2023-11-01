tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Imprimindo até o 4º elemento
print(f'Imprimindo até o 4º elemento: {tupla[:4]}')

# Imprimindo os números pares
print(f'Imprimindo os números pares: {tuple([num for num in tupla if num % 2 == 0])}')

# Imprimindo os números da tupla em order inversa
print(f'Imprimindo a tupla em ordem inversa: {tupla[::-1]}')