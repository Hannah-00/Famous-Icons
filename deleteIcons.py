from connect import *
from time import sleep
from readIcons import read

#subroutine to delete records
def delete():
    # use iconIDto delete records
    idfield = input("Enter the Icon ID of the record you want to delete: ")

    #delete icons by id
    cursor.execute(f"DELETE FROM icons WHERE IconID = {idfield} ")
    conn.commit()
    print(f"Record {idfield} deleted")

    sleep(2)
    read()
