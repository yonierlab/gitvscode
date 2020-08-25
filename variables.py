lista = ["amarillo", "azul", "rojo"]

for lab in lista:
    print(lab)

lista[0] = "Verde"

print(f"Se cambia el color amarillo por {lista[0]}")

lista.append("negro")

print("Se añade un nuevo color {}".format(lista))

print("Imprimiendo con el bucle for")
for lab in lista:
    print(lab)

print(f"Imprimiendo número de elementos que son {len(lista)}")