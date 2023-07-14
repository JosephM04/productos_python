# Creando las listas
codigo_del_producto = []
nombre_del_producto = []
cantidad = []
precio_unidad = []
porcentaje_de_descuento = []
porcentaje_de_impuesto = []
total_de_la_compra = float(0)

pregunta = "si"
#lower() convierte los caracteres a minusculas, strip() quita los espacios en blanco del inicio y al final del string
pregunta = pregunta.lower().strip() 
# Se valida que si se escribe si con tilde o sin tilde igual entre al ciclo
while pregunta == "si" or pregunta == "sí":
  #append agrega el valor despues del ultimo valor de la lista
  codigo_del_producto.append(int(input('Ingresa el codigo del producto: ')))
  nombre_del_producto.append(str(input('Ingresa el nombre del producto: ')))
  cantidad.append(int(input('Ingresa la cantidad del producto: ')))
  precio_unidad.append(float(input('Ingresa el valor de precio unidad: ')))
  porcentaje_de_descuento.append(float(input('Ingresa el porcentaje de descuento: ')))
  porcentaje_de_impuesto.append(float(input('Ingresa el porcentaje de de impuesto: ')))
  pregunta = str(input("¿Desea agregar más productos?"))
  pregunta = pregunta.lower().strip()
else:
  #hacer la impresión en un rango, segun los valores que tenga la lista codigo_del_producto
  for x in range(len(codigo_del_producto)): 
    #Para redondear los numeros a solo dos decimales se usa round(valor, numero de decimales que se quiere)
    subtotal = round(cantidad[x] * precio_unidad[x], 2)
    descuento = round(subtotal*porcentaje_de_descuento[x]/100, 2)
    impuesto = round((subtotal-descuento)*porcentaje_de_impuesto[x]/100, 2)
    total = round(subtotal-descuento+impuesto , 2) 
    print(f"\nCODIGO DEL PRODUCTO: {codigo_del_producto[x]}\nNombre del producto: {nombre_del_producto[x]}\nCantidad: {cantidad[x]}\nPrecio por unidad: {precio_unidad[x]}$\nSubtotal: {subtotal}$\nDescuento: {descuento}$\nImpuesto: {impuesto}$\n\n Total en {nombre_del_producto[x]}(s/es): {total}$\n --------------------")
   
    total_de_la_compra = round(total_de_la_compra + total, 2)
  
print(f"\nTOTAL DE LA COMPRA: {total_de_la_compra}$\nMuchas Gracias por preferirnos, MWBO ;)")
