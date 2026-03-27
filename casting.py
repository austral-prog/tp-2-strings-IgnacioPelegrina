def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int(input("precio:"))
    descuento = float(input("descuento:"))
    cantidad = int(input("cantidad:"))
    precio_descuento = precio - descuento
    precio_total = precio_descuento * cantidad
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_descuento}")
    print(f"Total: {precio_total}")