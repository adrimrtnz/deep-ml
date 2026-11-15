SELECT 
    DATE_TRUNC('month', review_date)::datetime AS month,
    product_id,
    AVG(stars) AS avg_stars
from reviews
GROUP BY 1, 2
