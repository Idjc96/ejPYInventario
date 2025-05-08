from mostrarInventario import mostrar_inventario
from agregarInventario import agregar_producto


# Inventario inicial
inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20
}

print("Inventario inicial:")
mostrar_inventario(inventario)

# Acciones

agregar_producto(inventario, 'bananas', 40)


print("\nInventario final:")
mostrar_inventario(inventario)