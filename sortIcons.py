from connect import *
from time import sleep
from readIcons import read

#subroutine to sort records
def sort():
    #ask for field they want to sort by
    fieldName = input("Which field would you like to sort by (firstName/lastName/Career/DOB): " ).title()
    cursor.execute(f"SELECT * FROM icons ORDER BY {fieldName}")
    conn.commit()

    print(f"Sorting by {fieldName}")
    sleep(2)
    row = cursor.fetchall()
    for record in row:
        print(record)
