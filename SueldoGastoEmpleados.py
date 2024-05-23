M= int(input("ingrese el número de personas: "))
E = 1
suma = 0
while E <= M:
    Mes = int(input("ingrese un monto (entre $500000 a $1500000): "))
    suma = suma + Mes
    E += 1
if Mes > 499999 and Mes <900001:
 print("La cantidad de empleados que recibe sueldo entre 500 a 900 mil es de: ", M )
else:
   if Mes > 900000:
      print("La cantidad de empleados que recibe sueldo superior a 900000 sería de:", M - E )
print("La cantidad de dinero gastado en los sueldos de los empleados es de: ", suma )