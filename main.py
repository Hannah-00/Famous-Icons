# import our modules
from readIcons import read
from addIcons import insertIcons
from updateIcons import update
from deleteIcons import delete
from sortIcons import sort
from time import sleep

# create menu subroutine
def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5","6"]:
        sleep(2)
        print(
            """
            Select an Option below:
            1. View all Icons
            2. Add Icons
            3. Update Icons
            4. Delete Icons
            5. Sort Icons
            6. Exit
        """)
        options = input("Enter an Option: ")
        if options not in ["1", "2", "3", "4", "5","6"]:
            print(options + " is not a valid choice, please try again")
    return options

# "flag" variable
mainProgram = True
while mainProgram == True:
    mainMenu = menuOptions()
    if mainMenu == "1":
        read()
    elif mainMenu == "2":
        insertIcons()
    elif mainMenu == "3":
        update()
    elif mainMenu == "4":
        delete()
    elif mainMenu == "5":
        sort()
    else:
        mainProgram = False

input("Press Enter to exit")
