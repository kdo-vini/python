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