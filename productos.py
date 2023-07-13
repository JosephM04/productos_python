"""
# codigo_del_producto = input('Ingresa el codigo del producto: ')
# nombre_del_producto = input('Ingresa el nombre del producto: ')
# cantidad = float(input('Ingresa la cantidad de compra del producto: '))
# precio_unidad = float(input('Ingresa el valor de precio unidad: '))
# porcentaje_de_descuento = float(input('Ingresa el valor de porcentaje de descuento: '))
# porcentaje_de_impuesto = float(input('Ingresa el valor de porcentaje de impuesto: '))
# subtotal = cantidad*precio_unidad
# descuento = subtotal*porcentaje_de_descuento/100
# impuesto = (subtotal-descuento)*porcentaje_de_impuesto/100
# total = subtotal-descuento+impuesto
# print('Codigo del producto: ' + codigo_del_producto)
# print('Nombre del producto: ' + nombre_del_producto)
# print('Valor de subtotal: ' + repr(subtotal))
# print('Valor de descuento: ' + repr(descuento))
# print('Valor de impuesto: ' + repr(impuesto))
# print('Valor de total: ' + repr(total))
# print("Gracias por su compra misera arrastrada")
"""

# Creando las listas
codigo_del_producto = []
nombre_del_producto = []
cantidad = []
precio_unidad = []

pregunta = "si"
pregunta = pregunta.lower().strip() #lower() convierte los caracteres a minusculas, strip() quita los espacios en blanco del inicio y al final del string

while pregunta == "si" or pregunta == "sí": # se valida que si se escribe si con tilde o sin tilde igual entre al ciclo
  codigo_del_producto.append(int(input('Ingresa el codigo del producto: '))) #append agrega el valor despues del ultimo valor de la lista
  nombre_del_producto.append(str(input('Ingresa el nombre del producto: ')))
  cantidad.append(int(input('Ingresa la cantidad del producto: ')))
  precio_unidad.append(float(input('Ingresa el valor de precio unidad: ')))
  
  pregunta = str(input("¿Desea agregar más productos?"))
  pregunta = pregunta.lower().strip()
else:
  for x in range(len(codigo_del_producto)): #hacer la impresión en un rango, segun los valores que tenga la lista codigo_del_producto
    codigo = "Codigo del Producto: {}, nombre del producto: {}, cantidad: {}, Precio por unidad: {}"
    print(codigo.format(codigo_del_producto[x], nombre_del_producto[x], cantidad[x], precio_unidad[x])) 
    """
    los productos se relacionan segun su indice, por ejemplo: codigo_de_producto[0] = 102
    y nombre_del_producto[0]= zapatillas y así sucesivamente
    """