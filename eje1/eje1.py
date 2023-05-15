import sys
import os
print ("ejercicio de suma dos numeros  python en docker ")
""" en local """
""" n1 = input("¿Dime el primer número?")
n1 = int(n1)
n2 = input("¿Dime el segundo número?")
n2 = int(n2) """
""" como argumentos  """
""" n1 = int(sys.argv[1])
n2 = int(sys.argv[2]) """
""" como variables de entorno """
""" n1 = int(os.environ.get('NUM1'))
n2 = int(os.environ.get('NUM2')) """
n1 = 2
n2 = 2
suma = n1 + n2
resta = n1 - n2
mul = n1 * n2
div = n1 / n2
print ("la suma es")
print (suma)
print ("la resta es")
print (resta)
print ("la multiplicacion es")
print (mul)
print ("la divicion es")
print (div)
print("el numero 2 no es mayor al numero1")