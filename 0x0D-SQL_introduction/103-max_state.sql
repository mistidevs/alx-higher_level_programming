-- Displaying the max tempearature of each state
-- ordering by the states alphabetically
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
