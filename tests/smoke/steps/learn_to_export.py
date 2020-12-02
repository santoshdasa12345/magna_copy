from behave import *
from tests.smoke.steps import settings as env
from selenium import webdriver
import time



@given('Lessons page')
def step_impl(context):
    context.driver = webdriver.Chrome(env.CHROME_DRIVER)
    context.driver.implicitly_wait(30)  # seconds
    context.execute_steps('''When User is navigating to Login Page''')
    context.execute_steps('''When User need to enter user name as {emailaddress} and password as {password}'''.format(
        emailaddress=env.LOGIN_USER_NAME, password=env.LOGIN_PASSWORD))
    context.execute_steps('''Then click on login button''')
    context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()

    context.driver.find_element_by_xpath("//a[@id='header-link-learning']").click()
    context.driver.fullscreen_window()
    context.driver.find_element_by_xpath("//h2[contains(text(),'Get started')]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[contains(text(),'Introduction to lessons and learning')]").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//label[contains(text(),'Yes')]").is_selected()
    time.sleep(5)
    context.driver.find_element_by_xpath("//button[contains(text(),'Continue learning')]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//body/main[@id='content']/div[1]/a[1]/i[1]").click()
    time.sleep(4)