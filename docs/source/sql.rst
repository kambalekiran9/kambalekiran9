.. _sql:

####################################### 
Getting started with SQL  :
#######################################

.. _ddl:

================================
Data definition language (DDL):
================================


* **1) Create Table statement:**

* A relational database consists of multiple related tables. A table consists of rows and columns.
  Tables allow you to store structured data like customers, products, employees, etc.
* To describe a table you may use command like \d table_name

* To create a new table, you use the CREATE TABLE statement. The following illustrates the basic
  syntax of the CREATE TABLE statement:


   .. code-block:: bash


      create table employee
      (id int primary key not null,
      name text not null,
      age int not null,
      address char(50),
      salary real );


   


   .. image:: ../images/ddl.png


**Alter Table Statement**


* ALTER TABLE changes the definition of an existing table.
* The following illustrates the basic syntax of the ALTER TABLE statement:
  ALTER TABLE table_name action;
  
* **PostgreSQL provides you with many actions:**

   
   • Add a column
   • Drop a column
   • Change the data type of a column
   • Rename a column
   • Add a constraint to a column.
   • Rename a table


**Example:-**

* In this example we have added a column name age in to employee table.  

   $ alter table employee add column age int;


   .. code-block:: bash


    postgres=# alter table employee add column pincode  int;
    ALTER TABLE
    postgres=# select * from employee ;
    id | name | age | address | salary | pincode 
    ----+------+-----+---------+--------+---------
    (0 rows)



.. _dml:

============================================
Data Manupulation Language- Insert (DML):
============================================


* The PostgreSQL INSERT statement allows you to insert a new row into a table.
* The following illustrates the most basic syntax of the INSERT statement:
   INSERT INTO table_name(column1, column2, …)
   VALUES (value1, value2, …);


**In this syntax:**


1) specify the name of the table (table_name) that you want to insert data after the INSERT INTO keywords and
   a list of comma-separated columns (colum1, column2, ....).
2) supply a list of comma-separated values in a parentheses (value1, value2, ...) after the VALUES keyword.
   The columns and values in the column and value lists must be in the same order.

**Example:-**


postgres=#insert into employee (id,name,age,address,salary)values (10,'smith',30,'Babglore',50000);


  .. code-block:: bash


    postgres=# insert into employee (id,name,age,address,salary)values (10,'smith',30,'Babglore',50000);
    INSERT 0 1



* **DML-Update:**


* UPDATE changes the values of the specified columns in all rows that satisfy the condition. Only the
  columns to be modified need be mentioned in the SET clause; columns not explicitly modified retain
  their previous values.
* The following illustrates the syntax of the UPDATE statement:
 
  UPDATE table_name
  SET column1 = value1,
  column2 = value2,
  ...
  WHERE condition;


* **DML -Update:**

**Example:-**

* In this example we have updated salary to 10000 where id no. is 2

    
  testdb=# update employee1 set salary = 10000 where id=2;


* **DML -Delete:**


* The PostgreSQL DELETE statement allows you to delete one or more rows from a table.
* The following shows basic syntax of the DELETE statement:


   DELETE FROM table_name
   WHERE condition;
   

**In this syntax:**

* First, specify the name of the table from which you want to delete data after the DELETE FROM
  keywords.
* Second, use a condition in the WHERE clause to specify which rows from the table to delete.
* Note that the DELETE statement only removes data from a table. It doesn’t modify the structure of the
  table.


**Example:-**


* In this example we have deleted a record where id was 6. 
  
   test=#delete from employee1 where id=6;


.. _dcl:

=====================================
Data control language (DCL):
=====================================



.. _tcl:

=====================================
Transaction control language (TCL):
=====================================


* **TCL begin:**

* **In TCL transaction start with ‘begin’ then we perform tasks.**

   testdb=# begin ;
   BEGIN
   testdb=# SELECT * FROM emp;


* Here we will insert a new recod in to the table


   testdb=# insert into emp (name,gender,age) values ('Rahul','M',27);
   testdb=# SELECT * FROM emp;


* **TCL Savepoint:**

* SAVEPOINT is a boundary defined within a transaction that allows for a partial
  rollback.
* It gives the user the ability to roll the transaction back to a certain point without rolling
  back the entire transaction.


 * testdb=# savepoint my_savepoint;


* **TCL Rollback and commit:**


**ROLLBACK:-**
  
* As the name suggests, ROLLBACK undoes the changes that were issued in the transaction block
    before it.

**Example:-**
  
 * testdb=# insert into emp (name,gender,age) values ('Rohit','M',26);
    INSERT 0 1 
 * testdb=# SELECT * FROM emp;

  
