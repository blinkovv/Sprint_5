import pytest
import time
from conftest import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators
import configuration


class TestInvalidPassword:
    def test_invalid_password(self, driver):   # Невалидный пароль, ошибка
        driver.get(configuration.URL_REGISTRATION)

        driver.find_element(By.XPATH, locators.input_name).send_keys("ИванАбрамов")
        driver.find_element(By.XPATH, locators.input_email).send_keys("123@ya.ru")
        driver.find_element(By.XPATH, locators.input_password).send_keys("12")
        driver.find_element(By.XPATH, locators.button_register).click()
        error_message = driver.find_element(By.XPATH, locators.error_password).text
        assert "Некорректный пароль" in error_message

class TestSuccessfulRegistration:
    def test_successful_registration(self, driver):    # Регистрация на сайте
        driver.get(configuration.URL_REGISTRATION)

        driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.generate_name())
        driver.find_element(By.XPATH, locators.input_email).send_keys(configuration.generate_email())
        driver.find_element(By.XPATH, locators.input_password).send_keys(configuration.generate_password())
        driver.find_element(By.XPATH, locators.button_register).click()
        assert "Вход" in driver.find_element(By.XPATH, locators.text_entrance_on_the_login_page).text

class TestLoginThroughDifferentButtons:
    def test_login_through_main_page(self, driver):
        driver.get(configuration.URL)  # Вход через главную страницу "Войти"

        driver.find_element(By.XPATH, locators.button_login).click()
        driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
        driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
        driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
        assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text

    def test_login_through_personal_account(self, driver):
        driver.get(configuration.URL)  # Вход через главную страницу "Личный кабинет"

        driver.find_element(By.XPATH, locators.button_personal_account).click()
        driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
        driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
        driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
        assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text

    def test_login_through_register_form(self, driver):
        driver.get(configuration.URL_REGISTRATION)  # Вход через кнопку в форме регистрации

        driver.find_element(By.XPATH, locators.button_login_from_register).click()
        driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
        driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
        driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
        assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text

class TestLoginThroughPasswordRecovery:
    def test_login_through_password_recovery_form(self, driver):
        driver.get(configuration.URL_LOGIN)  # Вход через кнопку в форме регистрации
        driver.find_element(By.XPATH, locators.button_reset_password).click()
        driver.find_element(By.XPATH, locators.button_login_from_register).click()
        driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
        driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
        driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
        assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text

class TestPersonalAccountAndConstructor:
    def test_personal_account_and_constructor(self, driver):
        driver.get(configuration.URL)
        driver.find_element(By.XPATH, locators.button_personal_account).click()  # Переход в ЛК
        driver.find_element(By.XPATH, locators.button_constructor).click()  # Переход из ЛК в Конструктор
        driver.find_element(By.XPATH, locators.button_personal_account).click()  # Переход в ЛК
        driver.find_element(By.CSS_SELECTOR, locators.button_logotype).click()  # Переход по клику на логотип Stellar Burgers.
        assert 'Соберите бургер' in driver.find_element(By.XPATH, locators.text_assemble_burger_main_page).text

class TestLogout:
    def test_logout(self, driver):
        driver.get(configuration.URL)

        driver.find_element(By.XPATH, locators.button_login).click()
        driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
        driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
        driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
        driver.find_element(By.XPATH, locators.button_personal_account).click()
        driver.find_element(By.XPATH, locators.button_log_out).click()
        successful_registrations = driver.find_element(By.XPATH, locators.text_entrance_on_the_login_page).text
        assert "Вход" in successful_registrations

class TestConstructorNavigation:
    def test_constructor_navigation_sauces(self, driver):
        driver.get(configuration.URL)
        driver.find_element(By.XPATH, locators.link_sauces).click()
        assert 'Соусы' in driver.find_element(By.XPATH, locators.text_sauces).text

    def test_constructor_navigation_buns(self, driver):
        driver.get(configuration.URL)
        driver.find_element(By.XPATH, locators.link_buns).click()
        assert 'Булки' in driver.find_element(By.XPATH, locators.text_buns).text

    def test_constructor_navigation_fillings(self, driver):
        driver.get(configuration.URL)
        driver.find_element(By.XPATH, locators.link_fillings).click()
        assert "Начинки" in driver.find_element(By.XPATH, locators.text_fillings).text