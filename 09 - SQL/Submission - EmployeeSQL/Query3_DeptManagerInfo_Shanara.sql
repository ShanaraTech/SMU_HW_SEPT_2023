 -- list each department manager's: department number, department name, employee number, last name, and first name, 
select
 	e.emp_no,
	e.first_name,
	e.last_name,
	dm.dept_no,
	dm.emp_no,
	d.dept_name
from
	employees as e
	join dept_manager as dm on e.emp_no = dm.emp_no
	inner join departments as d on dm.dept_no = d.dept_no 
	
order by
	d.dept_name asc;
