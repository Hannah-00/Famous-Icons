#import the connect module
from connect import *

#create table for icons
cursor.execute(
    """
CREATE TABLE "icons" (
	"IconID"	INTEGER NOT NULL UNIQUE,
	"firstName"	TEXT,
	"lastName"	TEXT,
	"Career"	TEXT,
    "DOB"       INT,
	PRIMARY KEY("IconID" AUTOINCREMENT)
)"""
)