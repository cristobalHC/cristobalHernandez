Preg1= float(input("ingrese total de preguntas hechas:"))
Preg2= float(input("ingrese total de preguntas correctas:"))
mult= Preg2*100
porcentaje= mult/Preg1
if porcentaje<40:
    print("Fuera del nivel")
else:
 if porcentaje>39 and porcentaje<70:
    print("nivel regular")
 else:
    if porcentaje>69 and porcentaje<95:
       print("Nivel medio")
    else:
       if porcentaje>94:
          print("Nivel Máximo")