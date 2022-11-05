SELECT countries, cities
FROM countries
FULL JOIN cities
ON countries.id =cities.country_id;

SELECT countries.name AS country, COUNT(cities.id) AS num_cities FROM countries
JOIN cities
ON countries.code = cities.country_code -- COUNTRIES.CODE IS WHAT IS IN COMMON-- 
GROUP BY countries.code -- STATMENT THAT GROUPS ROWS TOGETHER
ORDER BY COUNT(cities.id) DESC;

SELECT cities.name, population, country_id
FROM cities
WHERE country_id = 136 AND population > 500000
ORDER BY population DESC;

SELECT countries.name, language, percentage
FROM countries
JOIN languages
ON countries.code = languages.country_code
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'constitutional monarchy' AND capital > 200 AND life_expectancy> 75;

SELECT countries.name, cities.name, district, cities.population
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
WHERE countries.name = 'Argentina' AND district = 'Buenos Aires' AND cities.population > 500000;

SELECT region, COUNT(countries.id)
FROM countries
GROUP BY region
ORDER BY(countries.id) DESC;


