SELECT a1.machine_id, 
    ROUND(AVG(a2.timestamp - a1.timestamp)::NUMERIC, 3) AS processing_time
FROM Activity a1
join Activity a2 
    on a1.machine_id = a2.machine_id
    and a1.activity_type = 'start'
    and a2.activity_type = 'end'
    and a1.process_id = a2.process_id
group by a1.machine_id;

