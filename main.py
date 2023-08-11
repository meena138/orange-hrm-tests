from login_tests import Login_Test
from add_employee_tests import Add_Employee_Test

test_file_name = 'D:\Meena\OrangeHRM\Project_test_data.xlsx'
login_test_sheet = 'LOGIN TEST'
login_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
add_employee = 'ADD EMPLOYEE'
username = 'Admin'
password = 'admin123'

#login = Login_Test(test_file_name,login_test_sheet,login_url)
#login.run()


add_employee_test = Add_Employee_Test(test_file_name, add_employee, login_url,username, password)
add_employee_test.run()

