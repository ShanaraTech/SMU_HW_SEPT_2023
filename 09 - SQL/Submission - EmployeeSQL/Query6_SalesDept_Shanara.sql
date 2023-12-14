 -- list each employee in the Sales department, their employee number, last name, and first name, 
select
  	e.emp_no,
	e.first_name,
	e.last_name,
	de.emp_no,
	d.dept_name
from
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	inner join departments as d on de.dept_no = d.dept_no 
where 
	dept_name = 'Sales'
	
order by
	de.emp_no asc;