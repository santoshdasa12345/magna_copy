
from behave import *
from tests.smoke.steps import settings as env
from selenium import webdriver
import time


@given('upload logo')
def step_impl(context):
    context.driver = webdriver.Chrome(env.CHROME_DRIVER)
    context.driver.implicitly_wait(30)  # seconds
    context.execute_steps('''When User is navigating to Login Page''')
    context.execute_steps('''When User need to enter user name as {emailaddress} and password as {password}'''.format(
        emailaddress=env.LOGIN_USER_NAME, password=env.LOGIN_PASSWORD))
    context.execute_steps('''Then click on login button''')
    context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//a[@id='header-link-exporting-plan']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[@href='/export-plan/logo']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@id='id_logo']").send_keys('/Users/santoshdasari/Downloads/Logo-01.png')

    time.sleep(5)
    context.driver.find_element_by_xpath("//button[contains(text(),'Save and continue')]").click()
    time.sleep(2)