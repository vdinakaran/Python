from ast import Delete
from re import S
from select import select
import psycopg2

conn=psycopg2.connect(host="localhost",dbname="demo",user="postgres",password="Mark")
cur=conn.cursor()
def view():
    id=(input("Enter the Customer id:"))
    select_query='SELECT * FROM Customer WHERE id=(%s)'
    select_input=id
    cur.execute(select_query,select_input)
    print(cur.fetchone())
def add():
    id=input("Enter the Customer id:")
    name=input("Enter Customer name:")
    salary=input("Enter the salary:")
    insert_query='INSERT INTO Customer(id,name,salary) VALUES(%s,%s,%s)'
    insert_input=(id,name,salary)
    cur.execute(insert_query,insert_input)
def allEmp():
    select_query='SELECT * FROM Customer'
    cur.execute(select_query)
    for records in cur.fetchall():
        print(records)
def delete():
    id=(input("Enter the id:"))
    delete_query='DELETE FROM Customer WHERE id= %s'
    delete_input=(id,)
    cur.execute(delete_query,delete_input)
def update():
    id=input("Enter Customer id:")
    salary=(input("Enter the salary:"))
    update_query=('UPDATE Customer SET salary=%s where id=%s')
    update_data=(salary,id)
    cur.execute(update_query,update_data)



print("Customer details")
print("***************************")
print("1.View Customer Details")
print("2.Add Customer Details")
print("3.Update Customer Details")
print("4.Delete Customer")
print("5.All Customer Details")
choice=input("Enter the Choice")
if choice=='1':
        view()
elif choice=='2':
        add()
elif choice=='3':
        update()
elif choice=='4':
        delete()
elif choice=='5':
        allEmp()
else:
        print("Incorrect option.Please choose the correct option.....")

cur.close()
conn.close()
