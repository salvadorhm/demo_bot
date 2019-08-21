CREATE DATABASE samm_db;

USE samm_db;

CREATE TABLE productos(
  id_producto int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sku varchar(10) NOT NULL,
  producto varchar(100) NOT NULL,
  precio float NOT NULL,
  existencias int(11) NOT NULL,
  update_data timestamp
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO productos(sku, producto, precio, existencias)
VALUES
('mar001','Martillo Rojo',100.00, 12),
('mar002','Martillo Amarillo',110.00, 13),
('tal001','Taladro',1000.00, 5);

CREATE USER 'samm'@'localhost' IDENTIFIED BY 'samm.2019';
GRANT ALL PRIVILEGES ON samm_db.* TO 'samm'@'localhost';
FLUSH PRIVILEGES;
