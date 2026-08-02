SELECT COUNT(*) FROM fact_nav;

SELECT COUNT(*) FROM fact_transactions;

SELECT COUNT(*) FROM fact_performance;

SELECT AVG(nav)
FROM fact_nav;

SELECT MAX(nav)
FROM fact_nav;

SELECT MIN(nav)
FROM fact_nav;

SELECT COUNT(DISTINCT amfi_code)
FROM fact_nav;

SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

SELECT AVG(expense_ratio_pct)
FROM fact_performance;

SELECT *
FROM fact_performance
LIMIT 5;