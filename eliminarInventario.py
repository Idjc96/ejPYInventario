def eliminar_producto(inventario, producto):
    try:
        if producto not in inventario:
            raise KeyError(f"El producto '{producto}' no existe.")
        del inventario[producto]
        print(f"Eliminando '{producto}'...")
    except KeyError as e:
        print(f"Error: {e}")

 