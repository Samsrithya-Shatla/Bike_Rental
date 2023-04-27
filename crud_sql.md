SELECT * FROM Customers;

UPDATE Rentals SET rental_end_date = '07-APR-2023' WHERE rental_id = 1;

DELETE FROM Invoices WHERE invoice_amount<100;