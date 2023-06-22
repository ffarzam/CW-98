--part 1
SELECT title, release_year, name
From film INNER JOIN film_category on film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id;




