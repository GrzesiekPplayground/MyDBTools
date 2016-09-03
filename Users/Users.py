# -*- coding: utf-8 -*-

import adodbapi
from DB_tools import *

db = "D:/KAMIENIEC/IT/SQL/Baza MDB/testowa.mdb"

if login(db) == True:
    register(db)
else:
    print ("Nie zalogowano")


