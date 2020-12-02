from behave import *
from tests.smoke.steps import settings as env
from selenium import webdriver


@given('User is on home page after login')
def step_impl(context):
    context.driver = webdriver.Chrome(env.CHROME_DRIVER)
    context.driver.implicitly_wait(30)  # seconds
    context.execute_steps('''When User is navigating to Login Page''')
    context.execute_steps('''When User need to enter user name as {emailaddress} and password as {password}'''.format(
        emailaddress=env.LOGIN_USER_NAME, password=env.LOGIN_PASSWORD))
    context.execute_steps('''Then click on login button''')
    context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()


@when('User navigates to Avatar and click on sign out')
def step_impl(context):
    context.driver.find_element_by_xpath("//header/nav[1]/div[1]/ul[1]/li[4]/div[1]/button[1]").click()
    context.driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/ul[1]/li[6]/button[1]").click()


@then('User should navigate to login page')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "//button[@id='signup-modal-submit']").is_displayed()