  -- list the employee number, last name, first name, and salary for each employee
  select
  	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from
	employees as e
	join salaries as s on e.emp_no = s.emp_no
order by
	e.emp_no asc
 