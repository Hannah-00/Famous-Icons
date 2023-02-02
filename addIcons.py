from connect import *
from time import sleep
from readIcons import read

#subroutine to insert icon records
def insertIcons():
    #create an empty list
    icons = []
    #ask for input
    firstName = input("Enter Icon's first name: ")
    lastName = input("Enter Icon's last name: ")
    career = input("Enter thier line of work: ")
    dob = input("Enter their year of birth: ")

    icons.append(firstName)
    icons.append(lastName)
    icons.append(career)
    icons.append(dob)
    #test
    #print(icons)

    #insert into icons values(null, title, artist, genre)
    cursor.execute("insert into icons values(null, ?, ?, ?, ?)", icons)
    #commit the changes to the database
    conn.commit()
    print(f"{firstName} {lastName} added to icon list")
    sleep(2)

    read()
  
