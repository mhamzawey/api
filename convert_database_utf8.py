from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='root',
                                 host='mysqldb',port=3306,
                                 database='backend')

cursor = cnx.cursor(buffered=True)
cmd = ("show tables")
cmd1 = "ALTER DATABASE backend CHARACTER SET utf8 COLLATE utf8_general_ci"
cursor.execute(cmd1)
cursor.execute(cmd)
for table in cursor:
    cursor2 = cnx.cursor(buffered=True)
    cmd2 = "ALTER TABLE %s CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci" %table[0]
    cmd3 = "ALTER TABLE %s DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci" %table[0]
    cursor2.execute(cmd2)
    cursor2.execute(cmd3)


cnx.close()