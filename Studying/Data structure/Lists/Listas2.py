#append - adiciona valores a lista
lista = []
lista.append(1)
lista.append('Python')
print (lista)
################################
#clear - limpa a lista
lista.clear()
print (lista)
################################
#copy - copia em todos os locais q puxarem a lista ( lista1 fornece para l2, mas l2 nao muda l1.)
lista.copy()
################################
#extend - estende o tamanho da lista ja existente
lista.extend(['java','ruby','python','c','c','c#','golang'])
print (lista)
################################
#Index - acha um objeto na lista e onde ele ocorre *primeiramente*
lista.index()
################################
#pop - remove o ultimo item da lista, como se fosse uma pilha de pratos
lista.pop() #-golang
################################
#remove - remove um item
lista.remove('c')
################################
#reverse
lista.reverse()
################################
#sort - sorteia a lista
lista.sort()
lista.sort(key=lambda x: len(x)) #organiza as palavras por tamanho de escrita
lista.sort(key=lambda x: len(x), reverse=True) #reverte o anterior
################################
#len - ve o tamanho
lista.len() #6
################################
#sorted - igual o sort, mas esse é uma funçao
sorted(lista, key=lambda x: len(x))  
