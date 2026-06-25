SELECT 
  COUNT(*) AS total_customers,
  SUM(exited) AS churned_customers,
  ROUND(100.0*SUM(exited)/COUNT(*),2)AS churn_rate_percent
FROM customer_churn;


SELECT 
  geography,
  COUNT(*) AS total_customers,
  SUM(exited) AS churned_customers,
  ROUND(100.0*SUM(exited)/COUNT(*),2)AS churn_rate_percent
FROM customer_churn
GROUP BY geography
ORDER BY churn_rate_percent DESC;


SELECT
    gender,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate_percent
FROM customer_churn
GROUP BY gender
ORDER BY churn_rate_percent DESC;


SELECT
    is_active_member,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate_percent
FROM customer_churn
GROUP BY is_active_member
ORDER BY churn_rate_percent DESC;


SELECT
    num_of_products,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate_percent
FROM customer_churn
GROUP BY num_of_products
ORDER BY num_of_products;


SELECT
    CASE
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 39 THEN '30-39'
        WHEN age BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50+'
    END AS age_group,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate_percent
FROM customer_churn
GROUP BY age_group
ORDER BY churn_rate_percent DESC;


SELECT
    CASE
        WHEN credit_score < 500 THEN 'Poor'
        WHEN credit_score BETWEEN 500 AND 699 THEN 'Average'
        ELSE 'Good'
    END AS credit_category,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate_percent
FROM customer_churn
GROUP BY credit_category
ORDER BY churn_rate_percent DESC;