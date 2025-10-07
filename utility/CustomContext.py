from selenium.webdriver.remote.webdriver import WebDriver
from POM.login_pom import LoginPOM
from utility.CommonMethods import CommonMethods
from utility.read_excel import Excel


class CustomContext:
        driver : WebDriver
        comm : CommonMethods
        login : LoginPOM
        excel : Excel
