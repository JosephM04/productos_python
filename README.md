﻿# productos_python
Programa donde se preguntarán los datos de algún producto, luego de terminar los datos de un producto, se le preguntará si quiere agregar otro producto, si el usuario ingresa "si" o "sí" entrará nuevamente al ciclo para agregar mas productos, en caso de que ya no quiera más productos, al escribir cualquier cosa que no sea "si" o "sí", saldrá del ciclo y se harán los calculos de cada producto y los irá imprimiendo y habrá una variable que guardará el total de la compra y la se imprimirá al final del programa.

Funcionamiento:
Primero se crean las listas para cada valor, y los productos se iran ligando segun el indice de la lista
Estas listas son:
codigo_de_producto
nombre_de_producto
cantidad
precio_unidad
porcentaje_de_descuento
porcentaje_de_impuesto

se declara una variable pregunta = "si" para entrar al menos una vez al ciclo while (se podría hacer un 'do while' pero para no repetir dos veces el codigo elegí hacerlo así
luego la pregunta se convierte toda a minuscula con lower() y se eliminan los espacios en blanco al inicio y al final con strip() (en caso de que tenga, sino no hay cambios), así entrará al ciclo en caso de que se ingrese si con maysculas o minusculas o con espacios iniciales o finales

Dentro del ciclo while se ingresa a cada lista con append() el valor de cada lista
y al terminar de ingresar todo se pregunta si quiere agregar más productos y se guarda en la variable pregunta y se vuelve a usar lower() y strip().
Si quiere agregar más productos vuelve al ciclo, sino sale y ejecuta un for donde va a recorrer todas las listas

Tenemos variables subtotal, descuento, impuesto y total que serán redondeada a 2 decimales y se harán los calculos con cada producto y se guardarán en ellas para luego imprimirlas

y por ultimo a total_de_la_compra se le sumará el total (donde esta es la variable temporal que almacena el total del producto ingresado) para imprimir al final del ciclo el total de la compra de todos los productos.

