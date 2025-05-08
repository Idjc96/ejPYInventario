def actualizar_producto(inventario, producto, nueva_cantidad):
    try:
        if producto not in inventario:
            raise KeyError(f"El producto '{producto}' no existe.")
        inventario[producto] = nueva_cantidad
        print(f"Actualizando stock de '{producto}' a {nueva_cantidad}...")
    except KeyError as e:
        print(f"Error: {e}")