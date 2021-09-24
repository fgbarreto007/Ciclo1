#Este programa que implementa los condicionales en python
"""
Universidad Pontificia Bolivariana
Fundamentos de Programacion
"""
lista = []
reiniciar = "s"
print ("\n\t\t Universidad Pontificia Bolivariana")
print ("\n\t\t Fundamentos de Programacion")
print ("\n\t\t Este Programa genera la nomina mensual")
print ("\n\t\t Periodo: Mayo de 2021")
while (reiniciar == "s"):
    #Entradas
    cedula = input("Digite la cedula del empleado = ")
    nombre = input("Digite el nombre del empleado= ")
    salario = int(input("Digite el salario del empleado= "))
    dias = int(input("Digite los dias laborados por el empleado = "))
    nhed = int(input("Digite la cantidad de horas extras diurnas = "))
    nhen = int(input("Digite la cantidad de horas extras nocturnas = "))
    nhefd = int(input("Digite la cantidad de horas extras festivas diurnas = "))
    nhefn = int(input("Digite la cantidad de horas extras festivas nocturnas = "))
    prestamos = int(input("Digite los prestamos solicitados por el empleado = "))
    #Procesos
    if  salario >= 908526 and salario <= 1817052:  
        auxilio = 106454 / 30 * dias 
    else:
        auxilio = 0
    sueldo = salario / 30 * dias
    vhed  = salario / 240 * 1.25 *  nhed
    vhen  = salario / 240 * 1.75 *  nhen
    vhefd  = salario / 240 * 2 *  nhefd
    vhefn  = salario / 240 * 2.5 *  nhefn
    horario = input("El empleado tiene recargo nocturno s / n")
    if (horario == "s"):
        recargo_nocturno = salario * 0.35 
    else:
	    recargo_nocturno = 0
    total_devengado = round(sueldo + auxilio + vhed + vhen + vhefd + vhefn + recargo_nocturno)
    salud = (total_devengado - auxilio)  * 0.04
    pension = (total_devengado - auxilio)  * 0.04
    if  salario >= 3634104 and salario <= 14536416:
        fondo_solidaridad = salario * 1 // 100 
    elif  salario >14536416 and salario<=15444942: 
	    fondo_solidaridad = salario * 1.2 // 100
    elif  salario >15444942 and salario<=16353439:
	    fondo_solidaridad = salario * 1.4 // 100
    elif  salario >16353439 and salario<=17261964: 
	    fondo_solidaridad = salario * 1.6 // 100
    elif  salario >17261964 and salario<=18170520: 
	    fondo_solidaridad = salario * 1.8 // 100
    elif  salario >=18170520:
        fondo_solidaridad = round(salario * 2 / 100)
    else:   
        fondo_solidaridad = 0
    total_deducido= round(salud + pension + prestamos + fondo_solidaridad)	
    neto_pagado = round(total_devengado - total_deducido)
    lista.append(cedula)
    lista.append(nombre)
    lista.append(salario)
    lista.append(dias)
    lista.append(sueldo)
    lista.append(nhed)
    lista.append(nhen)
    lista.append(nhefd)
    lista.append(nhefn)
    lista.append(vhed)
    lista.append(vhen)
    lista.append(vhefd)
    lista.append(vhefn)
    lista.append(recargo_nocturno)
    lista.append(total_devengado)
    lista.append(salud)
    lista.append(pension)
    lista.append(prestamos)
    lista.append(fondo_solidaridad)
    lista.append(total_deducido)
    lista.append(neto_pagado)
    reiniciar= input ("Desea Liquidar otro empleado s / n = ")
    """
    print ("Universidad Pontificia Bolivariana")
    print ("Salario Semanal Empleados")
    print ("Cedula del Empleado=", cedula)
    print ("Nombre del Empleado=", nombre)
    print ("Salario =", salario)
    print ("Prestamos =", prestamos)
    print ("Devengado")
    print ("Sueldo =", sueldo)
    print ("Numero de Horas Extras Diurnas =", nhed)
    print ("Valor Horas Extras Diurnas =", vhed)
    print ("Numero de Horas Extras Nocturnas =", nhen)
    print ("Valor Horas Extras Nocturnas =", vhen)
    print ("Numero de Horas Extras Festivas Diurnas =", nhefd)
    print ("Valor Horas Extras Festivas Diurnas =", vhefd)
    print ("Valor Horas Extras Festivas Nocturnas =", vhefn)
    print ("Recargo Nocturno =", recargo_nocturno)
    print ("Total Devengado =", total_devengado)
    print ("Salud =", salud)
    print ("Pension =", pension)
    print ("Fondo de Solidaridad =", fondo_solidaridad)
    print ("Total Deducido =", total_deducido)
    print ("Neto Pagado =", neto_pagado)
    """
print("Lista Con Datos", lista)
print("Metodo 1. - Buscar Datos Por cedula")
cedula = input(("Digite la cedula para mostrar Liquidacion de Nomina del Empleado"))
n = lista.index(cedula)
print ("Cedula del Empleado=", lista[n])
print ("Nombre del Empleado=", lista[n+1])
print ("Salario =", lista[n+2])
print ("Dias =", lista[n+3])
print ("Sueldo =", lista[n+4])
print ("Numero de Horas Extras Diurnas =", lista[n+5])
print ("Numero de Horas Extras Nocturnas =", lista[n+6])
print ("Numero de Horas Extras Festivas Diurnas =", lista[n+7])
print ("Numero de Horas Extras Festivas Nocturnas =", lista[n+8])
print ("Valor Horas Extras Diurnas =", lista[n+9])
print ("Valor Horas Extras Nocturnas =", lista[n+10])
print ("Valor Horas Extras Festivas Diurnas =", lista[n+11])
print ("Valor Horas Extras Festivas Nocturnas =", lista[n+12])
print ("Recargo Nocturno =", lista[n+13])
print ("Total Devengado =", lista[n+14])
print ("Salud =", lista[n+15])
print ("Pension =", lista[n+16])
print ("Prestamos =", lista[n+17])
print ("Fondo de Solidaridad =", lista[n+18])
print ("Total Deducido =", lista[n+19])
print ("Neto Pagado =", lista[n+20]) 
print("Lista Con Datos", lista)

print("Metodo 2. - Eliminar Datos Por cedula")
cedula = input(("Digite la cedula para mostrar Liquidacion de Nomina del Empleado"))
n = lista.index(cedula)
del lista[n]
del lista[n+1]
del lista[n+2]
del lista[n+3]
del lista[n+4]
del lista[n+5]
del lista[n+6]
del lista[n+7]
del lista[n+8]
del lista[n+9]
del lista[n+10]
del lista[n+11]
del lista[n+12]
del lista[n+13]
del lista[n+14]
del lista[n+15]
del lista[n+16]
del lista[n+17]
del lista[n+18]
del lista[n+19]
del lista[n+20] 

print("Lista Despues del Borrado", lista)
