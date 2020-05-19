"""
	Entrada
Pedir la información de la cantidad de cada producto

	Proceso
Ordenar los datos en una lista

Ordenar la lista de menor a mayor usando sort()

	Salida

Imprimir la lista
"""
lista=[]
producto=True
while producto==True:

	temp=[]
	total = 0
	desc=input("Nombre del producto: ")
	temp.append(desc)
	precio=input("Cantidad del producto: ")
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

print (l)