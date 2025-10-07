import os
from datetime import datetime

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import utility.Global_Variable as gv
from POM.login_pom import LoginPOM
from utility.read_excel import Excel
from utility.CommonMethods import CommonMethods

SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

#def before_all(context):
def before_scenario(context, scenario):
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('start-maximized')
    context.driver = Chrome(options=options)
    context.driver.get(gv.BASE_URL)

    context.excel = Excel(context.driver)
    context.comm = CommonMethods(context.driver)
    context.login = LoginPOM(context.driver)

def after_step(context, step):
    if step.status == "failed":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{step.name}_{timestamp}.png".replace(" ", "_")
        file_path = os.path.join(SCREENSHOT_DIR, file_name)

        # Save screenshot
        context.driver.save_screenshot(file_path)
        print(f"Screenshot saved to: {file_path}")

        # Attach to HTML behave report (if using behave-html-formatter)
        if "behave_html_formatter" in context.config.reporters:
            context.config.reporters["behave_html_formatter"].embed(file_path, "image/png", "Screenshot")

#def after_all(context):
def after_scenario(context, scenario):
    context.driver.quit()

