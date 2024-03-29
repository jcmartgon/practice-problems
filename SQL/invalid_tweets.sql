-- Jesus Carlos Martinez Gonzalez
-- 18/07/2023
-- Recyclable and low fat products (https://leetcode.com/problems/recyclable-and-low-fat-products)
/*
 Table: Tweets
 
 +----------------+---------+
 | Column Name    | Type    |
 +----------------+---------+
 | tweet_id       | int     |
 | content        | varchar |
 +----------------+---------+
 In SQL, tweet_id is the primary key for this table.
 This table contains all the tweets in a social media app.
 
 
 Find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
 
 Return the result table in any order.
 
 The result format is in the following example.
 */
SELECT tweet_id
FROM tweets
WHERE length(content) > 15;