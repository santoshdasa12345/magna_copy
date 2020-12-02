from behave import *
from tests.smoke.steps import settings as env
from selenium import webdriver
import time



@given('Page tour to all the pages')
def step_impl(context):
    context.driver = webdriver.Chrome(env.CHROME_DRIVER)
    context.driver.implicitly_wait(30)  # seconds
    context.execute_steps('''When User is navigating to Login Page''')
    context.execute_steps('''When User need to enter user name as {emailaddress} and password as {password}'''.format(
        emailaddress=env.LOGIN_USER_NAME, password=env.LOGIN_PASSWORD))
    context.execute_steps('''Then click on login button''')
    #context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()
    time.sleep(5)

    context.driver.find_element_by_xpath("//button[@id='page-tour-submit']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@id='page-tour-next-step']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@id='page-tour-next-step']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@id='page-tour-next-step']").click()
    time.sleep(2)
