from logging import error
import psycopg2
import psycopg2.extras

hostname="localhost"
database="demo"
username="postgres"
pwd="Mark"
port_id=5432
conn=None
#The Cursor class of the psycopg library provide methods to execute the PostgreSQL commands in the database using python code.
#Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
#You can create Cursor object using the cursor() method of the Connection object/class
cur=None
try:
    conn=psycopg2.connect(host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id)

    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # create_script='create table employee (id int primary key,name varchar(20),salary int,dept_id varchar(30))'
    # cur.execute(create_script)

    insert_script='insert into employee(id,name,salary,dept_id) values (%s,%s,%s,%s)' #%s is used as a placeholder for string values you want to inject into a formatted string
    insert_record=[(4,'Anju',18000,'D3'),(3,'Arthy',18000,'D1')]
    for i in insert_record:
        cur.execute(insert_script,i)
    
    #update_script='UPDATE EMPLOYEE SET SALARY=SALARY+(SALARY*0.5)'
    #cur.execute(update_script)

    # delete_script='DELETE FROM EMPLOYEE WHERE name= %s'
    # delete_record=('Anu',)
    # cur.execute(delete_script,delete_record)

    select_script='SELECT * FROM EMPLOYEE'
    cur.execute(select_script)

    for records in cur.fetchall():
         print(records['name'],records['salary'])
    #print(cur.fetchall())
    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()