* Now use rollback to mu_savepoint it will delete the unsaved row from table.
  
 * testdb=# rollback to my_savepoint;
 * ROLLBACK


**Commit:-**
   
* the COMMIT keyword saves changes to the database.
   
 * testdb=# commit;
     COMMIT
 * testdb=# SELECT * FROM emp;


.. _sequence:

===========
sequence:
===========

* CREATE SEQUENCE creates a new sequence number generator. This involves creating
  and initializing a new special single-row table with the name. The generator will be
  owned by the user issuing the command.

* Sequence/ Serial Function..
* nextval() - Advance sequence and return new value
* currval() - Most recently used value for specific sequence
* setval() - Set next returned value for a sequence

 * Ex.

  testdb=#INSERT INTO student VALUES (nextval('demo_seqn'), 'saurabh');
  INSERTO I

**Sequences are used to generate unique values for insertion of new records.**



**Insert some values into the table:-**


* testdb=# create table emp1 (id int,name varchar(20),age int,city varchar(20));
    CREATE TABLE
* testdb=# insert into emp1 values (nextval('test_id'),'Kishor',24,'pune');
    INSERT 0 1
* testdb=# insert into emp1 values (nextval('test_id'),'Rohit',25,'pune');
    INSERT 0 1
* testdb=# insert into emp1 values (nextval('test_id'),'Nilesh',25,'pune');
    INSERT 0 1



**Data Retrieval - Select**

* One of the most common tasks, when you work with the database, is to query data from tables
    by using the SELECT statement.
* The SELECT statement is one of the most complex statements in PostgreSQL. It has many
* clauses that you can use to form a flexible query.

* **The following illustrates the syntax of the SELECT statement:**


    .. code-block:: bash
   
     
       testdb=#SELECT
       select_list
       FROM
       table_name;


.. _groupby:

======================
GROUP BY Statement:
======================

* The GROUP BY statement groups rows that have the same values into summary rows, like "find the 
  number of customers in each country".

* The GROUP BY statement is often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(),
   AVG()) to group the result-set by one or more columns.


* **GROUP BY Syntax:-**


   SELECT column_name(s)
   FROM table_name
   WHERE condition
   GROUP BY column_name(s)
   ORDER BY column_name(s);

**Using PostgreSQL GROUP BY with SUM() function example:-**

* The GROUP BY clause is useful when it is used in conjunction with an aggregate function.
* For example, to select the total amount that each customer has been paid, you use the GROUP BY clause
  to divide the rows in the payment table into groups grouped by customer id. For each group, you calculate
  the total amounts using the SUM() function.
  The following query uses the GROUP BY clau


**The following query uses the GROUP BY clause to get total amount that each customer has been paid:**

      
       dvdrental=#SELECT customer_id,SUM (amount)
                  FROM payment
                  GROUP BY customer_id;


* The GROUP BY clause sorts the result set by customer id and adds up the amount that belongs to
  the same customer. Whenever the customer_id changes, it adds the row to the returned result set.



.. _having:

===================
HAVING Statement
===================



* **PostgreSQL HAVING clause**

* The HAVING clause specifies a search condition for a group or an aggregate. The HAVING clause is often
  used with the GROUP BY clause to filter groups or aggregates based on a specified condition.

* The following statement illustrates the basic syntax of the HAVINGclause:

   
     dvdrental=#SELECT column1, aggregate_function (column2)
               FROM table_name
               GROUP BY
               column1
               HAVING condition;


* In this syntax, the group by clause returns rows grouped by the column1.
* The HAVING clause specifies a condition to filter the groups.
* It’s possible to add other clauses of the SELECT statement such as JOIN, LIMIT, FETCH etc.


**Using PostgreSQL HAVING clause with SUM function example**

* The following statement adds the HAVING clause to select the only customers who have been
  spending more than 200:


     dvdrental=#SELECT customer_id,SUM (amount)
               FROM payment
               GROUP BY customer_id
               HAVING SUM (amount) > 200;



.. _orderby:

============
Order By
============


* When you query data from a table, the SELECT statement returns rows in an unspecified order.
  To sort the rows of the result set, you use the ORDER BY clause in the SELECT statement.
* The ORDER BY clause allows you to sort rows returned by a SELECT clause in ascending or
  descending order based on a sort expression.

* The following illustrates the syntax of the ORDER BY clause:
 

     SELECT
     select_list
     FROM
     table_name
     ORDER BY
     sort_expression1 [ASC | DESC],
     ...
     sort_expressionN [ASC | DESC];




