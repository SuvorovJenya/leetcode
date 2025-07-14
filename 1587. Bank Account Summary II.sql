-- Write your PostgreSQL query statement below
select  
    name sum(amount) as balance
from 
    Users
join Transactions using (account)
group by name
having sum(amount) > 10000;

