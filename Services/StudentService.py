from DAOImpl.StudentDAOImpl import StudentDAOImpl
from Entities.Student import  Student
def menu():
    print("MENU")
    print("1. Hiển thị từ các sinh viên")
    print("2. Tạo mới một sinh viên")
    print("3. Cập nhật một sinh viên")
    print("4. Xóa một sinh viên")
    print("5. Tìm sinh viên theo id")
    print("6. Thoát chương trình")

def exit_program():
    print("Chương trình đã kết thúc")
    exit()

studentDAO = StudentDAOImpl()
while True:
    menu()
    choice = input("Vui lòng chọn một chức năng: ")
    if choice == "1":
        print("==== List Student ====")
        students = studentDAO.findAll()
        s = '| %s | %s | %s %s | %s | %s | %s | %s |'
        head = ['ID', 'Mã sinh viên', 'Họ', 'tên', 'Ngày sinh', 'Điểm toán', 'Điểm lý', 'Điểm hóa']
        print('| {:3s} | {:10s} | {:20s} | {:10s} | {:10s} | {:10s} | {:10s} | {:10s} |'
              .format('ID', 'Mã sinh viên', 'Họ', 'tên', 'Ngày sinh', 'Điểm toán', 'Điểm lý', 'Điểm hóa'))
        # print (s % tuple(head))
        for student in students:
            # print (s % tuple(student))
            print('| {:3d} | {:12s} | {:20s} | {:10s} | {:10s} | {:10.2f} | {:10.2f} | {:10.2f} |'
                  .format(student[0], student[1], student[2], student[3], student[4].strftime("%d-%m-%Y"), student[5], student[6], student[7]))
    elif choice == "2":
        code = input("Nhập mã sinh viên: ")
        firstName = input("Nhập họ và tên đệm: ")
        lastName = input("Nhập tên: ")
        dob = input("Nhập ngày sinh (dd/mm/YYYY): ")
        math = float(input("Nhập điểm toán: "))
        physics = float(input("Nhập điểm lý: "))
        chemistry = float(input("Nhập điểm hóa: "))
        print(firstName)
        student = Student(code, firstName, lastName, dob, math, physics, chemistry)
        studentDAO.insert(student)
    elif choice == "3":
        studentId = input('Nhập id muốn cập nhật: ')
        student = studentDAO.findById(studentId)
        if student is None:
            print("Không tìm thấy sinh viên")
        else:
            print('| {:3d} | {:12s} | {:20s} | {:10s} | {:10s} | {:10.2f} | {:10.2f} | {:10.2f} |'
                  .format(student[0], student[1], student[2], student[3], student[4].strftime("%d-%m-%Y"), student[5],
                          student[6], student[7]))
            code = input("Nhập mã sinh viên: ")
            firstName = input("Nhập họ và tên đệm: ")
            lastName = input("Nhập tên: ")
            dob = input("Nhập ngày sinh (dd/mm/YYYY): ")
            math = float(input("Nhập điểm toán: "))
            physics = float(input("Nhập điểm lý: "))
            chemistry = float(input("Nhập điểm hóa: "))
            studentDAO.update((code, firstName, lastName, dob, math, physics, chemistry,studentId))
            print("After updating record ")
            studentAfterUpdated = studentDAO.findById(studentId)
            print('| {:3d} | {:12s} | {:20s} | {:10s} | {:10s} | {:10.2f} | {:10.2f} | {:10.2f} |'
                  .format(studentAfterUpdated[0], studentAfterUpdated[1], studentAfterUpdated[2], studentAfterUpdated[3],
                          studentAfterUpdated[4].strftime("%d-%m-%Y"), studentAfterUpdated[5],
                          studentAfterUpdated[6], studentAfterUpdated[7]))
    elif choice == "4":
        studentId = input('Nhập id muốn xoá: ')
        student = studentDAO.findById(studentId)
        if student is None:
            print("Không tìm thấy sinh viên")
        else:
            print('| {:3d} | {:12s} | {:20s} | {:10s} | {:10s} | {:10.2f} | {:10.2f} | {:10.2f} |'
                  .format(student[0], student[1], student[2], student[3], student[4].strftime("%d-%m-%Y"), student[5],
                          student[6], student[7]))

            print('Bạn có chắc chắn xóa thông tin này ?')
            print('1.Vâng')
            print('2.Hủy')
            confirm = int(input("Vui lòng chọn 1 trong 2: "))
            if confirm == 1:
                studentDAO.delete(studentId)
    elif choice == "5":
        studentId = input('Nhập id muốn tìm: ')
        student = studentDAO.findById(studentId)
        if student is None:
            print("Không tìm thấy sinh viên")
        else:
            print('| {:3d} | {:12s} | {:20s} | {:10s} | {:10s} | {:10.2f} | {:10.2f} | {:10.2f} |'
                  .format(student[0], student[1], student[2], student[3], student[4].strftime("%d-%m-%Y"), student[5],
                          student[6], student[7]))
    elif choice == "6":
        exit_program()
    else:
        print("Vui lòng chọn một lựa chọn hợp lệ.")