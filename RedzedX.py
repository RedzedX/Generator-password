#Generador De Contraseñas 
#Generator of password

import random


minus = "abcdefghijklmnñopqrstuvwxz"
mayus = minus.upper()
numbers = ("123456789")
simbols = ("!#$%&/()=?¡*][")

base = minus+mayus+numbers+simbols
lenght = 10  ###password length

for _ in range(100):
 M1 = random.sample(minus, lenght) ###Put base if you want
 password = "".join(M1)
 print(password)

 

 ######RedzedX#######
