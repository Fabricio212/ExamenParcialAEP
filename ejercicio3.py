cantidad = int(input("cuantos productos va ingresar?"))

lista = []

for i in range(cantidad):
    num = str (i + 1)
    nombre = input("ingrese nombre del producto " + num + ":")
    precio = float(input("ingrece precio " + num + ":"))
    categoria = input("ingrese categoria " + num + ":")

    producto =[nombre, precio, categoria]
    lista.append(producto)

#cantidad de prod en el catalo
print(len(lista)) 

#recio prom del catalogo
suma = 0
for producto in lista:
    suma = suma + producto[1]
promedio = suma / cantidad
print("el precio del promedio es: ", promedio)

#cant de produc q superan el rpecio prom del catalogo
contador = 0
for producto in lista:
    if producto[1] > promedio:
        contador = contador + 1

print("cantidad de productos que superan el precio promedio: ", contador)

#producto mas caro
mas_caro = lista[0]

for producto in lista:
    if producto[1] > mas_caro[1]:
        mas_caro = producto
print("el producto mas caro es: ", mas_caro)

#producto mas barato
mas_barato = lista[0]

for producto in lista:
    if producto[1] > mas_barato[1]:
        mas_barato = producto
print("el producto mas barato es: ", mas_barato)

#categoria con mas producto

categorias = []
cantidades = []

for p in lista:
    categoria = p [2]
    if categorias.count(categoria) == 0:
        categorias.append(categoria)
        cantidades.append(0)
    else:
        pos = categorias.index(categoria)
        cantidades[pos] = cantidades[pos] + 1

num_mas_alto = max(cantidades)
pos_num_mas_alto = cantidades.index(num_mas_alto)
categoria_con_mas_productos = categorias[pos_num_mas_alto]

print("categoria comn mas prodructos: ", categoria_con_mas_productos)