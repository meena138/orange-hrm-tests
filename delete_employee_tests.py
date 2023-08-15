from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import locators


class Delete_Employee_Test:
    def __init__(self, url, username, password):
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

        driver.find_element(
            by=By.XPATH, value=locators.Locators().pim_menu).click()
        sleep(5)

        deleted_row_emp_id = driver.find_element(by=By.XPATH, value=locators.Locators(
        ). pim_emp_list_emp_id).text
        deleted_row_emp_firstname = driver.find_element(by=By.XPATH, value=locators.Locators(
        ).pim_emp_list_emp_firstname).text
        deleted_row_emp_lastname = driver.find_element(by=By.XPATH, value=locators.Locators(
        ).pim_emp_list_emp_lastname).text

        print(
            f"{deleted_row_emp_id} {deleted_row_emp_firstname} {deleted_row_emp_lastname} is the employee in the actual first row")

        driver.find_element(
            by=By.XPATH, value=locators.Locators().pim_emp_list_delete_button).click()
        driver.find_element(by=By.XPATH, value=locators.Locators(
        ). pim_emp_list_delete_confirm_button).click()
        sleep(10)

        first_row_emp_id = driver.find_element(by=By.XPATH, value=locators.Locators(
        ). pim_emp_list_emp_id).text
        first_row_emp_firstname = driver.find_element(by=By.XPATH, value=locators.Locators(
        ).pim_emp_list_emp_firstname).text
        first_row_emp_lastname = driver.find_element(by=By.XPATH, value=locators.Locators(
        ).pim_emp_list_emp_lastname).text

        print(
            f"{first_row_emp_id} {first_row_emp_firstname} {first_row_emp_lastname} is the employee in the current first row")

        if deleted_row_emp_id != first_row_emp_id and deleted_row_emp_firstname != first_row_emp_firstname and deleted_row_emp_lastname != first_row_emp_lastname:
            print(
                f"{ deleted_row_emp_firstname} {deleted_row_emp_lastname} employee deleted-TEST PASSED")

        else:
            print(
                f"{ deleted_row_emp_firstname} {deleted_row_emp_lastname} employee not deleted-TEST FAILED")

        driver.quit()
