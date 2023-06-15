#Funciones
#def name_function():
#   code

#Funciones sin parametros 
#Fuinciones sin retornos

def saluda():
    print("hola developers!")

    saluda() 

#parametros, siin retorno 
def duplica(number):
    print(number *2)

    duplica(23)

def suma(num1, num2):
        print(num1 + num2)
        suma(12,34)

#parametros opcionales 
def lista_drinks(d1="beer",d2= "water"):
    print(d1)
    print(d2)

    lista_drinks("tequila","juice")
    lista_drinks("tequila")
    lista_drinks()
    lista_drinks(f2='soda',d1="vodka")


    #Funciones con retornos 
    #return

def get_list():
    return [1,2,3,]

list_gotten = get_list()
print(list_gotten)

def resta(num1, num2):
    return num1 - num2
result =resta (13,2)
print(result)

def duplicar_lista(lista):
    new_list =[]
    for item in list:
        new_list.append(item=2)
        return 
my_list=[1,2,3,4,5]
print(my_list)
new_list = duplicar_lista(my_list)
print(new_list)




