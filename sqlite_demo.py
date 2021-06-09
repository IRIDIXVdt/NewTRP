import sqlite3
from employee import Employee


conn = sqlite3.connect('employee.db')

c = conn.cursor()

# we can only have
# null, integer, real, text, blob

# c.execute("""
#     CREATE TABLE employees(
#         first text,
#         last text,
#         pay integer
#     )""")

emp_1 = Employee('John','Doe',8000)
emp_2 = Employee('Hane','Doe',9000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)


c.execute("INSERT INTO employees VALUES (?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))


# c.execute("INSERT INTO employees VALUES('Mary','Scha',50000)")
c.execute("SELECT * FROM employees WHERE last = ?", ('Doe',))
# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchone())
print(c.fetchall())

conn.commit()

conn.close()