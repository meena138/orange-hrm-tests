from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import locators
from excel_functions import Excel_Funtions

class Login_Test:

    def __init__(self,file_name, sheet_name, url):
        self.file = file_name
        self.sheet = sheet_name
        self.url = url

    def run(self):
        excel_file = Excel_Funtions (self.file,self.sheet)
       
        rows=excel_file.row_count()

        for row in range(2,rows+1):
            username = excel_file.read_data(row,6)
            password = excel_file.read_data(row,7)
            expected_result = excel_file.read_data(row,8)
            test_id = excel_file.read_data(row,2)
             
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get(self.url)
            driver.implicitly_wait(10)        

            driver.find_element(by=By.NAME, value=locators.Locators().login_username).send_keys(username)
            driver.find_element(by=By.NAME, value=locators.Locators().login_password).send_keys(password)
            driver.find_element(by=By.XPATH, value=locators.Locators().login_submit).click()

            if expected_result in driver.current_url:
                print(f"{test_id} test passed")
                excel_file.write_data(row, 9,'Test passed')
            else:
                print(f"{test_id} test failed")
                excel_file.write_data(row,9,'Test failed')
        
            driver.quit()