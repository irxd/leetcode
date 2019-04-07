--https://leetcode.com/problems/not-boring-movies/

SELECT *
FROM cinema
WHERE NOT description = 'boring'
    AND NOT id % 2 = 0
ORDER BY rating DESC
