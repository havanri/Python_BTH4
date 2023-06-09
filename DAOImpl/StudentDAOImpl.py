from datetime import datetime

from MySQLdb._mysql import connection

from DAO import DB
from DAO.StudentDAO import StudentDAO


class StudentDAOImpl(StudentDAO):

    def __init__(self):
        self.conn = DB.connectDB()

    def findAll(self):
        try:
            connection = self.conn
            cursor = connection.cursor()

            # Update single record now
            sql_get_all = "select * from students"
            cursor.execute(sql_get_all)
            record = cursor.fetchall()
            connection.commit()
            return record
        except connection.Error as error:
            connection.close()
            print("Failed to get all record: {}".format(error))

    def insert(self, student):
        print(student.masv)
        try:
            connection = self.conn
            cursor = connection.cursor()
            insertQuery = "INSERT INTO students(masv, firstname, lastname, dob, math, physical, chemistry) " \
                          "VALUES(%s, %s, %s, %s, %s, %s, %s)"
            val = (student.masv, student.firstname, student.lastname, datetime.strptime(student.dob, '%d/%m/%Y'),
            student.math, student.physical,
            student.chemistry)
            cursor.execute(insertQuery, val)
            connection.commit()
            print("Thêm sinh viên thành công")
        except connection.Error as error:
            connection.rollback()
            connection.close()
            print("Failed to get all record: {}".format(error))

    def update(self, student):
        print('update')
        try:
            connection = self.conn
            cursor = connection.cursor()

            # Update single record now
            sql_update_query = "Update students set masv = %s, firstname = %s, lastname = %s, dob = %s, " \
                               "math = %s, physical = %s, chemistry = %s where id = %s"
            val = (
                student[0], student[1], student[2], datetime.strptime(student[3], '%d/%m/%Y'),
                student[4], student[5], student[6], student[7])
            cursor.execute(sql_update_query, val)
            connection.commit()
            print("Record Updated successfully ")


        except connection.Error as error:
            connection.rollback()
            connection.close()
            print("Failed to update table record: {}".format(error))

    def findById(self, studentId):
        try:
            connection = self.conn
            cursor = connection.cursor()

            # Update single record now
            sql_find_query = "select * from students where id =" + studentId
            cursor.execute(sql_find_query)
            record = cursor.fetchone()

            connection.commit()
            return record
        except connection.Error as error:
            connection.rollback()
            connection.close()
            print("Failed to update table record: {}".format(error))

    def delete(self, studentId):
        try:
            connection = self.conn
            cursor = connection.cursor()

            # Update single record now
            sql_delete_query = "DELETE FROM students where id =" + studentId
            cursor.execute(sql_delete_query)
            print("Deleted sucessfully")
            connection.commit()
        except connection.Error as error:
            connection.rollback()
            connection.close()
            print("Failed to delete table record: {}".format(error))
