"""
	Entrada
Introducir la cantidad de dinero a cambiar

	Proceso
Calcular la tasa de cambio a cada moneda

	euro=Cantidad/3710.12
	dolar=Cantidad/3365.07
	yenes=Cantidad/30.79

Calcular la ganancia de la casa de cambio y restarla de la cantidad de dinero
	
	Cantidad final=Cantidad Cambiada - Cantidad Cambiada*(2/100)

	Salida

Imprimir las cantidades final

"""

cantidad=int(input("Cantidad de pesos a cambiar: "))

euro=cantidad/3710.12
dolar=cantidad/3365.07
yen=cantidad/30.79

totaleuro=round(euro - euro*(2/100),2)
totaldolar=round(dolar - dolar*(2/100),2)
totalyen=round(yen - yen*(2/100),2)

print ("En Euros {0}, Dollar {1}, y Yen {2}".format(totaleuro , totaldolar, totalyen))
