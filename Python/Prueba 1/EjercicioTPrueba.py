producto = input("Ingrese nombre del producto: ").lower()
dinero_usuario = int(input("Ingrese el dinero que dispone: "))
precio_producto = int(input("Ingrese el precio del producto: "))
iva_producto = precio_producto * 1.19
iva = precio_producto * 0.19
print("El producto que desea comprar cuesta:")
print("Precio + IVA =", "$" + str(int(iva_producto)))
print("IVA del producto =", "$" + str(int(iva)))
edad_usuario = int(input("Ingresa tu edad: "))
if edad_usuario <= 18 or (edad_usuario > 50 and edad_usuario <= 70):
    descuento=0.05
elif edad_usuario > 18 and edad_usuario <= 50:
    descuento=0
else:
    descuento=0.1
precio_descuento = iva_producto * (1-descuento)
descuento_producto = iva_producto * descuento
print("El precio con descuento es", "$" + str(int(precio_descuento)))
print("Hemos aplicado el siguiente descuento:", "$" + str(int(descuento_producto)))
metodo_pago = input("Ingrese el método de pago: ").lower()
if metodo_pago == "efectivo":
    precio_descuento=precio_descuento
elif metodo_pago == "debito":
    precio_descuento=precio_descuento*(1-0.05)
elif metodo_pago == "crédito":
    precio_descuento=precio_descuento*(1-0.08)
elif metodo_pago == "cheque":
    precio_descuento = precio_descuento*(1-0.06)
print("El costo final del producto es:", "$" + str(int(precio_descuento)))
puede_comprar=dinero_usuario-precio_descuento
if puede_comprar < 0:
    print("No puedes comprar el producto con tu dinero")
else:
    print("Felicidades ! Puedes comprar el producto con tu dinero")