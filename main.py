from login_tests import Login_Test
from add_employee_tests import Add_Employee_Test
from edit_employee_tests import Edit_Employee_Test
from delete_employee_tests import Delete_Employee_Test

test_file_name = 'D:\Meena\orange-hrm-tests\Project_test_data.xlsx'
login_test_sheet = 'LOGIN TEST'
login_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
add_employee = 'ADD EMPLOYEE'
edit_employee = 'EDIT EMPLOYEE'
username = 'Admin'
password = 'admin123'

# login = Login_Test(test_file_name, login_test_sheet, login_url)
# login.run()


# add_employee_test = Add_Employee_Test(test_file_name, add_employee, login_url,username, password)
# add_employee_test.run()


# edit_employee_test = Edit_Employee_Test(test_file_name, edit_employee, login_url, username, password)
# edit_employee_test.run()


delete_employee_test = Delete_Employee_Test(login_url, username, password)
delete_employee_test.run()
