import time

from PageObject.LoginPage import Swaglabs_login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig

class Test_Login:
    username = Readconfig.GetUsername()
    password = Readconfig.GetPassword()


    log = LogGenerator.loggen()

    def test_page_title_001(self,setup):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.log.info("Page title is"+ self.driver.title)
        if self.driver.title == "Swag Labs":
            time.sleep(1)
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject_swaglabs\\ScreenShots"
                                        "\\test_page_title_001_pass.png")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject_swaglabs\\ScreenShots"
                                        "\\test_page_title_001_fail.png")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is failed")
            assert False
        self.log.info("Testcase test_page_title_001 is comleted")


    def test_login_002(self,setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = Swaglabs_login(self.driver)
        self.log.info("Entering username:" + self.username)
        self.lp.Enter_Username(self.username)
        self.log.info("Entering password:" + self.password)
        self.lp.Enter_Password(self.password)
        self.log.info("Clicking on login button")
        self.lp.Click_login()
        self.log.info("Checking login status")
        if self.lp.Login_Status() == True:
            self.log.info("Taking screenshot")

            time.sleep(1)
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject_swaglabs\\ScreenShots"
                                        "\\test_login_002_pass.png")
            time.sleep(1)
            self.log.info("Clicking on menu button")

            self.lp.Click_Menu()

            self.log.info("Clicking on logout button")

            self.lp.Click_Logout()
            self.log.info("Testcase test_login_002 is passed")

            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject_swaglabs\\ScreenShots"
                                        "\\test_login_002_fail.png")
            self.driver.close()
            self.log.info("Testcase test_login_002 is failed")
            assert False
        self.log.info("Testcase test_login_002 is completed")


