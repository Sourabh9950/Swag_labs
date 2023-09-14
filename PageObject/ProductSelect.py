from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Product_Select:

    Click_Bag_XPATH = (By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']")
    Click_AddCart_XPATH = (By.XPATH,"//button[@class='btn_primary btn_inventory']")
    Click_Back_XPATH = (By.XPATH,"//button[@class='inventory_details_back_button']")
    Click_Tshirt_XPATH = (By.XPATH,"//div[3]//div[3]//button[1]")
    Click_AddKart_XPATH = (By.XPATH,"//button[@class='btn_primary btn_inventory']")
    Click_Kart_XPATH =(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/a[1]/*[name()='svg'][1]/*[name()='path'][1]")
    Your_Cart_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]")

    def __init__(self,driver):
        self.driver = driver

    def click_bag(self):
        self.driver.find_element(*Product_Select.Click_Bag_XPATH).click()

    def click_addcart(self):
        self.driver.find_element(*Product_Select.Click_AddCart_XPATH).click()

    def click_back(self):
        self.driver.find_element(*Product_Select.Click_Back_XPATH).click()

    def click_tshirt(self):
        self.driver.find_element(*Product_Select.Click_Tshirt_XPATH).click()

    def click_addkart(self):
        self.driver.find_element(*Product_Select.Click_AddKart_XPATH).click()

    def click_kart(self):
        self.driver.find_element(*Product_Select.Click_Kart_XPATH).click()

    def Your_Cart(self):
        try:
            your_cart = self.driver.find_element(*Product_Select.Your_Cart_XPATH)
            return True
        except NoSuchElementException:
            return False





