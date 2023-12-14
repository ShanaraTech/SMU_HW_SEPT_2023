  -- list the first name, first name, and hire date for each employee hired in 1986
select
  	e.first_name,
	e.last_name,
	e.hire_date
from
	employees as e
where extract(Year From hire_date) = 1986
order by 
	e.hire_date asc;

 