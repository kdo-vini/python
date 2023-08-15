numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado = []
for i in numeros:
    quadrado.append(i ** 2)
print (quadrado)


## OU USANDO COMPREHENSION ##
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado = [i ** 2 for i in numeros]
print (quadrado)
