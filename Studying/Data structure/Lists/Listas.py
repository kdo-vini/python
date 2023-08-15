#LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# C listas
notas = [7.9,9.7,8.2]

#criando listas
lista = list()
lista =[]
lista_de_listas = [1, [], 'Teste']

#indexação e slices
lista = [10, 'Vinicius', 3.1415, True]
print (lista[0])

#slices
print(lista[0:3])

#iterações com FOR

for elemento in lista:
    print(elemento)

#2. utilizando os indices
print ('comprimento da lista:',len(lista))

for i in range(len(lista)):
    print(lista[i])

# Matrizes
matriz = [
    [1, "a",  3],
    ["b", 2 , 4],
    [4 , 1 ,"c"]
]
matriz [0]
matriz [1]
matriz [1][-1]

# Filtros #
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#Filtro versão 2: comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [numero for numero in numeros   if numero % 2 == 0] #1: return, #2 for, #3 condição
