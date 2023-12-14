 -- list each employee in the Sales & Development departments, their employee number, last name, first name, and department name

select
  	e.emp_no,
	e.first_name,
	e.last_name,
	de.dept_no,
	de.emp_no,
	d.dept_name
from
	departments as d
	join dept_emp as de on d.dept_no = de.dept_no
	join employees as e on de.emp_no = e.emp_no 
where 
	dept_name = 'Sales'
or
	dept_name = 'Development'
	
order by
	d.dept_no desc;