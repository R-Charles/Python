SELECT * FROM arbortrary_db.users;

-- query = "SELECT * " 
--         query += "FROM planted_trees "
--         query += "JOIN users ON planted_trees.user_id = users.id;"
        
SELECT *
FROM users
JOIN planted_trees ON users.id = planted_trees.id,
WHERE id = 1;

SELECT * 
FROM users
WHERE id = 2;

SELECT * 
FROM planted_trees
WHERE user_id = 2;
 