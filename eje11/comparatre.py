print("opcion 1: divisores")
print("opcion 2: compara 3 numeros")
opcion = int(input("ingrese opcion: "))
if opcion == 1:
    print("introduzca el numero")
    numero = int(input())
    contador = 0
    print("los divisores de ",numero)
    for divisor in range(1,numero+1):
        if (numero % divisor) == 0 :
            print(divisor,"es divisor")
            contador += 1
    print("el numero ",numero," tiene ",contador," divisores")
if opcion == 2:
    n1 = input("¿Dime el primer número?")
    n1 = int(n1)
    n2 = input("¿Dime el segundo número?")
    n2 = int(n2)
    n3 = input("¿Dime el tercer número?")
    n3 = int(n3)
    if n1 == n2 == n3:
        print ("los tres números son iguales")
    else:
        print("no son iguales los tres números")
else :
    print("ninguna opcion eleigda fin")
