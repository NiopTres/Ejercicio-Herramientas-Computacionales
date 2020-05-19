NotaParcial1 = int(input("Nota primer Parcial: "))
NotaParcial2 = int(input("Nota segundo Parcial: "))
NotaTaller = int(input("Nota del Taller: "))
NotaProyecto = int(input("Nota del Proyecto: "))


Parcial1 = NotaParcial1*(25/100)
Parcial2 = NotaParcial2*(25/100)
Taller = NotaTaller*(20/100)
Proyecto = NotaProyecto*(30/100)


nota_final = Parcial1 + Parcial2 + Taller + Proyecto


print (nota_final)

"""
	Entrada
Ingresar los valores de las notas:
Nota Primer Parcial
Nota Segundo Parcial
Nota Taller
Nota Proyecto

	Proceso
Calcular el valor del porcentaje de cada nota:
Porcentaje Parcial 1=Nota Pirmer Parcial * 25%
Porcentaje Parcial 2=Nota Segundo Parcial * 25%
Porcentaje Taller=Nota Taller * 20%
Porcentaje Proyecto=Nota Proyecto * 30%

Calcular la nota final sumando la suma de los porcentajes:
Nota Final = Porcentaje Parcial 1 + Porcentaje Parcial 2 + Porcentaje Taller + Porcentaje Proyecto

	Salida
Devolver la Nota Final

"""
