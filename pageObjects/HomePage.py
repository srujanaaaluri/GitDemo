from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.LINK_TEXT, "Shop")  #(this is a tuple)
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@placeholder='Password']")
    dropdownlocator = (By.ID, "exampleFormControlSelect1")
    submitbutton = (By.CSS_SELECTOR, "input[value='Submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
         self.driver.find_element(*HomePage.shop).click()
         checkoutPage = CheckoutPage(self.driver)
         return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getdropdownlocator(self):
        return self.driver.find_element(*HomePage.dropdownlocator)
    def getsubmitbutton(self):
        return self.driver.find_element(*HomePage.submitbutton)

    def getsuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

         #homepage.shop ---> since it is a class variable (otherwise--> self.shop)
         #since shop is a tuple it wraps entire element like "driver.find_element(By.LINK_TEXT, "Shop"" (by putting, * shop is treated like a tuple)


