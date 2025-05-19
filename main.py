from Repositorios import (
    RepositorioRoles, RepositorioUsuarios, RepositorioCategorias, 
    RepositorioProductos, RepositorioEstadoTransaccion, RepositorioMetodosPago, 
    RepositorioTransacciones, RepositorioDetallesTransaccion, RepositorioInventario,
    RepositorioProveedores, RepositorioDireccionesUsuarios, RepositorioHistorialPrecios,
    RepositorioDevoluciones, RepositorioNotificaciones
)

# Instancias de cada repositorio
repositorio_roles = RepositorioRoles.RepositorioRoles()
repositorio_usuarios = RepositorioUsuarios.RepositorioUsuarios()
repositorio_categorias = RepositorioCategorias.RepositorioCategorias()
repositorio_productos = RepositorioProductos.RepositorioProductos()
repositorio_estado_transaccion = RepositorioEstadoTransaccion.RepositorioEstadoTransaccion()
repositorio_metodos_pago = RepositorioMetodosPago.RepositorioMetodosPago()
repositorio_transacciones = RepositorioTransacciones.RepositorioTransacciones()
repositorio_detalles_transaccion = RepositorioDetallesTransaccion.RepositorioDetallesTransaccion()
repositorio_inventario = RepositorioInventario.RepositorioInventario()
repositorio_proveedores = RepositorioProveedores.RepositorioProveedores()
repositorio_direcciones_usuarios = RepositorioDireccionesUsuarios.RepositorioDireccionesUsuarios()
repositorio_historial_precios = RepositorioHistorialPrecios.RepositorioHistorialPrecios()
repositorio_devoluciones = RepositorioDevoluciones.RepositorioDevoluciones()
repositorio_notificaciones = RepositorioNotificaciones.RepositorioNotificaciones()

# Ejecución de algunos métodos con cifrado AES
print("Insertando un nuevo rol:")
repositorio_roles.InsertarRol("Administrador")
print(" Listado de roles:")
print(repositorio_roles.ListarRoles())

print("\n Insertando un nuevo usuario:")
repositorio_usuarios.InsertarUsuario("Juan Pérez", "juan@example.com", "password123", 1)
print("Listado de usuarios:")
print(repositorio_usuarios.ListarUsuarios())

print("\n Insertando una categoría:")
repositorio_categorias.InsertarCategoria("Electrónica")
print(" Listado de categorías:")
print(repositorio_categorias.ListarCategorias())

print("\n Insertando un producto:")
repositorio_productos.InsertarProducto("Smartphone", 1, 799.99)
print(" Listado de productos:")
print(repositorio_productos.ListarProductosConCategoria())

print("\n Insertando un método de pago:")
repositorio_metodos_pago.InsertarMetodoPago("Tarjeta de crédito")
print(" Listado de métodos de pago:")
print(repositorio_metodos_pago.ListarMetodosPago())

print("\n Insertando un estado de transacción:")
repositorio_estado_transaccion.InsertarEstadoTransaccion("Aprobado")
print(" Listado de estados de transacción:")
print(repositorio_estado_transaccion.ListarEstadoTransaccion())

print("\n Insertando una transacción:")
repositorio_transacciones.InsertarTransaccion(1, "2025-04-14", 1, 1)
print(" Listado de transacciones:")
print(repositorio_transacciones.ListarTransacciones())

print("\n Insertando un detalle de transacción:")
repositorio_detalles_transaccion.InsertarDetalleTransaccion(1, 1, 2)
print(" Listado de detalles de transacción:")
print(repositorio_detalles_transaccion.ListarDetallesTransaccion())

print("\n Actualizando inventario:")
repositorio_inventario.ActualizarInventario(1, 50)
print(" Listado de inventario:")
print(repositorio_inventario.ListarInventario())

print("\n Insertando un proveedor:")
repositorio_proveedores.InsertarProveedor("Proveedor XYZ", "contacto@xyz.com")
print(" Listado de proveedores:")
print(repositorio_proveedores.ListarProveedores())

print("\n Insertando una dirección de usuario:")
repositorio_direcciones_usuarios.InsertarDireccionUsuario(1, "Av. Principal 123")
print(" Listado de direcciones:")
print(repositorio_direcciones_usuarios.ListarDireccionesUsuarios())

print("\n Insertando un historial de precios:")
repositorio_historial_precios.InsertarHistorialPrecio(1, "2025-04-14", 799.99, 749.99)
print(" Listado de historial de precios:")
print(repositorio_historial_precios.ListarHistorialPrecios())

print("\n Insertando una devolución:")
repositorio_devoluciones.InsertarDevolucion(1, "Producto defectuoso", "2025-04-14")
print(" Listado de devoluciones:")
print(repositorio_devoluciones.ListarDevoluciones())

print("\n Insertando una notificación:")
repositorio_notificaciones.InsertarNotificacion(1, "Su pedido ha sido enviado", "2025-04-14")
print(" Listado de notificaciones:")
print(repositorio_notificaciones.ListarNotificaciones())