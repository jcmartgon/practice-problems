-- Jesus Carlos Martinez Gonzalez
-- 17/07/2023
-- Recyclable and low fat products (https://leetcode.com/problems/recyclable-and-low-fat-products)
/*
 Table: Products
 
 +-------------+---------+
 | Column Name | Type    |
 +-------------+---------+
 | product_id  | int     |
 | low_fats    | enum    |
 | recyclable  | enum    |
 +-------------+---------+
 In SQL, product_id is the primary key for this table.
 low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
 recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
 
 
 Find the ids of products that are both low fat and recyclable.
 
 Return the result table in any order.
 
 The result format is in the following example.
 */
SELECT product_id
FROM products
WHERE low_fats = "Y"
    AND recyclable = "Y";