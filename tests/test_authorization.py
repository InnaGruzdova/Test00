#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_authorization.py

# from pages.basa import BasePage
#
# def test_visit(driver):
#     basa_page = BasePage(driver)
#     basa_page.visit()
#     # ozon_page.get_shops().click()
#     # time.sleep(5)
#     #assert basa_page.get_shops().is_displayed(), "WARRNING visbl"


#py -m pytest -v --driver Chrome --driver-path driver.exe
#python -m pytest -v --driver Chrome --driver-path C:\Skillfactory\Drivers/chromedriver.exe

import time
from pages.auth_page import AuthPage
from config import valid_email, valid_password, valid_pone, login_no_valid, ls_no_valid ,pass_gener, email_gener
# from script import  pass_gener, email_gener
from pages.elements import WebElement
#from pages.register_page import MainPage
# from pages.auth_page_code import AuthPageWithCode
# from config import TestData

def test_main_page_all_items(web_browser):
    """Проверка главной страницы"""
    page = AuthPage(web_browser)
    assert page.text_authorization.is_visible()
    assert page.text_personal_area.is_visible()
    assert page.email_input_form.is_visible()
    assert page.password_input_form.is_visible()
    assert page.tab_phone.is_visible()
    assert page.tab_email.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_ls.is_visible()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()

def test_positive_authorisation_phone(web_browser):
    """Авторизация по номеру телефона и паролю"""
    page = AuthPage(web_browser)
    page.tab_phone.click()
    page.email_input_form.send_keys(valid_pone)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click() #Снимаем галочку с поля запомнить меня
    page.btn.click()
    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_positive_authorisation_email(web_browser):
    """Авторизация по email и паролю"""
    page = AuthPage(web_browser)
    page.tab_email.click()
    page.email_input_form.send_keys(valid_email)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

def test_negative_authorization_login(web_browser):
    """Не удачная авторизация по логину и паролю"""
    page = AuthPage(web_browser)
    page.tab_login.click()
    page.email_input_form.send_keys(login_no_valid)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()

def test_negative_authorization_ls(web_browser):
    """Не удачная авторизация по лицевому счету и паролю"""
    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.email_input_form.send_keys(ls_no_valid)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()

def test_negative_authorisation_email(web_browser):
    """Не удачная авторизация по email и паролю"""
    page = AuthPage(web_browser)
    page.tab_email.click()

    if page.captcha_text.is_visible():
        assert page.captcha_text.is_visible()
    else:
        for i in range(5):
        # asdf = True#'https://b2c.passport.rt.ru/' in page.get_current_url() or page.invalid_login_password.is_visible()
        # while asdf:
            page.email_input_form.send_keys(email_gener())
            if page.captcha_text.is_visible():
                break
            page.password_input_form.send_keys(pass_gener())
            if page.captcha_text.is_visible():
                break
            page.check_mark.click()
            if page.captcha_text.is_visible():
                break
            page.btn.click()
            if page.captcha_text.is_visible():
                break
        # assert page.captcha.is_visible()
        # assert page.forgot_password.is_visible()
        # assert page.invalid_login_password.is_visible()
            # else:
            #     #page.captcha.is_visible()
            #     assert page.captcha.is_visible()
        # page.email_input_form.element.clear()
        # page.password_input_form.element.clear()

    # print(pass_gener())
    # print(email_gener())

# def test_positive_authorisation_email(web_browser):
#     """Не удачная авторизация по email и паролю"""
#     page = AuthPage(web_browser)
#     page.tab_email.click()
#     page.email_input_form.send_keys(e_mail)
#     page.password_input_form.send_keys(passw)
#     page.check_mark.click()
#     page.btn.click()
#     assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


        #page.btn.click()
    #
    #     page.check_mark.click()
    #     page.btn.click()
    #     print(pass_gener())
    #     print(email_gener())
    # page.email_input_form.send_keys(e_mail)
    # page.password_input_form.send_keys(passw)
    # page.check_mark.click()
    # page.btn.click()
    # assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

    # assert Color.page.forgot_password == 'orange'
    # assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

    time.sleep(5)
    # page.forgot_password_btn.click()
    #
    # assert page.email.is_presented()
    # assert page.captcha.is_presented()
    # assert page.captcha_input.is_presented()
    # assert page.btn_continue.is_presented()









# import time
# import pytest
# from pages.auth_page import AuthPage
# from pages.register_page import MainPage
# from pages.auth_page_with_code import AuthPageWithCode
# from config import TestData
#
# def test_main_page_all_items(web_browser):
#     page = AuthPage(web_browser)
#
#     assert page.email.is_visible()
#     assert page.password.is_visible()
#     assert page.btn.is_visible()
#     assert page.registration_btn.is_visible()
#     assert page.forgot_password_btn.is_visible()
#     assert page.tab_email.is_visible()
#     assert page.tab_login.is_visible()
#     assert page.tab_phone.is_visible()
#     assert page.tab_ls.is_visible()