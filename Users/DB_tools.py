

def login(database):
    import adodbapi
    db = database
    tablename = "Users"
    constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s'  % db
    Fields = ["ID", "User", "Password"]

    # connect to the database
    conn = adodbapi.connect(constr)

    login = input('Login: ')
    password = input('Haslo: ')

    # create a cursor
    cur = conn.cursor()

    sql = 'SELECT * FROM Users'
    cur.execute(sql)
    result = cur.fetchall()
    logged = False
    user_exist = False
    for item in result:
        i_user = item[1]
        i_pass = item[2]
        if i_user == login:
            user_exist = True
            if i_pass == password:
                logged = True

    if user_exist == True:
        if logged:
            print ('Zalogowano')
        else:
            print ('Bledne Haslo')
    else:
        print ('Nie ma takiego usera')

    # close the cursor and connection
    cur.close()
    conn.close()

    return logged

def register(database):
    import adodbapi
    db = database
    tablename = "Users"
    constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s'  % db
    Fields = ["ID", "User", "Password"]

    # connect to the database
    conn = adodbapi.connect(constr)

    # create a cursor
    cur = conn.cursor()

    sql = "SELECT * FROM Users"
    cur.execute(sql)
    result = cur.fetchall()

    sql = "SELECT Id FROM Users"
    cur.execute(sql)
    result = cur.fetchall()
    last_id_sql = str(result[len(result)-1])
    last_id = last_id_sql.replace(")", "")
    last_id = last_id.replace("(", "")
    last_id = last_id.replace(",", "")
    last_id = last_id.replace("'", "")
    new_id = int(last_id) + 1

    login = input('Login: ')
    password1 = input('Haslo: ')
    password2 = input('Potwierdz Haslo: ')

    while password1 != password2:
        print ('Hasla nie pasuja')
        login = input('Login: ')
        password1 = input('Haslo: ')
        password2 = input('Potwierdz Haslo: ')

    user_f = "User"
    pass_f = "Password"
    if password1 == password1:
        sql = """INSERT INTO Users VALUES ( '""" + str(new_id) + """', '""" + str(login) + """','""" + str(password1) + """')"""
        input("Press Enter to confirm")
        cur.execute(sql)

    conn.commit()