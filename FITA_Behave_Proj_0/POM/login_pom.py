from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utility.CommonMethods import CommonMethods

comm = CommonMethods

class LoginPOM:
    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def specification_tab(self, specification_tab):
        tab_locator = (By.XPATH, f'//*[@class="accordion-header"]//*[contains(normalize-space(text()), "{specification_tab}")]')
        tab_status = self.wait.until(EC.presence_of_element_located(tab_locator)).get_attribute("aria-expanded")
        return tab_locator, tab_status

    def expand_or_collapse_it(self, tab_status= "false", locator=None, element_to_ExpandOrCollapse= None):
        if  tab_status == "false":
            self.wait.until(EC.presence_of_element_located(locator)).click()
            print(f"{element_to_ExpandOrCollapse} expanded")
        else:
            print(f"{element_to_ExpandOrCollapse} collapsed")