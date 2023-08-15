from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import locators
from excel_functions import Excel_Funtions


class Edit_Employee_Test:
    def __init__(self, file_name, sheet_name, url, username, password):
        self.file = file_name
        self.sheet = sheet_name
        self.url = url
        self.username = username
        self.password = password

    def run(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get(self.url)
        driver.implicitly_wait(10)

        driver.find_element(by=By.NAME, value=locators.Locators(
        ).login_username).send_keys(self.username)
        driver.find_element(by=By.NAME, value=locators.Locators(
        ).login_password).send_keys(self.password)
        driver.find_element(
            by=By.XPATH, value=locators.Locators().login_submit).click()

        excel_file = Excel_Funtions(self.file, self.sheet)
        rows = excel_file.row_count()

        for row in range(2, rows+1):
            first_name = excel_file.read_data(row, 6)
            middle_name = excel_file.read_data(row, 7)
            last_name = excel_file.read_data(row, 8)
            test_id = excel_file.read_data(row, 2)
            driving_license = excel_file.read_data(row, 9)
            ssn_number = excel_file.read_data(row, 10)
            gender = excel_file.read_data(row, 11)

            driver.find_element(
                by=By.XPATH, value=locators.Locators().pim_menu).click()
            driver.find_element(
                by=By.XPATH, value=locators.Locators().pim_add_new_employee_button).click()
            sleep(5)
            driver.find_element(by=By.NAME, value=locators.Locators(
            ).pim_first_name).send_keys(first_name)
            driver.find_element(by=By.NAME, value=locators.Locators(
            ).pim_middle_name).send_keys(middle_name)
            driver.find_element(
                by=By.NAME, value=locators.Locators().pim_last_name).send_keys(last_name)
            driver.find_element(
                by=By.XPATH, value=locators.Locators().pim_save_button).click()
            sleep(10)

            driver.find_element(by=By.XPATH, value=locators.Locators(
            ).pim_emp_details_driving_license).send_keys(driving_license)
            driver.find_element(by=By.XPATH, value=locators.Locators(
            ).pim_emp_details_ssn_num).send_keys(ssn_number)
            if gender == 'Male':
                driver.find_element(
                    by=By.XPATH, value=locators.Locators().pim_emp_details_gender_male).click()
            else:
                driver.find_element(by=By.XPATH, value=locators.Locators(
                ).pim_emp_details_gender_female).click()
            sleep(2)
            driver.find_element(by=By.XPATH, value=locators.Locators(
            ).piim_emp_details_save_button).click()
            sleep(5)

            actual_driving_license = driver.find_element(by=By.XPATH, value=locators.Locators(
            ).pim_emp_details_driving_license).get_attribute('value')
            actual_ssn_number = driver.find_element(by=By.XPATH, value=locators.Locators(
            ).pim_emp_details_ssn_num).get_attribute('value')

            if actual_driving_license == driving_license and actual_ssn_number == ssn_number:
                print(f"{test_id} test passed")
                excel_file.write_data(row, 12, 'Test passed')
            else:
                print(f"{test_id} test failed")
                excel_file.write_data(row, 12, 'Test failed')

        driver.quit()
