from DAOImpl.StudentDAOImpl import StudentDAOImpl

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
        studentDAO.findAll()
    elif choice == "2":
        code = input("Nhập mã sinh viên: ")
        firstName = input("Nhập họ và tên đệm: ")
        lastName = input("Nhập tên: ")
        dob = input("Nhập ngày sinh (dd/mm/YYYY): ")
        math = float(input("Nhập điểm toán: "))
        physics = float(input("Nhập điểm lý: "))
        chemistry = float(input("Nhập điểm hóa: "))
        studentDAO.insert((code, firstName, lastName, dob, math, physics, chemistry))
    elif choice == "3":
        studentId = input('Nhập id muốn cập nhật: ')
        student = studentDAO.findById(studentId)
        if student is None:
            print("Không tìm thấy sinh viên")
        else:
            print(student)
            code = input("Nhập mã sinh viên: ")
            firstName = input("Nhập họ và tên đệm: ")
            lastName = input("Nhập tên: ")
            dob = input("Nhập ngày sinh (dd/mm/YYYY): ")
            math = float(input("Nhập điểm toán: "))
            physics = float(input("Nhập điểm lý: "))
            chemistry = float(input("Nhập điểm hóa: "))

            studentDAO.update((code, firstName, lastName, dob, math, physics, chemistry, studentId))

    elif choice == "4":
        studentId = input('Nhập id muốn xoá: ')
        studentDAO.delete(studentId)
    elif choice == "5":
        studentId = input('Nhập id muốn tìm: ')
        student = studentDAO.findById(studentId)
        if student is None:
            print("Không tìm thấy sinh viên")
        else:
            print(student)
    elif choice == "6":
        exit_program()
    else:
        print("Vui lòng chọn một lựa chọn hợp lệ.")