* **The following illustrates the example of the ORDER BY clause:**
  
   testdb=#SELECT name FROM emp ORDER BY name DESC;


.. _limit:

==================
LIMIT and OFFSET
==================
* LIMIT and OFFSET are used when you want to retrieve only a few records from your result
  of query.
* LIMIT will retrieve only the number of records specified after the LIMIT keyword, unless the 
  query itself returns fewer records than the number specified by LIMIT.
* OFFSET is used to skip the number of records from the results.


* **The following illustrates the syntax of the LIMIT clause:**

    SELECT
    select_list
    FROM 
    table_name
    ORDER BY
    sort_expression1 [ASC | DESC],
    LIMIT ....;

**LIMIT**

**1) Using PostgreSQL LIMIT to constrain the number of returned rows example:-**

 * This example uses the LIMIT clause to get the first five films sorted by film_id:

   dvdrental=#SELECT film_id, title, release_year
   FROM film
   ORDER BY film_id LIMIT 5;


**2) Using PostgreSQL LIMIT with OFFSET example:-**


* To retrieve 4 films starting from the fourth one ordered by film_id, you use both LIMIT
  and OFFSET clauses as follows:


   dvdrental=#SELECT film_id, title, release_year
   FROM film
   ORDER BY film_id
   LIMIT 4 OFFSET 3;


**3) Using PostgreSQL LIMIT OFFSSET to get top / bottom N rows :-**


* Typically, you often use the LIMIT clause to select rows with the highest or lowest values from a table.
* For example, to get the top 10 most expensive films in terms of rental, you sort films by the rental rate
  in descending order and use the LIMIT clause to get the first 10 films.
* The following query illustrates the idea:


   dvdrental=#SELECT film_id, title, rental_rate
   FROM film
   ORDER BY rental_rate DESC LIMIT 10;


**Aliases:**


* In simple terms, the ALIAS means temporarily giving another name to a table or a column.
* In order to give the temporary name for tables or columns, we generally use the
  PostgreSQL Aliases.
* The existence of aliasing is limited to the PostgreSQL statement’s execution means the
  PostgreSQL aliases are used to rename a column or a table in a specific PostgreSQL query.
* Hence the actual table name or column name does not change in the database.

**Aliases for column:-**

  SELECT column [AS] alias_name
  FROM table;


 **Aliases for column:-**

  testdb=# select id as emp_id from emp ;


.. _constraints:

======================
Constraints:
======================

* Constraints are the rules enforced on data columns on table. These are used to prevent
  invalid data from being entered into the database.
* This ensures the accuracy and reliability of the data in the database.
* Constraints could be column level or table level. Column level constraints are applied only
  to one column whereas table level constraints are applied to the whole table. Defining a
  data type for a column is a constraint in itself.
* For example, a column of type DATE constrains the column to valid dates.


**Not null Constraint:**
  
* By default, a column can hold NULL values. If you do not want a column to have a NULL value, then
   you need to define such constraint on this column specifying that NULL is now not allowed for that
   column.
* A NOT NULL constraint is always written as a column constraint.


 **Example:-**

    testdb=#create table emp (id integer not null,name character varying(50),gender character(1),age
    smallint);



**Primery key constraint**


* The PRIMARY KEY constraint specifies that the constrained columns' values must uniquely
  identify each row.
* Unlike other constraints which have very specific uses, the PRIMARY KEY constraint must
  be used for every table because it provides an intrinsic structure to the table's data.
* A table's primary key should be explicitly defined in the CREATE TABLE statement. Tables
  can only have one primary key.
* You can change the primary key of an existing table with an ALTER TABLE ... ALTER
  PRIMARY KEY statement, or by using DROP CONSTRAINT and then ADD CONSTRAINT
  in the same transaction.


   CREATE TABLE TABLE (
   column_1 data_type PRIMARY KEY,
   column_2 data_type);

 **Primery key example:-**

  * testdb=#create table Test_1 (id integer Primary key,name character varying(50),gender character(1),age
    smallint);


**Foreign key Constraint:**


* A foreign key is a column or a group of columns in a table that reference the primary key
  of another table.
* The table that contains the foreign key is called the referencing table or child table. And
  the table referenced by the foreign key is called the referenced table or parent table.
* A table can have multiple foreign keys depending on its relationships with other tables.
* In PostgreSQL, you define a foreign key using the foreign key constraint. The foreign
  key constraint helps maintain the referential integrity of data between the child and
  parent tables.



**Changing the name of the Objects**

