import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1310',
    database='practice1'
)

cursor = conn.cursor()

# creating a table
create_table = """CREATE TABLE IF NOT EXISTS EMPLOYEES(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(100),
DEPARTMENT VARCHAR(100), SALARY FLOAT);"""
cursor.execute(create_table)
print("table employees created successfully")

# insert query
insert_data = """INSERT INTO EMPLOYEES (NAME, DEPARTMENT, SALARY) VALUES ('RAHUL', 'ENGINEERING', 75000),
('GEETHA', 'MARKETING', 60000), ('PRIYA', 'HR', 50000);
"""
cursor.execute(insert_data)
conn.commit()
print("data inserted successfully")

# update data
update_data = """UPDATE EMPLOYEES SET SALARY = 65000 WHERE DEPARTMENT = 'MARKETING';"""
cursor.execute(update_data)
conn.commit()
print("data UPDATED successfully")

# DELETE DATA
delete_data = """DELETE FROM EMPLOYEES WHERE NAME = 'RAHUL';"""
cursor.execute(delete_data)
conn.commit()
print("data deleted successfully")

# close connection
cursor.close()
conn.close()



