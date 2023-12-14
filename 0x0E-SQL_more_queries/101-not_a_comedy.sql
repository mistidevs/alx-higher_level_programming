-- Returning the shows
-- that don't have comedy as a genre
SELECT DISTINCT s.title
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.title NOT IN (
SELECT s.title
FROM tv_shows AS s
INNER JOIN tv_show_genres AS sg ON s.id = sg.show_id
INNER JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE g.name = 'Comedy')
ORDER BY s.title ASC;
