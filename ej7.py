"""
	Entrada
Identificar lista o crear la lista de estudiantes y promedios

	Procdeso
Ordenar la lista de estudiantes de mayor a menor promedio
Identificar el primer elemento de la lista

	Salida

Retornar el nombre y el promedio del estudiante

	
"""
lista=[]
producto=True
while producto==True:

	temp=[]
	total = 0
	desc=input("Nombre del estudiante: ")
	temp.append(desc)
	precio=input("Promedio del estudiante: ")
	temp.append(precio)
	
	lista.append(temp)
	
	

	while True:
		p=input("Siguiente producto? Si/No: ")
		if p.strip() == "Si":
			producto=True
			break
		elif p.strip() == "No":
			producto=False
			break
l=sorted(lista, key = lambda r: r[1], reversed=True)

print (l[0])
