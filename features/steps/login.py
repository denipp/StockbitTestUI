import time

from behave import *
from web_source.Test import Test


class Catalog(Test):
    @given(u'User go to Login Page')
    def step_impl(context):
        try:
            context.web.click_change_number()
            context.web.click_back_register()
            context.web.login_from_register()
        except:
            context.web.screenshot()
            assert False

    @when(u'User in login page')
    def step_impl(context):
        try:
            context.web.verify_login_page()
        except:
            context.web.screenshot()
            assert False

    @then(u'Click Login')
    def step_impl(context):
        try:
            context.web.click_login_button()
        except:
            context.web.screenshot()
            assert False

    @when(u'Click Login')
    def step_impl(context):
        try:
            context.web.click_login_button()
        except:
            context.web.screenshot()
            assert False


    @then(u'Verify if user cannot login and get error message')
    def step_impl(context):
        try:
            context.web.verify_login_page()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user cannot login and get error message invalid')
    def step_impl(context):
        try:
            context.web.error_login_input()
        except:
            context.web.screenshot()
            assert False
    @given(u'User in login page')
    def step_impl(context):
        try:
            context.web.verify_login_page()
        except:
            context.web.screenshot()
            assert False

    @when(u'User input invalid username and password')
    def step_impl(context):
        try:
            context.web.input_login_username('den')
            context.web.input_login_password('den')
        except:
            context.web.screenshot()
            assert False

    @when(u'User click forgot password')
    def step_impl(context):
        try:
            context.web.click_forgot_password()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user in forgot password page')
    def step_impl(context):
        try:
            context.web.verify_in_forgot_password()
        except:
            context.web.screenshot()
            assert False

    @given(u'User in forgot password page')
    def step_impl(context):
        try:
            context.web.verify_in_forgot_password()
        except:
            context.web.screenshot()
            assert False

    @when(u'User input invalid email')
    def step_impl(context):
        try:
            context.web.input_1('denitest')
        except:
            context.web.screenshot()
            assert False

    @then(u'Click submit')
    def step_impl(context):
        try:
            context.web.submit_button()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user get error message in forgot password page')
    def step_impl(context):
        try:
            context.web.error_forgot_password()
        except:
            context.web.screenshot()
            assert False

    @when(u'User input valid email')
    def step_impl(context):
        try:
            context.web.input_1('denipratama@gmail.com')
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can success submit')
    def step_impl(context):
        try:
            context.web.verify_success_send_forgot()
        except:
            context.web.screenshot()
            assert False

    @given(u'User in success submit')
    def step_impl(context):
        try:
            context.web.verify_success_send_forgot()
        except:
            context.web.screenshot()
            assert False

    @when(u'Click Back to Login')
    def step_impl(context):
        try:
            context.web.back_to_login_page()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input valid username and password')
    def step_impl(context):
        try:
            context.web.input_login_username('denitesting123')
            context.web.input_login_password('rahasia')
        except:
            context.web.screenshot()
            assert False

    @when(u'Click Submit')
    def step_impl(context):
        try:
            context.web.click_login_button()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can login with valid data')
    def step_impl(context):
        try:
            context.web.verify_homepage()
        except:
            context.web.screenshot()
            assert False
