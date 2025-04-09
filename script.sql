CREATE DATABASE SistemaTransacciones;

USE SistemaTransacciones;

CREATE TABLE Usuarios (
    IDUsuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100),
    Correo VARCHAR(100),
    Contraseña VARCHAR(255),
    IDRol INT,
    FOREIGN KEY (IDRol) REFERENCES Roles(IDRol)
);

CREATE TABLE Roles (
    IDRol INT AUTO_INCREMENT PRIMARY KEY,
    NombreRol VARCHAR(50)
);

CREATE TABLE Productos (
    IDProducto INT AUTO_INCREMENT PRIMARY KEY,
    NombreProducto VARCHAR(100),
    IDCategoria INT,
    Precio DECIMAL(10,2),
    FOREIGN KEY (IDCategoria) REFERENCES Categorías(IDCategoria)
);

CREATE TABLE Categorías (
    IDCategoria INT AUTO_INCREMENT PRIMARY KEY,
    NombreCategoria VARCHAR(100)
);

CREATE TABLE Transacciones (
    IDTransaccion INT AUTO_INCREMENT PRIMARY KEY,
    IDUsuario INT,
    Fecha DATE,
    IDMetodoPago INT,
    IDEstadoTransaccion INT,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario),
    FOREIGN KEY (IDMetodoPago) REFERENCES MétodosPago(IDMetodoPago),
    FOREIGN KEY (IDEstadoTransaccion) REFERENCES EstadoTransacción(IDEstadoTransaccion)
);

CREATE TABLE MétodosPago (
    IDMetodoPago INT AUTO_INCREMENT PRIMARY KEY,
    NombreMetodo VARCHAR(100)
);

CREATE TABLE DetallesTransacción (
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
    Dirección VARCHAR(255),
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)
);

CREATE TABLE EstadoTransacción (
    IDEstadoTransaccion INT AUTO_INCREMENT PRIMARY KEY,
    NombreEstado VARCHAR(100)
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
    IDDevolución INT AUTO_INCREMENT PRIMARY KEY,
    IDTransaccion INT,
    Motivo VARCHAR(255),
    Fecha DATE,
    FOREIGN KEY (IDTransaccion) REFERENCES Transacciones(IDTransaccion)
);

CREATE TABLE Notificaciones (
    IDNotificación INT AUTO_INCREMENT PRIMARY KEY,
    IDUsuario INT,
    Mensaje VARCHAR(255),
    Fecha DATE,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)
);
