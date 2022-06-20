from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    prod = (By.XPATH, "div/h4/a")
    prodName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    #addButton = (By.XPATH, "//div[@class='card h-100']/div/button")
    addButton = (By.XPATH, "div/button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutSubmit = (By.CSS_SELECTOR, "button[class*='btn-success']")






    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getprod(self):
        return self.driver.find_elements(*CheckoutPage.prod)

    def getprodName(self):
        return self.driver.find_element(*CheckoutPage.prodName)

    def getAddButton(self):
        return self.driver.find_element(*CheckoutPage.addButton)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getCheckoutSubmit(self):
        self.driver.find_element(*CheckoutPage.checkoutSubmit).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

