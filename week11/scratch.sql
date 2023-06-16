--part 1
SELECT * FROM film WHERE rental_duration > 4

--part 2
(SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5

--part 3

SELECT * FROM film WHERE rental_duration > 4 ORDER BY title
SELECT * FROM film WHERE rental_duration > 4 ORDER BY title DESC

SELECT * FROM film WHERE rental_duration > 4 ORDER BY rental_duration
SELECT * FROM film WHERE rental_duration > 4 ORDER BY rental_duration DESC

SELECT * FROM film WHERE rental_duration > 4 ORDER BY last_update
SELECT * FROM film WHERE rental_duration > 4 ORDER BY last_update DESC


SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5 ORDER BY title
SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5 ORDER BY title DESC

SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5 ORDER BY rental_duration
SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5 ORDER BY rental_duration DESC

SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5 ORDER BY last_update
SELECT * FROM film WHERE rental_duration > 2 and rental_duration <5 ORDER BY last_update DESC