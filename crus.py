comidas=[]
def show_comidas():
    for comida in comidas:
        print(f"comida{comida}")

def add_comida(comida):
    comidas.append(comida)

def del_comida(comida):
    comidas.remove(comida)
text_menu='''

Elige una opcion:
1- Agregar comida
2- Eliminar comida
3- mostra comidas 
4- salir 
'''



while True:
    choice_user = int(input(text_menu))
    if choice_user== 1: 
        comida = input("Escribe una comida: ")
        add_comida(comida)

        if choice_user== 2: 
            comida = input("Escribe una comida: ")
        add_comida(comida)

        if choice_user== 3:
            show_comidas()
        if choice_user== 4:
            break
        else:
            print("Escribe bien ")


