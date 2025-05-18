-- 1. Top 10 spending customers
SELECT
  customer_id,
  COUNT(*) AS total_orders,
  SUM(total_price) AS total_spent
FROM `get-coordenates.cm_learning_projects.orders_cleaned`
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;

-- 2. Orders per day
SELECT
  order_date,
  COUNT(*) AS total_orders,
  SUM(total_price) AS total_revenue
FROM `get-coordenates.cm_learning_projects.orders_cleaned`
GROUP BY order_date
ORDER BY order_date;

-- 3. Average order value by customer
SELECT
  customer_id,
  ROUND(AVG(total_price), 2) AS avg_order_value
FROM `get-coordenates.cm_learning_projects.orders_cleaned`
GROUP BY customer_id
ORDER BY avg_order_value DESC
LIMIT 10;

-- 4. Order status distribution
SELECT
  status,
  COUNT(*) AS total
FROM `get-coordenates.cm_learning_projects.orders_cleaned`
GROUP BY status;
