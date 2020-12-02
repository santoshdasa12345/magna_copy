from behave import *

from tests.smoke.steps import settings as env
from selenium import webdriver
import time


@given('User is on home page')
def step_impl(context):
    context.driver = webdriver.Chrome(env.CHROME_DRIVER)
    context.driver.implicitly_wait(30)  # seconds
    context.execute_steps('''When User is navigating to Login Page''')
    context.execute_steps('''When User need to enter user name as {emailaddress} and password as {password}'''.format(
        emailaddress=env.LOGIN_USER_NAME, password=env.LOGIN_PASSWORD))
    context.execute_steps('''Then click on login button''')
    context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()


@when('User searches for product to export {products}')
def step_impl(context, products):
    context.driver.find_element_by_xpath(
        "//body/nav[@id='personalisation-bar']/span[@id='set-product-button']/span[1]/button[1]").click()
    if context.driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
        context.driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    context.driver.find_element_by_xpath(
        "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys(products)
    context.driver.find_element_by_xpath("//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/button[1]/i[1]").click()
    if "Vehicle" in products:

        context.driver.find_element_by_xpath("//input[@data-label='road vehicle']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
        #
        context.driver.find_element_by_xpath("//input[@data-label='motorcycle']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        context.driver.find_element_by_xpath("//input[@data-label='internal combustion engine']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        context.driver.find_element_by_xpath("//input[@data-label='> 50 and <= 250 cc']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
        time.sleep(1)  # seconds
        context.driver.find_element_by_xpath("//button[contains(text(),'Select this product')]").click()
        time.sleep(1)  # seconds
        context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()

        # next
    if "Leather" in products:

        context.driver.find_element_by_xpath("//input[@data-label='pretanned']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        context.driver.find_element_by_xpath("//input[@data-label='reversible']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        context.driver.find_element_by_xpath("//input[@data-label='sheep']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        context.driver.find_element_by_xpath("//input[@data-label='pickled']").click()
        context.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
        time.sleep(1)  # seconds
        context.driver.find_element_by_xpath("//button[contains(text(),'Select this product')]").click()
        time.sleep(1)  # seconds
        context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()

    context.driver.find_element_by_xpath("//body/nav[@id='personalisation-bar']/span[@id='set-country-button']/span[1]/button[1]").click()
    time.sleep(1)  # seconds

@then("User searches for country to sell in {country} for already selected {products}")
def step_impl(context, country, products):
    if "Vehicle" in products and "Germany" in country:
        if context.driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
            context.driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()

        path_germany_element = "//body/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/button[" + str(3) + "]"
        context.driver.find_element_by_xpath(path_germany_element).click()
        time.sleep(1)  # seconds
        context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()

    if "Leather" in products and "Poland" in country:
        if context.driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
            context.driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()

        context.driver.find_element_by_xpath("//body/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(country)
        context.driver.find_element_by_xpath("//button[contains(text(),'Poland')]").click()
        context.driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()
