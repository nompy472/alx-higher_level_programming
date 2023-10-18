0x0D. SQL - Introduction

Tasks
Mandatory
0. List databases
a script that lists all databases of your MySQL server.
1. Create a database
a script that creates the database hbtn_0c_0 in your MySQL server.
-If the database hbtn_0c_0 already exists, your script should not fail
2. Delete a database
a script that deletes the database hbtn_0c_0 in your MySQL server.
-If the database hbtn_0c_0 doesn’t exist, your script should not fail
3. List tables
a script that lists all the tables of a database in your MySQL server.
-The database name will be passed as argument of mysql command
4. First table
a script that creates a table called first_table in the current database in your MySQL server.
-first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first_table already exists, your script should not fail
5. Full description
a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
-The database name will be passed as an argument of the mysql command
6. List all in table
a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
7. First add
a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
-New row:
id = 89
name = Best School
The database name will be passed as an argument of the mysql command
8. Count 89
a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
9. Full creation
a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
-second_table description:
id INT
name VARCHAR(256)
score INT
10. List by best
a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
11. Select the best
a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
12. Cheating is bad
a script that updates the score of Bob to 10 in the table second_table.
13. Score too low
a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
14. Average
a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server
15. Number by score
a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
16. Say my name
a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Advanced

17. Go to UTF8
a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
18. Temperatures #0
a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
19. Temperatures #1
a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
20. Temperatures #2
a script that displays the max temperature of each state (ordered by State name)
