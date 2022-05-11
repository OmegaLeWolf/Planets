import mysql.connector
from tabulate import tabulate


mydb = mysql.connector.connect(
    host="localhost",
    user="omega",
    password="1234",
    database="test"
)
cursor = mydb.cursor(buffered=True)


def showTables():
    result = [["ID", "Nome", "Proximidade ao Sol", "Existencia de Vida", "Quantidade de Água em %", "Ponto mais alto"]]
    cursor.execute("select * from planets")
    #Done because if not returns list [("val1", val2, "val3", val4, "val5", val6)]
    a = cursor.fetchall()
    for i in range(len(a)):
        result.append(a[i])
    #-----------------------------------------
    print(tabulate(result, headers='firstrow', tablefmt='fancy_grid', stralign="center", numalign="center"))


def saveSQLData(name, data):
    sql = "select name from planets;"
    cursor.execute(sql)
    names = []
    a = cursor.fetchall()
    for i in range(len(a)):
        names.append(a[i])
    print(names)
    if (name,) in names:
        print("Nome já existe na base de dados!")
    else:
        sql = "select max(id) from planets;"
        cursor.execute(sql)
        id = cursor.fetchall().pop(0)[0]
        print(id)

        sql = "insert into planets values (%s, %s, %s, %s, %s, %s)"
        data = (id+1,) + (name,) + data
        cursor.execute(sql, data)

        mydb.commit()
        print("Data inserted into database")


def deleteData(data):
    sql = "select * from planets where id=(%s);"
    cursor.execute(sql, (data,))

    try:
        cursor.fetchall().pop(0)[0]
    except IndexError:
        print("Valor introduzido é inválido.")

    else:
        sql = "delete from planets where id = (%s)"
        cursor.execute(sql, (str(data),))
        print("Data removed from database")

    mydb.commit()

def returnMaxID():
    sql = "select max(id) from planets;"
    cursor.execute(sql)
    return cursor.fetchall().pop(0)[0]

def getPlanets(list):
    sql = "select * from planets where id > 8"
    cursor.execute(sql)
    a = cursor.fetchall()
    for i in range(len(a)):
        list.append(a[i])
    return list



