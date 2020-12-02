from behave import *

from helpers.read_email import ReadEmail
from tests.smoke.steps import settings as env
from selenium import webdriver
import time


@given('User is navigated to Login Page')
def step_impl(context):
    context.driver = webdriver.Chrome(env.CHROME_DRIVER)
    context.driver.implicitly_wait(20)  # seconds
    context.driver.get(env.DOMAIN_URL + "/login/")
    context.driver.fullscreen_window()
    time.sleep(2)


@when('User clicks on forgotten password')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Forgotten password?')]").click()
    time.sleep(5)


@when('User enters "emailaddress" to reset password')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@class='_2Je4saUrXDlps2OeB9xZFT button']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@id='id_email']").send_keys(env.LOGIN_USER_NAME)
    time.sleep(5)
    context.driver.find_element_by_xpath("//button[contains(text(), 'Reset my password')]").click()
    time.sleep(5)


@then('User receives an email with reset password link')
def step_impl(context):
    time.sleep(5)
    # create and load the confirmation code email from the test user
    objreadmail = ReadEmail(env.DEV_GMAIL_HOST, env.LOGIN_USER_NAME, env.GMAIL_LOGIN_PASSWORD, env.EMAIL_FETCH_COUNT)
    # search the test user INBOX, read the email body text from the Reset password email
    email_search_criteria = "Reset your password at "
    email_body_text = objreadmail.reademailbody("Reset your great.gov.uk password", email_search_criteria)
    print(email_body_text)

    # check if the email_body_text exists or empty
    if email_body_text:
        # search text position in email_body_text
        reset_link_pos = email_body_text.find(email_search_criteria)

        # check if the required search criteria text found in the email_body_text. -1 indicates not found.
        if reset_link_pos != -1:
            reset_link_text = email_body_text[reset_link_pos + len(email_search_criteria):]
            reset_link_text = reset_link_text.strip()  # trim left and right

            reset_link_end_pos = reset_link_text.find("/about/")
            if reset_link_end_pos != -1:
                reset_link_text = reset_link_text[:reset_link_end_pos+ len("/about/")]
                reset_link_text = reset_link_text.strip()  # trim left and right
                print(reset_link_text)
                context.driver.get(reset_link_text)
                if context.driver.find_element_by_xpath("//h1[contains(text(),'Change Password')]").is_displayed():
                    context.driver.find_element_by_xpath("//input[@id='id_password1']").send_keys("newpassword")
                    context.driver.find_element_by_xpath("//input[@id='id_password2']").send_keys("newpassword")
                    context.driver.find_element_by_xpath("//button[contains(text(),'change password')]").click()