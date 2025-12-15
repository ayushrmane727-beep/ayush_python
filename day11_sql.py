SELECT * FROM movies;# for selecting all columns or rows

SELECT title FROM movies;#for selecting title column

SELECT director FROM movies;#for selecting director column 

SELECT title,director FROM movies; #for selecting tile and director column

SELECT title,year FROM movies; #for selecting title and year column

SELECT id, title From movies 
WHERE id =6;#for selecting 6th row id

SELECT title, year FROM movies
WHERE year BETWEEN 2000 AND 2010;#for finding movie between years 2000 and 2010

SELECT title, year FROM movies
WHERE year < 2000 OR year > 2010;#for finding  from first 5 pixer movie title and year  

SELECT title, year FROM movies
WHERE year <= 2003;