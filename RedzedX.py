#Generador De Contraseñas 
#Generator of password

import random


minus = "abcdefghijklmnñopqrstuvwxz"
mayus = minus.upper()
numeros = ("123456789")
simbolos = ("!#$%&/()=?¡*][")

base = minus+mayus+numeros+simbolos
longitud = 10 

for _ in range(100):
 M1 = random.sample(minus, longitud)
 contraseña = "".join(M1)
 print(contraseña)

 

 ######RedzedX#######