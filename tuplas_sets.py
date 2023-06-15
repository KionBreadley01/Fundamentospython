#mas coleciones en python 

#tuplas

#(itm1, item2, item3)
#listas son mutables 
#tuplas onmutables 
my_tupla=(1,"dos",3.1,True)
print(type(my_tupla))

print(my_tupla)
print(my_tupla[0])
print(my_tupla[-1])
#Error
#my_tupla[0]="algo mas "
#conguntos setes
#desordenados
#mutable
#no permite duplicados 

my_set ={"uno","dos","tres", "uno"}
print(type(my_set))
print(my_set)
my_set.add(4)
print(my_set)

a={1, 2, 3, 4, }
b={3, 4, 5 ,6, }
print(a.inion(b))
print(a.intersection(b))



