--part 1
SELECT title, release_year, name
From film INNER JOIN film_category on film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id;

--part 2
SELECT title, release_year, name
From film INNER JOIN film_category on film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
WHERE name IN ('Action', 'Comedy' , 'Family');

--part 3
SELECT  name, count(*)
From film INNER JOIN film_category on film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
GROUP BY name;

--part 4
SELECT  name, count(*) as count
From film INNER JOIN film_category on film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
GROUP BY name
HAVING count(*) > 60 AND count(*) < 68;

--part 5

SELECT language.name language, film.title, category.name category
From film INNER JOIN language ON language.language_id = film.language_id
INNER JOIN film_category ON film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id;

--part 6
SELECT customer.first_name,customer.last_name, film.title,AGE(return_date,rental_date) AS rental_duration
FROM customer
INNER JOIN rental ON rental.customer_id = customer.customer_id
INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
INNER JOIN film ON film.film_id = inventory.inventory_id;


--part 7

select title,length,(select avg(length) from film) as avg_lengh from film
where film.length > (select avg(length) from film);

--SELECT f.film_id, f.title,f.length, f.c
--FROM (Select * ,(SELECT avg(length) FROM film)  as c
--FROM film) as f
--WHERE f.length> f.c


--part 8
SELECT *
FROM (SELECT film.film_id,film.title, rental.return_date
FROM film
INNER JOIN inventory ON inventory.film_id=film.film_id
INNER JOIN rental ON rental.inventory_id=inventory.inventory_id) as f
WHERE return_date > '2005-05-29' and return_date < '2005-05-30';