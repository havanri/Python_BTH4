import mysql.connector
from mysql.connector import Error
def connectDB():
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="",
                                         database="student_python")
    try:
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
    # # insertQuery = "INSERT INTO students(firstname, lastname, birth, dToan, dLy, dHoa) VALUES(%s, %s, %s, %s, %s, %s)"
    # # record = (student.firstname, student.lastname, student.birth, student.dToan, student.dLy, student.dHoa)
    # cursor.execute(insertQuery, record)

