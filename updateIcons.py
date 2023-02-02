from connect import *
from time import sleep
from readIcons import read

#subroutine to update records
def update():
    # use iconID to update records
    idfield = input("Enter the Icon ID of the record you want to update: ")
    #ask for the field they want to update
    fieldName = input("Which field would you like to update (firstName/lastName/Career/DOB): " ).title()
    # enter value to update to
    newFieldValue = input(f"Enter the value for {fieldName}: ")
    #print(newFieldValue)
    newFieldValue = "'" + newFieldValue + "'"
    #print(newFieldValue)
    
    cursor.execute(f"UPDATE icons SET {fieldName} = {newFieldValue} WHERE IconID = {idfield} ")
    conn.commit()

    print(f"Record {idfield} was updated")
    sleep(2) # delay for 3 second before executing the code block below
    read() #call/invke the read subroutine from the readSongs application
