from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "country")
    locationSuggestion = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    orderSubmit = (By.CSS_SELECTOR, "[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")


    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.location)
    def getlocationSuggestion(self):
        return self.driver.find_element(*ConfirmPage.locationSuggestion)
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)
    def getOrderSubmit(self):
        return self.driver.find_element(*ConfirmPage.orderSubmit)
    def getsuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
