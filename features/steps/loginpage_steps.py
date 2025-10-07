from behave import given, when, then, parser
from utility.CustomContext import CustomContext


@given('User inside Automation Practise website')
def step_impl(context):
    assert "Selenium Practice" in context.driver.title, f"Expected {context.driver.title}"

@when('User expands the {tab_specification} tab')
def step_impl(context : CustomContext, tab_specification):
    tab_locator, tab_status = context.login.specification_tab(tab_specification)
    context.login.expand_or_collapse_it(tab_status = tab_status, locator=tab_locator, element_to_ExpandOrCollapse = tab_specification)


@then('User clicks on {components} and executes cases in {testcase}')
def step_impl(context : CustomContext, testcase : str, components):
    print(f"{components} cases Verification in progress...")
    context.excel.read_my_excel(testcase)

