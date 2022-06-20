import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("firstname is " +getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        #homepage.getPassword().send_keys(getData["password"])
        # creating an object and the locator the dropdown as a parameter (select class ca only be used if the tag of the drop down is select
        dropdown = Select(homepage.getdropdownlocator())
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)

        # selenium provides an pi select class -----> which provides the methods to handle the options in drop down
        homepage.getsubmitbutton().click()
        message = homepage.getsuccessMessage().text  # text method
        print(message)
        print(message)
        # //*[contains(@class, 'alert-success')] -------> xpath
        # [class*='alert-success'] ---------> CSS
        assert "success" in message  # for substring
        self.driver.refresh()


    @pytest.fixture(params = HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param