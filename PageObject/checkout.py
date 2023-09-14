from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Checkout:
    Click_CheckOut_XPATH = (By.XPATH,"//a[@class='btn_action checkout_button']")
    Text_FirstName_XPATH = (By.XPATH,"//input[@id='first-name']")
    Text_LastName_XPATH = (By.XPATH,"//input[@id='last-name']")
    Text_Zip_XPATH = (By.XPATH,"//input[@id='postal-code']")
    Click_Continue_XPATH = (By.XPATH,"//input[@value='CONTINUE']")
    Click_Finish_XPATH = (By.XPATH, "//a[@class='btn_action cart_button']")
    Success_Message_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]")

    def __init__(self,driver):
        self.driver = driver

    def Checkout(self):
        self.driver.find_element(*Checkout.Click_CheckOut_XPATH).click()

    def Firstname(self, firstname):
        self.driver.find_element(*Checkout.Text_FirstName_XPATH).send_keys(firstname)

    def Lastname(self,lastname):
        self.driver.find_element(*Checkout.Text_LastName_XPATH).send_keys(lastname)

    def Zipcode(self,zipno):
        self.driver.find_element(*Checkout.Text_Zip_XPATH).send_keys(zipno)

    def Continue(self):
        self.driver.find_element(*Checkout.Click_Continue_XPATH).click()

    def Finish(self):
        self.driver.find_element(*Checkout.Click_Finish_XPATH).click()

    def Success_Message(self):
        try:
            success_message = self.driver.find_element(*Checkout.Success_Message_XPATH)
            return True
        except NoSuchElementException:
            return False

