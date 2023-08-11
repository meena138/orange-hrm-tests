from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import locators
from excel_functions import Excel_Funtions


class Add_Employee_Test:
    def __init__(self,file_name, sheet_name, url, username, password):
        self.file = file_name
        self.sheet = sheet_name
        self.url = url
        self.username = username
        self.password = password    
    
    def run(self):        
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get(self.url)   
        driver.implicitly_wait(10)

        driver.find_element(by=By.NAME, value=locators.Locators().login_username).send_keys(self.username)
        driver.find_element(by=By.NAME, value=locators.Locators().login_password).send_keys(self.password)
        driver.find_element(by=By.XPATH, value=locators.Locators().login_submit).click()
    
        excel_file = Excel_Funtions (self.file,self.sheet)
        rows=excel_file.row_count()

        for row in range(2,rows+1):
            first_name = excel_file.read_data(row,6)
            middle_name = excel_file.read_data(row,7)
            last_name = excel_file.read_data(row,8)
            test_id = excel_file.read_data(row,2)

            driver.find_element(by=By.XPATH, value=locators.Locators().pim_menu).click()
            driver.find_element(by=By.XPATH, value=locators.Locators().pim_add_new_employee_button).click()
            sleep(5)
            driver.find_element(by=By.NAME, value=locators.Locators().pim_first_name).send_keys(first_name)
            driver.find_element(by=By.NAME, value=locators.Locators().pim_middle_name).send_keys(middle_name)
            driver.find_element(by=By.NAME, value=locators.Locators().pim_last_name).send_keys(last_name)
            driver.find_element(by=By.XPATH, value=locators.Locators().pim_save_button).click()
            sleep(10)

            actual_first_name = driver.find_element(by=By.NAME, value=locators.Locators().pim_first_name).get_attribute('value')
            actual_middle_name = driver.find_element(by=By.NAME, value=locators.Locators().pim_middle_name).get_attribute('value')
            actual_last_name = driver.find_element(by=By.NAME, value=locators.Locators().pim_last_name).get_attribute('value')

            if 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee' in driver.current_url:
                if first_name == "" or last_name == "":
                    print(f"{test_id} test passed")
                    excel_file.write_data(row,9,'Test passed')
                else:
                    print(f"{test_id} test failed")
                    excel_file.write_data(row, 9,'Test failed')
            else:
                print(f"{actual_first_name} {actual_middle_name} {actual_last_name} employee detail added")
                if actual_first_name == first_name and actual_middle_name == middle_name and actual_last_name == last_name:
                    print(f"{test_id} test passed")
                    excel_file.write_data(row,9,'Test passed')
                else:
                    print(f"{test_id} test failed")
                    excel_file.write_data(row,9,'Test failed')
        
        driver.quit()
