--part 1
SELECT * FROM film WHERE rental_duration > 4

--part 2
(SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5