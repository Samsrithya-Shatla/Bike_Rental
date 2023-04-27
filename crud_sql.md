SELECT * FROM Customers;

UPDATE Rentals SET rental_end_date = '07-APR-2023' WHERE rental_id = 1;

DELETE FROM Invoices WHERE invoice_amount<100;

#calculate_total_earnings
SELECT bikes.bike_id, bikes.bike_type, SUM(invoices.invoice_amount) as TotalEarnings
            FROM bikes
            JOIN rentals ON rentals.bike_id = bikes.bike_id
            JOIN invoices ON invoices.rental_id = rentals.rental_id
            GROUP BY bikes.bike_id
            
#calculate_total_rentals
SELECT customers.customer_id, customers.first_name, customers.last_name, COUNT(*) as TotalRentals
            FROM rentals
            JOIN customers ON rentals.customer_id = customers.customer_id
            GROUP BY customers.customer_id
            
#find_most_rented_bikes
SELECT bikes.bike_id, bikes.bike_type, COUNT(rentals.rental_id) as NumberOfRentals
            FROM bikes
            JOIN rentals ON rentals.bike_id = bikes.bike_id
            GROUP BY bikes.bike_id
            ORDER BY NumberOfRentals DESC;
