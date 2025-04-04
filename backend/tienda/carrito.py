class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        producto_id = str(producto.id)

        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                "nombre": producto.nombre,
                "precio": float(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url if producto.imagen else "",
            }
        else:
            if isinstance(self.carrito[producto_id], dict):  # ✅ Validar que sea un diccionario
                self.carrito[producto_id]["cantidad"] += 1
            else:
                self.carrito[producto_id] = {  # ✅ Corregir en caso de error
                    "nombre": producto.nombre,
                    "precio": float(producto.precio),
                    "cantidad": 1,
                    "imagen": producto.imagen.url if producto.imagen else "",
                }

        self.guardar()


    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    def disminuir(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            if self.carrito[producto_id]["cantidad"] > 1:
                self.carrito[producto_id]["cantidad"] -= 1
            else:
                self.eliminar(producto)

        self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
