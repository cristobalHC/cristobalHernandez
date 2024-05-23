P= float(input("ingrese el número de personas: "))
N = 1
suma = 0
while N <= P:
    Altura = float(input("ingrese una altura: "))
    suma = suma + Altura
    N += 1
print("el promedio de la altura es de: ", suma / N )