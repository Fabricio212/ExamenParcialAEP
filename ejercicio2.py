#hacer q el sisteme un numero aleatorio entre 1 y 10. luego hacer q 
# el usuario adivine el numero. la aplicacion debe termenar cuando el 
# usuario adivine.

import random

s = random.randint(1, 10)

while True:
    n = int(input("adivina el numero del sistema (1... 10): "))
    if n == s:
        print("adivinaste!")
        break
    else:
        print("numero incorrecto!")