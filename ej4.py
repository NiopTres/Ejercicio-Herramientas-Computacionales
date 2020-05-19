"""
	Entrada
Introducir el primer producto.
	Pedir la descripción
	Precio

	Proceso
Calcular el IVA del Producto

Agregar el producto a una lista temporal.

Preguntar si hay otro producto (True/False)

Repetir el mismo proceso hasta que no haya mas productos
	
Agregar cada lista de productos a una lista general

	Salida

Imprimir la lista
"""


factura=[]
producto=True
while producto:

	temp=[]
	total = 0
	desc=input("Descripción del producto: ")
	temp.append(desc)
	precio=int(input("Precio del producto: "))
	temp.append(precio)
	iva=precio*(8/100)
	temp.append(iva)
	
	factura.append(temp)
	
	total=total+(precio+iva)

	while True:
		p=input("Siguiente producto? Si/No: ")
		if p.strip() == "Si":
			producto=True
			break
		elif p.strip() == "No":
			producto=False
			break
	


print (factura)
