from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Swaglabs_login:

    Text_Username_Name = (By.NAME, "user-name")
    Text_Password_Name = (By.NAME, "password")
    Click_login_ID = (By.ID, "login-button")
    Click_Menu_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]")
    Click_Logout_XPATH = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self,driver):
        self.driver = driver
        #self.wait = WebDriverWait(self.driver,10,poll_frequency=0.2)


    def Enter_Username(self, username):
        self.driver.find_element(*Swaglabs_login.Text_Username_Name).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*Swaglabs_login.Text_Password_Name).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*Swaglabs_login.Click_login_ID).click()

    def Click_Menu(self):
        self.driver.find_element(*Swaglabs_login.Click_Menu_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*Swaglabs_login.Click_Logout_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*Swaglabs_login.Click_Menu_XPATH)
            return True
        except:
            return False




