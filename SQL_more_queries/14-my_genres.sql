-- list the genre of tv_shows --
SELECT tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id= tv_genres.id
WHERE title = 'Dexter'
ORDER BY name ASC;
