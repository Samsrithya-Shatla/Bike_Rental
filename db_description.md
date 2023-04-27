# **Introduction** 
This assignment is focused on creating a desktop application(using Python) that uses local database(MySQL server). The objective of the venture is to make a database for a bike rental organization utilizing well-known 
database programs such as MySQL server. The database is planned to meet particular prerequisites, counting having at least four tables, each within the third typical frame (3NF), 
with at least four areas per table, counting essential keys. Utilitarian conditions (FDs) are recognized for each table, and outside key imperatives and arrangements are defined to guarantee information astuteness. 
SQL articulations are given to form the tables, populate them with test information, and perform CRUD operations on the information.

In expansion to planning the database, the task requires creating a graphical client interface (GUI) application that serves as a straightforward front conclusion to perform CRUD operations on the database. 
Predefined SQL statements, such as SQL performing connect on different tables and sub queries, are moreover included within the application. 
This venture gives a hands-on involvement with planning a database and creating an application that interact with the database. 
It moreover highlights the significance of information modeling and utilize of local databases in overseeing complex information structures.

# **Database description**
This database is designed to be used to store and oversee information related to a bike rental organization. By employing a local database administration framework, MySQL Server, the organization can store client data, 
Bike points of interest, rental exchanges, and receipt data in an organized and organized way. The database permits the organization to effectively oversee their bike rental operations, 
counting following Bike accessibility, overseeing client data, and producing rental solicitations. Also, the database can give bits of knowledge into the organization's operations by permitting it to analyze rental designs,
track income, and make data-driven choices to optimize commerce forms. The database is planned for a bike rental organization and is actualized utilizing MySQL.


# ** Structure**
the database contains 4 tables: Customers, Bikes, Rentals, and Invoices.
Customers table:
Attributes: customer_id (PK), first_name, last_name, email, phone
Primary Key (PK): customer_id
Foreign Keys: None
Foreign Key Constraints: None
FDs: customer_id -> first_name, last_name, email, phone
3NF: Yes
Sample data:
(1, 'John', 'Doe', 'john.doe@example.com', '555-123-4567')
(2, 'Jane', 'Smith', 'jane.smith@example.com', '555-987-6543')

Bikes table:
Attributes: bike_id (PK), bike_type, bike_color, bike_price
Primary Key (PK): bike_id
Foreign Keys: None
Foreign Key Constraints: None
FDs: bike_id -> bike_type, bike_color, bike_price
3NF: Yes
Sample data:
(1, 'Mountain', 'Red', 25.00)
(2, 'Road', 'Blue', 30.00)

Rentals table:
Attributes: rental_id (PK), customer_id (FK), bike_id (FK), rental_start_date, rental_end_date
Primary Key (PK): rental_id
Foreign Keys: customer_id, bike_id
Foreign Key Constraints:
ON DELETE CASCADE for customer_id, bike_id (if a customer or bike record is deleted, related rentals will be deleted automatically)
FDs: rental_id -> customer_id, bike_id, rental_start_date, rental_end_date
3NF: Yes
Sample data:
(1, 1, 1, '2023-04-01', '2023-04-03')
(2, 2, 2, '2023-04-02', '2023-04-04')

Invoices table:
Attributes: invoice_id (PK), rental_id (FK), invoice_amount
Primary Key (PK): invoice_id
Foreign Keys: rental_id
Foreign Key Constraints:
ON DELETE CASCADE for rental_id (if a rental record is deleted, the related invoice will be deleted automatically)
FDs: invoice_id -> rental_id, invoice_amount
3NF: Yes
Sample data:
(1, 1, 50.00)
(2, 2, 60.00)

# **3NF**
The tables are planned to be within the third ordinary frame (3NF), meaning that they are normalized to decrease information excess and progress information judgment. Each table has at slightest four areas, counting essential keys, and each table's useful conditions are recorded to guarantee that the information is organized accurately. The outside key constraints are too characterized, together with approaches on outside key constraints to guarantee that information keenness is kept up.