* To rename a column of a table, you use the ALTER TABLE statement with RENAME
  COLUMN clause as follows:
  
  ALTER TABLE table_name
  RENAME COLUMN column_name TO new_column_name;

* In this statement:
 
 * First, specify the name of the table that contains the column which you want to rename
   after the ALTER TABLE clause.
 * Second, provide name of the column that you want to rename after the RENAME
   COLUMN keywords.
 * Third, specify the new name for the column after the TO keyword.


**Example:-** In this example we have changed the column name from id to student_id

   testdb=#ALTER TABLE Test_1
   RENAME COLUMN id TO Student_id;



**Adding Comments to a table:**



* you can add a comments to a table or column by using the COMMENT statement
* testdb=#comment on table employee is ‘employee information’;
* you can see all these comments by using \d+

.. _array:

==========================
Arrays in PostgreSQL
==========================
* Array plays an important role in PostgreSQL. Every data type has its own companion array type e.g.,
  integer has an integer[] array type, character has character[] array type, etc. In case you define your own
  data type, PostgreSQL creates a corresponding array type in the background for you.
* PostgreSQL allows you to define a column to be an array of any valid data type including built-in type,
  user-defined type or enumerated type.
* The following CREATE TABLE statement creates the contacts table with the phones column is defined as
  an array of text.


   testdb=#CREATE TABLE contacts (id serial PRIMARY KEY,name VARCHAR (100),
          phones TEXT[]);

   testdb=#INSERT INTO contacts (name, phones) VALUES('John Doe',
          ARRAY [ '(408)-589-5846','(408)-589-5555' ]);

* The phones column is a one-dimensional array that holds various phone numbers that a contact may
  have.


 **Accessing Arrays:**

 * We can use array element in the WHERE clause as the condition to filter the rows. For example, to find
   out who has the phone number (898)-589-7675 as the second phone number, we use the following
   query.


    dvdrental=# SELECT name
    FROM contacts
    WHERE phones [ 2 ] = '(898)-589-7675';
 

 **Updates to Array:**


  **Modifying PostgreSQL array:-**
  
   * PostgreSQL allows you to update each element of an array or the whole array. The following
     statement updates the second phone number of William Gate.


     dvdrental=#UPDATE contacts
     SET phones [2] = '(408)-589-5843'
     WHERE ID = 3;


.. _function:

=====================
Using SQL Functions
=====================

* It Can be used in SELECT statements and WHERE clauses
* Include

 * String Functions
 * Format Functions
 * Date & Time Functions

* Aggregate Functions
* Example:-
* Upper It will display all the department names in CAPITAL letters.
* lower - It will display all the department names in SMALL letters.



**Example:-**

* Upper It will display all the department names in CAPITAL letters.
* lower - It will display all the department names in SMALL letters.
* testdb=#select lower(name) from emp;
* testdb=#select upper(name) from emp;


 **String Functions**

  * PostgreSQL provides plenty of functions and operators for manipulating strings, will consider few of
    them: the string concatenation operator ||, char_length(), substring(), trim() and replace().
  * char_length() and length(). In Postgres both of these functions work the same. They count how
    many characters make up a given string.
  * testdb=#select first_name,length(first_name),char_length(first_name) from employee;


 **String Functions – Pattern Matching**

 * LIKE can be used for simple pattern matching and its case sensitive


   testdb=#select * from employee where first_name like ‘%Ans%’;
   

  **Substring()**: with three parameters extracts a substring based on a specified pattern. substring() implements
    SQL **LIKE** matching. That is, you can use the wildcards % and _ (underscore) but not the Posix regular
    expression metacharacters * and +.

     testdb=# select substring('http://www.google.co.in' from 3 for 7);


 * **trim()** removes leading or trailing characters, or both leading and trailing characters (default
   character is space), from a string.
 * testdb=#select trim (leading 'x' from 'xxx.www.google.comxxx'); 


 * The functions **ltrim()**, **rtrim()**, and **btrim()** (left trim, right trim and both trim, respectively) work like trim()
   but uses a different syntax.

 
 * The **replace()** function replaces a text (the original text) in the string with another (the replacement text). 
   It's syntax is ..

   replace(string, original, replacement)
    
   * testdb=#select replace ('i have two dogs','dog','cat');

 * Initcap – This function convert first letter of each word to capital and rest to lower case.
 * Length – Will display the number of characters in a string.
 * Lpad/rpad - Fill up the string to the length by prepending the characters.
   

     testdb=# select initcap('hello abhishek');


.. _aggregates:

==============
Aggregates
==============
