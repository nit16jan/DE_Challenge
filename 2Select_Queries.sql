--list of our customers and their spending
SELECT 
cust.customer_name,
sum(s.total_price) as spending
from sales s, customer cust
where s.customer_id = cust.customer_id
group by cust.customer_name

--top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month

SELECT
m.manufacturer_name,
sum(s.total_price) as sales_number,
sum(s.quantity) as sales
from sales s, cars c, manufacturer m
where s.car_id = c.car_id
and c.manufacturer_id = m.manufacturer_id
and s.sales_dt >= date_trunc('month', CURRENT_DATE)
group by m.manufacturer_name
order by 2 desc, 3 desc
limit 3