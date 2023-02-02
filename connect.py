#import sqlite3 library
import sqlite3 as sql

#path to database file
conn = sql.connect("icons.db")

#create cursor object
cursor = conn.cursor()