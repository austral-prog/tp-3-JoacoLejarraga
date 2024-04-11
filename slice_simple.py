def slice_simple():
	texto = "Awesome"
	mitad_texto = int(len(texto)/2)

	print(texto[0:3].lower())
	print((texto[mitad_texto-1]+texto[mitad_texto]+texto[mitad_texto+1]).lower())
	print((texto[0:4]+texto[len(texto)-3:len(texto)]).lower())
