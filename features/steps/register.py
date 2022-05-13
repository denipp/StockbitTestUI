import time

from behave import *
from web_source.Test import Test
import random



class Catalog(Test):
    @given(u'Open Stockbit')
    def step_impl(context):
        try:
            context.web.open_browser()
        except:
            context.web.screenshot()
            assert False


    @when(u'Click Register page')
    def step_impl(context):
        try:
            context.web.click_register()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if users can redirect to register page')
    def step_impl(context):
        try:
            context.web.verify_register()
        except:
            context.web.screenshot()
            assert False

    @given(u'Users in register page')
    def step_impl(context):
        try:
            context.web.verify_register()
        except:
            context.web.screenshot()
            assert False

    @when(u'Users click register with email')
    def step_impl(context):
        try:
            context.web.register_with_email()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify user can click register with email')
    def step_impl(context):
        try:
            context.web.verify_register_form()
        except:
            context.web.screenshot()
            assert False

    @given(u'User in Register form')
    def step_impl(context):
        try:
            context.web.verify_register_form()
        except:
            context.web.screenshot()
            assert False

    @when(u'Click Register')
    def step_impl(context):
        try:
            context.web.submit_button()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify user cant register and get error message')
    def step_impl(context):
        try:
            context.web.verify_register_form()
        except:
            context.web.screenshot()
            assert False

    @when(u'input name')
    def step_impl(context):
        try:
            context.web.input_1('Deni Testing')
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can input name')
    def step_impl(context):
        try:
            context.web.verify_input_name()
        except:
            context.web.screenshot()
            assert False

    @when(u'input invalid email')
    def step_impl(context):
        try:

            context.web.input_2('Deni')
        except:
            context.web.screenshot()
            assert False

    @when(u'input available email')
    def step_impl(context):
        try:

            context.web.input_2('deni@gmail.com')
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can see error message email available')
    def step_impl(context):
        try:
            context.web.verif_available_email()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can see error message email')
    def step_impl(context):
        try:
            context.web.verif_invalid_format_email()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input valid email')
    def step_impl(context):
        try:
            n = random.randint(0, 10000)
            context.web.input_2('denitesting'+str(n)+'@gmail.com')
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can input email')
    def step_impl(context):
        try:
            context.web.verify_input_email()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input username with 2 character')
    def step_impl(context):
        try:
            context.web.input_3('de')
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can see error message username 3 character')
    def step_impl(context):
        try:
            context.web.verify_username()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can see error message username not available')
    def step_impl(context):
        try:
            context.web.verify_available_username()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input username that is used')
    def step_impl(context):
        try:
            context.web.input_3('deni')
        except:
            context.web.screenshot()
            assert False

    @when(u'Input username available')
    def step_impl(context):
        try:
            n = random.randint(0, 10000)
            context.web.input_3('denitest'+str(n))
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can input username')
    def step_impl(context):
        try:
            context.web.verify_input_username()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input correct password')
    def step_impl(context):
        try:
            context.web.input_4('rahasia')
        except:
            context.web.screenshot()
            assert False

    @when(u'Input incorrect confirm password')
    def step_impl(context):
        try:
            context.web.input_5('lolololo')
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can see error message password')
    def step_impl(context):
        try:
            context.web.verify_confirm_password()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input correct confirm password')
    def step_impl(context):
        try:
            context.web.input_5('rahasia')
            time.sleep(2)
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can register')
    def step_impl(context):
        try:
            context.web.submit_button()
            context.web.verify_sms_verification_page()
        except:
            context.web.screenshot()
            assert False

    @given(u'User in Phone Verification page')
    def step_impl(context):
        try:
            context.web.verify_sms_verification_page()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input invalid phone number format')
    def step_impl(context):
        try:
            context.web.input_phone_number('85747')
            context.web.submit_button()
        except:
            context.web.screenshot()
            assert False

    @then(u'Verify if user can see error message invalid phone number format')
    def step_impl(context):
        try:
            context.web.error_phone_number()
        except:
            context.web.screenshot()
            assert False

    @when(u'Input valid phone number')
    def step_impl(context):
        n = random.randint(0, 1000000)
        try:
            context.web.input_phone_number(str(n))
            context.web.submit_button()
        except:
            context.web.screenshot()
            assert False

    @then(u'verify if user can send phone verification')
    def step_impl(context):
        try:
            context.web.verify_success_submit_phone()
            context.web.submit_button()
        except:
            context.web.screenshot()
            assert False

    @given(u'User in Verification code')
    def step_impl(context):
        try:
            context.web.verif_verification_page()
        except:
            context.web.screenshot()
            assert False

    @when(u'User input invalid code')
    def step_impl(context):
        try:
            context.web.input_1('2')
            context.web.input_2('1')
            context.web.input_3('1')
            context.web.input_4('1')
        except:
            context.web.screenshot()
            assert False

    @then(u'verify if user can see error message verification code')
    def step_impl(context):
        try:
            context.web.submit_button()
            context.web.get_error_code_verification()
        except:
            context.web.screenshot()
            assert False

