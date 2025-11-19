
CREATE DATABASE myflaskapp;
use myflaskapp;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    username varchar(255),
    password varchar(255)
);


INSERT INTO users VALUES(null, "juan", "juan@gmail.com", "juan", "123"),
    (null, "maria", "maria@gmail.com", "maria", "456");


CREATE TABLE productos (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    descripcion varchar(255) NOT NULL,
    precio decimal(10,2) NOT NULL,
    cantidad int NOT NULL
);

INSERT INTO productos VALUES(null, "Pepsi 400ml", "Bebida gasificada", 2500.00, 15),
    (null, "Margaritas limon", "Papas con sabeor limon", 3000.00, 10),
    (null, "Chao cereza", "Mentas con sabor cereza", 1000.00, 25)
