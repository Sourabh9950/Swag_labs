import time

import allure
from allure_commons.types import AttachmentType

from PageObject.LoginPage import Swaglabs_login
from PageObject.checkout import Checkout
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig
from PageObject.ProductSelect import Product_Select

class Test_Product_select:
    username = Readconfig.GetUsername()
    password = Readconfig.GetPassword()


    log = LogGenerator.loggen()


    def test_checkout_004(self,setup):
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
        self.co = Checkout(self.driver)
        self.log.info("Clicking on checkout")
        self.co.Checkout()
        self.log.info("Entering Firstname")
        self.co.Firstname("Sourabh")
        self.log.info("Entering Lastname")
        self.co.Lastname("Jadhav")
        self.log.info("Entering Zipcode")
        self.co.Zipcode("123456")
        self.log.info("Clicking on Continue Button")
        self.co.Continue()
        self.log.info("Clicking on Finish Button")
        self.co.Finish()
        self.log.info("Checking Successful message")
        if self.co.Success_Message() == True:
            self.log.info("Taking screenshot for allure report")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_checkout_004_pass",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Testcase test_checkout_004 passed")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_checkout_004_fail",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Testcase test_checkout_004 faild")
            assert False
        self.log.info("Testcase test_checkout_004 Complited")








