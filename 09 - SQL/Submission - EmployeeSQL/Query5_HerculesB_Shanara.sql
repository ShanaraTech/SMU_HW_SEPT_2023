-- list the first name, last name initial, and sex of employees whose first name is Hercules AND last name begins with "B"
  select
  	e.last_name,
	e.first_name,
	e.sex
	
from
	employees as e
where 
	first_name = 'Hercules'
and 
	last_name like 'B%'

order by
	e.last_name asc
 