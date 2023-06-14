#Elecion de la maquina
import random

num_rand =random.randint(1,3)
if num_rand==1:
    choice_maq ='piedra'
elif num_rand==2:
    cheice_maq ='papel'
else:
    choice_maq ='Tijeras'

#Elecion de usuario
choice_text = '''
Escribe una opcion:
piedra
papel
Tijeras
'''

#imorime selecicon
print("Usuario elige:", choice_user)
print("maquina elige:", choice_maq)
# Define Ganador 
if choice_user == choice_maq:
    print("Es un empate!")

else:

if choice_user =='piedra' and choice_maq =='papel':
    print("Gana MAquina!")
   
if choice_user =='piedra' and choice_maq =='Tijeras':
    print("Gana usuario!")
   
if choice_user =='papel' and choice_maq =='piedra':
    print("Gana Usuario!")
   
if choice_user =='papel' and choice_maq =='Tijeras':
    print("Gana MAquina!")
   
if choice_user =='Tijeras' and choice_maq =='piedras':
    print("Gana MAquina!")
else:
        print("Ganan usuario!")
   
   