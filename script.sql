CREATE DATABASE SistemaTransacciones;

USE SistemaTransacciones;

CREATE TABLE Roles (
    IDRol INT AUTO_INCREMENT PRIMARY KEY,
    NombreRol VARCHAR(50)
);

CREATE TABLE Usuarios (
    IDUsuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100),
    Correo VARCHAR(100),
    Contrasena VARCHAR(255),
    IDRol INT,
    FOREIGN KEY (IDRol) REFERENCES Roles(IDRol)
);

CREATE TABLE Categorias (
    IDCategoria INT AUTO_INCREMENT PRIMARY KEY,
    NombreCategoria VARCHAR(100)
);

CREATE TABLE Productos (
    IDProducto INT AUTO_INCREMENT PRIMARY KEY,
    NombreProducto VARCHAR(100),
    IDCategoria INT,
    Precio DECIMAL(10,2),
    FOREIGN KEY (IDCategoria) REFERENCES Categorias(IDCategoria)
);

CREATE TABLE EstadoTransaccion (
    IDEstadoTransaccion INT AUTO_INCREMENT PRIMARY KEY,
    NombreEstado VARCHAR(100)
);

CREATE TABLE MetodosPago (
    IDMetodoPago INT AUTO_INCREMENT PRIMARY KEY,
    NombreMetodo VARCHAR(100)
);

CREATE TABLE Transacciones (
    IDTransaccion INT AUTO_INCREMENT PRIMARY KEY,
    IDUsuario INT,
    Fecha DATE,
    IDMetodoPago INT,
    IDEstadoTransaccion INT,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario),
    FOREIGN KEY (IDMetodoPago) REFERENCES MetodosPago(IDMetodoPago),
    FOREIGN KEY (IDEstadoTransaccion) REFERENCES EstadoTransaccion(IDEstadoTransaccion)
);

CREATE TABLE DetallesTransaccion (
    IDDetalle INT AUTO_INCREMENT PRIMARY KEY,
    IDTransaccion INT,
    IDProducto INT,
    Cantidad INT,
    FOREIGN KEY (IDTransaccion) REFERENCES Transacciones(IDTransaccion),
    FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto)
);

CREATE TABLE Inventario (
    IDInventario INT AUTO_INCREMENT PRIMARY KEY,
    IDProducto INT,
    CantidadDisponible INT,
    FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto)
);

CREATE TABLE Proveedores (
    IDProveedor INT AUTO_INCREMENT PRIMARY KEY,
    NombreProveedor VARCHAR(100),
    Contacto VARCHAR(100)
);

CREATE TABLE DireccionesUsuarios (
    IDDireccion INT AUTO_INCREMENT PRIMARY KEY,
    IDUsuario INT,
    Direccion VARCHAR(255),
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)
);

CREATE TABLE HistorialPrecios (
    IDHistorial INT AUTO_INCREMENT PRIMARY KEY,
    IDProducto INT,
    Fecha DATE,
    PrecioAntiguo DECIMAL(10,2),
    PrecioNuevo DECIMAL(10,2),
    FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto)
);

CREATE TABLE Devoluciones (
    IDDevolucion INT AUTO_INCREMENT PRIMARY KEY,
    IDTransaccion INT,
    Motivo VARCHAR(255),
    Fecha DATE,
    FOREIGN KEY (IDTransaccion) REFERENCES Transacciones(IDTransaccion)
);

CREATE TABLE Notificaciones (
    IDNotificacion INT AUTO_INCREMENT PRIMARY KEY,
    IDUsuario INT,
    Mensaje VARCHAR(255),
    Fecha DATE,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)
);
