 -- list the department number, department name, employee number, last name, first name, for each employee
  select
  	e.emp_no,
	e.first_name,
	e.last_name,
	de.dept_no,
	de.emp_no,
	d.dept_name
from
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	inner join departments as d on de.dept_no = d.dept_no 
	
order by
	de.emp_no asc;