from connect import *

#subroutine to read print table
def read():
    #select all songs
    cursor.execute("select * from icons")
     # Fetchall() method, which fetches all rows from the last executed statement.
    row = cursor.fetchall()
    for record in row:
        print(record)

#stops code running automatically if it is not a main file
if __name__ == "__main__":
    read()
