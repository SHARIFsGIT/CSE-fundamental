-- ERD (Entity Diagram) --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Database design --
/*
1. Top down approach: 
At the top there are MODEL & at the down there are DATA. We will make the structure 
first then insert and analysis data.
 */

/*
2. Bottom up approach: 
We have available data and now want to make a MODEL.
 */
-- What to avoid in database design?
-- 01. Redundancy: if I keep duplicate data in more table.
-- 02. Incompleteness: extra data in another table.
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- ERD notations --
-- In general every database is a table and entity as well such as STUDENT database.
-- Relation table such as STUDENT_EXAM it has relation, table but no entity.
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- ERD primary key, Relations between tables --
-- Relation type --
-- 01. One to one: only one row from table A is related with another table B
-- 02. One to many: one row of table A has relation with multiple rows of table B
-- 03. Many to many: multiple rows of table A has relation with multiple rows of table B
-- Cardinality: the ratio of participation to other table
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Strong entity, Weak entity --
-- Strong entity: has dedicated primary key. It doesn't depend on other entity.
-- Weak entity: has no dedicated primary key. Depends on another entity. 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- ERD attributes --
-- 01. Composite: multiple attributes such as first name, last name in an entity
-- 02. Multivalued: more than one attribute such as {phone_number}
-- 03. Derived: one entity has DOB and AGE attribute. AGE() is derived by DOB
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- ERD generalization, specialization --