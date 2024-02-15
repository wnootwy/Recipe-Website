import mysql.connector
import numpy as np
connect = mysql.connector.connect(user="website_user",
            host="localhost",
            password="goatsquad",
            database="gracert"
        )

cursor = connect.cursor()
query = "select * from Users"
cursor.execute(query)
result = cursor.fetchall()
for i in range(len(result)):
    result[i] = list(result[i])
result = np.array(result)
