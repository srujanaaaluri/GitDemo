from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver) # creating object homepage for class homepage ( we are sending this actual driver to homepage)
        checkoutPage = homepage.shopItems()
        log.info("getting all card titles")
        products = checkoutPage.getCardTitles()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        checkoutPage.getCheckoutButton().click()
        confirmPage = checkoutPage.getCheckoutSubmit()
        log.info("entering country name as ind")
        confirmPage.getLocation().send_keys("Ind")
        self.verifylinkpresence("India")
        confirmPage.getlocationSuggestion().click()
        confirmPage.getCheckBox().click()
        confirmPage.getOrderSubmit().click()
        successText = confirmPage.getsuccessMessage().text
        assert "Success! Thank you!" in successText

