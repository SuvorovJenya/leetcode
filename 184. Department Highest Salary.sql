-- Write your PostgreSQL query statement below
with cte as (
    select
        *,
        dense_rank() over (partition by departmentId order by salary desc) as ds
    from Employee
)
select t2.name as Department , t1.name as Employee, t1.salary as Salary
from cte t1
join Department t2 on t1.departmentid = t2.id
where ds = 1;