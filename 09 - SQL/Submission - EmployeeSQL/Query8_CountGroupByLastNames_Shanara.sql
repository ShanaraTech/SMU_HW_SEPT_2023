  -- list the frequency counts of all employees that share a last name, in descending order
select
  	e.last_name,
	Count (last_name) as total
from
	employees as e
group by
	last_name
order by 
	e.last_name desc;