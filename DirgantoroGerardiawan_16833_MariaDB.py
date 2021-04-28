# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )


# Get Cursor
cur = conn.cursor()



print(" Program Demo Operasi CRUD SQLite Database ")
print("       Lab Komputasi DTM SV UGM            ")
print("===========================================\n")
print("Menu operasi database")
print("1. Create database dan tabel")
print("2. Insert data")
print("3. Select/search data")
print("4. Update data")
print("5. Delete data")
menu=input("Silahkan pilih operasi ( 1/2/3/4/5 ) ? ")
print("Anda memilih : " + menu)
if menu=='1' :
    print("Create database dan tabel")
    # create a database named bengkel
     conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )
    cur = conn.cursor()
  
    # create a table named user
    
elif menu=='2' :
    
    print("Insert data")
    cur.execute(
    "SELECT first_name,last_name FROM employees WHERE first_name=?", 
    (some_name,))
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )
    cur = conn.cursor()
    
elif menu=='3' :
    print("Select/search data")
    cur.execute(
    "SELECT first_name,last_name FROM employees WHERE first_name=?", 
    (some_name,))
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )
    cur = conn.cursor()
elif menu=='4' :
    print("Update data")
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )
    cur = conn.cursor()
elif menu=='5' :
    print("Delete data")
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"

    )
    cur = conn.cursor()