-- Number by score
-- in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
