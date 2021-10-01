-- vine table
CREATE TABLE vine_table (
  review_id TEXT PRIMARY KEY,
  star_rating INTEGER,
  helpful_votes INTEGER,
  total_votes INTEGER,
  vine TEXT,
  verified_purchase TEXT
);

-- Filter the data and create a new table to retrieve rows 
--where the total_votes count is equal to or greater than 20
SELECT * INTO filtered_votes_table
FROM vine_table
WHERE total_votes >= 20


-- Retrieve rows where the number of helpful_votes divided by total_votes is equal to or greater than 50%
SELECT * INTO helpful_votes_table
FROM filtered_votes_table 
WHERE CAST(helpful_votes AS FLOAT)/CAST(total_votes AS FLOAT) >=0.5


-- Retrieve rows where a review was written as part of the Vine program (paid), vine == 'Y'
SELECT * INTO paid_vine_table
FROM helpful_votes_table
WHERE vine = 'Y'

-- count of paid vine reviews from the filtered table
SELECT COUNT(*) AS count_paid_vine_reviews FROM paid_vine_table

-- Retrieve rows where a review was not written as part of the Vine program (unpaid), vine == 'N'
SELECT * INTO unpaid_vine_table
FROM helpful_votes_table
WHERE vine = 'N'

-- count of unpaid vine reviews from the filtered table
SELECT COUNT(*) AS count_unpaid_vine_reviews FROM unpaid_vine_table


-- review analysis table
CREATE TABLE review_analysis_table (
  Total_Reviews INTEGER,
  Number_of_5_star_Reviews INTEGER,
  Percentage_of_Paid_5_star_Reviews NUMERIC,
  Percentage_of_Unpaid_5_star_Reviews NUMERIC
);

-- count of paid 5-star reviews in the filtered table
SELECT COUNT(*) AS number_of_paid_5_star_reviews  FROM helpful_votes_table WHERE star_rating = 5 AND vine = 'Y'

-- count of unpaid 5-star reviews in the filtered table
SELECT COUNT(*) AS number_of_unpaid_5_star_reviews  FROM helpful_votes_table WHERE star_rating = 5 AND vine = 'N'

-- insert data into the review analysis table
INSERT INTO review_analysis_table VALUES (
	(SELECT COUNT(*) FROM helpful_votes_table),
	(SELECT COUNT(*) FROM helpful_votes_table WHERE star_rating = 5),
	(SELECT ROUND(100.0* x.pcount/y.pcount, 2)
	 FROM
	 (SELECT COUNT(*) AS pcount  FROM helpful_votes_table WHERE star_rating = 5 AND vine = 'Y') x
	 JOIN
	 (SELECT COUNT(*) AS pcount FROM helpful_votes_table WHERE vine = 'Y') y on 1=1),
	(SELECT ROUND(100.0* x.ucount/y.ucount, 2)
	 FROM
	 (SELECT COUNT(*) AS ucount  FROM helpful_votes_table WHERE star_rating = 5 AND vine = 'N') x
	 JOIN
	 (SELECT COUNT(*) AS ucount FROM helpful_votes_table WHERE vine = 'N') y on 1=1)
)

SELECT * FROM review_analysis_table