import time
import datetime
from selenium.webdriver.common.by import By
from web_source.web import Web
from selenium.webdriver.common.keys import Keys
import allure


class Test(Web):

    WEB = "https://stockbit.com/"

    CLICK_REGISTER = (By.CSS_SELECTOR, ".button:nth-child(2) > .register-lnd")
    CLICK_LOGIN = (By.CSS_SELECTOR, 'css=.button:nth-child(1) > .login-ldn')
    VERIFY_REGISTER = (By.XPATH, '//a[contains(text(),"Register with Email")]')
    REGIS_WITH_EMAIL = (By.LINK_TEXT, "Register with Email")
    VERIFY_REGISTER_FORM = (By.XPATH, "//input[contains(@value,'Register')]")
    INPUT_PHONE_NUMBER_VERIF = (By.CSS_SELECTOR, ".form-control")
    SUBMIT = (By.CSS_SELECTOR, ".loginlogin")
    VERIF_SMS_PAGE = (By.XPATH, '//div[contains(text(),"SMS Verification")]')
    CHANGE_PHONE = (By.LINK_TEXT, "Change Phone Number")
    VERIF_VERIFICATION = (By.XPATH, '//div[contains(text(),"Verification Code")]')
    INPUT_1 = (By.ID, "input-1")
    INPUT_2 = (By.ID, "input-2")
    INPUT_3 = (By.ID, "input-3")
    INPUT_4 = (By.ID, "input-4")
    INPUT_5 = (By.ID, "input-5")
    VERIFY_CODE_NUMBER = (By.XPATH, '//div[contains(text(),"A verification code has been sent to your phone")]')
    BACK_TO_REGISTER = (By.CSS_SELECTOR, ".login-note > img")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".errorfield > .errormsg")
    ERROR_CODE = (By.XPATH, '//div[contains(text(),"verifikasi kamu salah")]')

    VERIFY_INPUT_NAME = (By.XPATH, '(//i[@class="icon-toolbar_check"])[1]')
    VERIFY_INPUT_EMAIL = (By.XPATH, '(//i[@class="icon-toolbar_check"])[2]')
    VERIFY_INPUT_USERNAME = (By.XPATH, '(//i[@class="icon-toolbar_check"])[3]')


    CLICK_LOGIN = (By.XPATH, '//a[contains(text(),"Login")]')
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginbutton")
    ERROR_LOGIN_PAGE_INPUT = (By.XPATH, '//div[contains(text(),"Username atau password salah")]')
    CLICK_FORGOT_PASSWORD = (By.LINK_TEXT, "Click here")
    FORGOT_PASSWORD_PAGE = (By.XPATH, '//div[contains(text(),"Forgot Password")]')
    ERROR_MESSAGE_FORGOT_PASSWORD = (By.XPATH, '//div[contains(text(),"Format email salah")]')
    ERROR_MESSAGE_INVALID_PHONE = (By.XPATH, '//div[contains(text(),"Gagal mengirim")]')
    BACK_TO_LOGIN = (By.LINK_TEXT, "I didn\'t receive the email")
    BACK_TO_LOGIN_PAGE = (By.LINK_TEXT, "Back to Login Page")
    SUCCESS_SEND_FORGOT_PASSWORD = (By.XPATH, '//div[contains(text(),"Check Your Email")]')
    VERIFY_HOMEPAGE = (By.XPATH, '//A[contains(text(),"Berlangganan Pro")]')



    def __init__(self, driver):
        super(Web, self).__init__()
        self.driver = driver
    def open_browser(self):
        self.open(self.WEB)
    def click_register(self):
        self.do_click(self.CLICK_REGISTER)
    def click_login(self):
        self.do_click(self.CLICK_LOGIN)
    def verify_register(self):
        self.is_visible(self.VERIFY_REGISTER)
    def register_with_email(self):
        self.do_click(self.REGIS_WITH_EMAIL)
    def verify_register_form(self):
        self.is_visible(self.VERIFY_REGISTER_FORM)
    def submit_button(self):
        self.do_click(self.SUBMIT)
    def input_1(self, data):
        self.do_send_keys(self.INPUT_1, Keys.CONTROL + 'a')
        self.do_send_keys(self.INPUT_1, data)
    def input_2(self, data):
        self.do_send_keys(self.INPUT_2, Keys.CONTROL + 'a')
        self.do_send_keys(self.INPUT_2, data)
    def input_3(self, data):
        self.do_send_keys(self.INPUT_3, Keys.CONTROL + 'a')
        self.do_send_keys(self.INPUT_3, data)
    def input_4(self, data):
        self.do_send_keys(self.INPUT_4, Keys.CONTROL + 'a')
        self.do_send_keys(self.INPUT_4, data)
    def input_5(self, data):
        self.do_send_keys(self.INPUT_5, Keys.CONTROL + 'a')
        self.do_send_keys(self.INPUT_5, data)
    def verify_input_name(self):
        time.sleep(1)
        self.is_visible(self.VERIFY_INPUT_NAME)
    def verify_input_username(self):
        time.sleep(1)
        self.is_visible(self.VERIFY_INPUT_USERNAME)
    def verif_invalid_format_email(self):
        time.sleep(1)
        invalid_email = self.get_element_text(self.ERROR_MESSAGE)
        assert 'Format email salah' in invalid_email
    def verif_available_email(self):
        time.sleep(1)
        available = self.get_element_text(self.ERROR_MESSAGE)
        assert 'Email sudah terdaftar' in available
    def verify_input_email(self):
        time.sleep(1)
        self.is_visible(self.VERIFY_INPUT_EMAIL)
    def verify_username(self):
        time.sleep(1)
        low_character = self.get_element_text(self.ERROR_MESSAGE)
        assert 'minimal 4 karakter' in low_character
    def verify_available_username(self):
        time.sleep(1)
        avail_username = self.get_element_text(self.ERROR_MESSAGE)
        assert 'username tidak tersedia' in avail_username
    def verify_confirm_password(self):
        time.sleep(1)
        confirm = self.get_element_text(self.ERROR_MESSAGE)
        assert 'Password does not match' in confirm
    def verify_sms_verification_page(self):
        time.sleep(1)
        self.is_visible(self.VERIF_SMS_PAGE)
    def input_phone_number(self, data):
        self.do_send_keys(self.INPUT_PHONE_NUMBER_VERIF, data)
    def error_phone_number(self):
        time.sleep(1)
        self.is_visible(self.ERROR_MESSAGE_INVALID_PHONE)
    def verify_success_submit_phone(self):
        time.sleep(1)
        self.is_visible(self.VERIFY_CODE_NUMBER)
    def verif_verification_page(self):
        time.sleep(1)
        self.is_visible(self.VERIF_VERIFICATION)
    def get_error_code_verification(self):
        time.sleep(1)
        self.is_visible(self.ERROR_CODE)
    def click_change_number(self):
        self.do_click(self.CHANGE_PHONE)
    def click_back_register(self):
        self.do_click(self.BACK_TO_REGISTER)
    def login_from_register(self):
        self.do_click(self.CLICK_LOGIN)
    def input_login_username(self, data):
        self.do_send_keys(self.LOGIN_USERNAME, Keys.CONTROL + 'a')
        self.do_send_keys(self.LOGIN_USERNAME, data)
    def input_login_password(self, data):
        self.do_send_keys(self.LOGIN_PASSWORD, Keys.CONTROL + 'a')
        self.do_send_keys(self.LOGIN_PASSWORD, data)
    def click_login_button(self):
        self.do_click(self.LOGIN_BUTTON)
    def verify_login_page(self):
        time.sleep(1)
        self.is_visible(self.LOGIN_BUTTON)
    def error_login_input(self):
        time.sleep(1)
        self.is_visible(self.ERROR_LOGIN_PAGE_INPUT)

    def click_forgot_password(self):
        self.do_click(self.CLICK_FORGOT_PASSWORD)
    def verify_in_forgot_password(self):
        time.sleep(1)
        self.is_visible(self.FORGOT_PASSWORD_PAGE)
    def error_forgot_password(self):
        time.sleep(1)
        self.is_visible(self.ERROR_MESSAGE_FORGOT_PASSWORD)
    def verify_success_send_forgot(self):
        time.sleep(1)
        self.is_visible(self.SUCCESS_SEND_FORGOT_PASSWORD)
    def back_to_login_page(self):
        self.do_click(self.BACK_TO_LOGIN)
        self.do_click(self.BACK_TO_LOGIN_PAGE)
    def verify_homepage(self):
        time.sleep(1)
        self.is_visible(self.VERIFY_HOMEPAGE)






















    def screenshot(self):
        now = str(datetime.datetime.now())
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Fail - " + now, attachment_type=allure.attachment_type.PNG
        )

