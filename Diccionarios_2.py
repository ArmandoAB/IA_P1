#Itera el diccionario teclado1 con un solo bucle for
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado1:
	print(x + ': ' + teclado1[x] + '.')
