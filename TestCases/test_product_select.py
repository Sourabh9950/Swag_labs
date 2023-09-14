import time

import allure
from allure_commons.types import AttachmentType

from PageObject.LoginPage import Swaglabs_login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig
from PageObject.ProductSelect import Product_Select

class Test_Product_select:
    username = Readconfig.GetUsername()
    password = Readconfig.GetPassword()


    log = LogGenerator.loggen()


    def test_product_select_003(self,setup):
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
        self.ps = Product_Select(self.driver)
        self.log.info("Clicking on bag option")
        self.ps.click_bag()
        self.log.info("Clicking on addcart menu")
        self.ps.click_addcart()
        self.log.info("Clicking on back option")
        self.ps.click_back()
        self.log.info("Clicking on Tshirt option")
        self.ps.click_tshirt()
        self.log.info("Clicking on addcart menu")
        self.ps.click_addkart()
        self.log.info("Clicking on cart menu")
        self.ps.click_kart()
        self.log.info("checking your message")
        if self.ps.Your_Cart() == True:
            self.log.info("Taking screenshot for allure report")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_product_select_003_pass",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Testcase test_product_select_003 passed")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_product_select_003_fail",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Testcase test_product_select_003 faild")
            assert False
        self.log.info("Testcase test_product_select_003 Complited")






#pytest -v -s -n=2 --html="C:\Users\LENOVO\PycharmProjects\pythonProject_swaglabs\HTML_Report" --alluredir="C:\Users\LENOVO\PycharmProjects\pythonProject_swaglabs\Allure_Report" --browser chrome