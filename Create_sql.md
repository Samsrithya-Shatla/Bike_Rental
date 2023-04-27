USE BikeRentalDB;

CREATE TABLE Customers (
customer_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
phone VARCHAR(20)
);

CREATE TABLE Bikes (
bike_id INT PRIMARY KEY,
bike_type VARCHAR(50),
bike_color VARCHAR(20),
bike_price DECIMAL(8, 2)
);

CREATE TABLE Rentals (
rental_id INT PRIMARY KEY,
customer_id INT,
bike_id INT,
rental_start_date DATE,
rental_end_date DATE,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
FOREIGN KEY (bike_id) REFERENCES Bikes(bike_id) ON DELETE CASCADE
);

CREATE TABLE Invoices (
invoice_id INT PRIMARY KEY,
rental_id INT,
invoice_amount DECIMAL(8, 2),
FOREIGN KEY (rental_id) REFERENCES Rentals(rental_id) ON DELETE CASCADE
);
