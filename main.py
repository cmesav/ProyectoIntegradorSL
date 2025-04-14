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

# Ejecución de algunos métodos
print("Insertando un nuevo rol:")
repositorio_roles.InsertarRol("Administrador")
repositorio_roles.ListarRoles()

print("\nInsertando un nuevo usuario:")
repositorio_usuarios.InsertarUsuario("Juan Pérez", "juan@example.com", "password123", 1)
repositorio_usuarios.ListarUsuarios()

print("\nInsertando una categoría:")
repositorio_categorias.InsertarCategoria("Electrónica")
repositorio_categorias.ListarCategorias()

print("\nInsertando un producto:")
repositorio_productos.InsertarProducto("Smartphone", 1, 799.99)
repositorio_productos.ListarProductosConCategoria()

print("\nInsertando un método de pago:")
repositorio_metodos_pago.InsertarMetodoPago("Tarjeta de crédito")
repositorio_metodos_pago.ListarMetodosPago()

print("\nInsertando un estado de transacción:")
repositorio_estado_transaccion.InsertarEstadoTransaccion("Aprobado")
repositorio_estado_transaccion.ListarEstadoTransaccion()

print("\nInsertando una transacción:")
repositorio_transacciones.InsertarTransaccion(1, "2025-04-14", 1, 1)
repositorio_transacciones.ListarTransacciones()

print("\nInsertando un detalle de transacción:")
repositorio_detalles_transaccion.InsertarDetalleTransaccion(1, 1, 2)
repositorio_detalles_transaccion.ListarDetallesTransaccion()

print("\nActualizando inventario:")
repositorio_inventario.ActualizarInventario(1, 50)
repositorio_inventario.ListarInventario()

print("\nInsertando un proveedor:")
repositorio_proveedores.InsertarProveedor("Proveedor XYZ", "contacto@xyz.com")
repositorio_proveedores.ListarProveedores()

print("\nInsertando una dirección de usuario:")
repositorio_direcciones_usuarios.InsertarDireccionUsuario(1, "Av. Principal 123")
repositorio_direcciones_usuarios.ListarDireccionesUsuarios()

print("\nInsertando un historial de precios:")
repositorio_historial_precios.InsertarHistorialPrecio(1, "2025-04-14", 799.99, 749.99)
repositorio_historial_precios.ListarHistorialPrecios()

print("\nInsertando una devolución:")
repositorio_devoluciones.InsertarDevolucion(1, "Producto defectuoso", "2025-04-14")
repositorio_devoluciones.ListarDevoluciones()

print("\nInsertando una notificación:")
repositorio_notificaciones.InsertarNotificacion(1, "Su pedido ha sido enviado", "2025-04-14")
repositorio_notificaciones.ListarNotificaciones()
