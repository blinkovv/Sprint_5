import pytest
import time
from conftest import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators
import configuration


def test_invalid_password(driver):   # Невалидный пароль, ошибка
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, locators.input_name).send_keys("ИванАбрамов")
    driver.find_element(By.XPATH, locators.input_email).send_keys("123@ya.ru")
    driver.find_element(By.XPATH, locators.input_password).send_keys("12")
    driver.find_element(By.XPATH, locators.button_register).click()
    error_message = driver.find_element(By.XPATH, locators.error_password).text
    assert "Некорректный пароль" in error_message


def test_successful_registration(driver):    # Регистрация на сайте
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.generate_name())
    driver.find_element(By.XPATH, locators.input_email).send_keys(configuration.generate_email())
    driver.find_element(By.XPATH, locators.input_password).send_keys(configuration.generate_password())
    driver.find_element(By.XPATH, locators.button_register).click()
    assert "Вход" in driver.find_element(By.XPATH, locators.text_entrance_on_the_login_page).text


def test_login_through_different_buttons(driver):
    driver.get(configuration.URL)  # Вход через главную страницу "Войти"

    driver.find_element(By.XPATH, locators.button_login).click()
    driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
    driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
    driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
    assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text


def test_login_through_different_home_page(driver):
    driver.get(configuration.URL)  # Вход через главную страницу "Личный кабинет"

    driver.find_element(By.XPATH, locators.button_personal_account).click()
    driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
    driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
    driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
    assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text


def test_login_through_button_on_the_registration_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")  # Вход через кнопку в форме регистрации

    driver.find_element(By.XPATH, locators.button_login_from_register).click()
    driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
    driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
    driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
    assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text


def test_login_through_password_recovery_form_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")  # Вход через кнопку в форме регистрации
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
    driver.find_element(By.XPATH, locators.button_login_from_register).click()
    driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
    driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
    driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
    assert 'Оформить заказ' in driver.find_element(By.XPATH, locators.place_an_order_button).text


def test_personal_account_and_constructor(driver):
    driver.get(configuration.URL)
    driver.find_element(By.XPATH, locators.button_personal_account).click()  # Переход в ЛК
    driver.find_element(By.XPATH, locators.button_constructor).click()  # Переход из ЛК в Конструктор
    driver.find_element(By.XPATH, locators.button_personal_account).click()  # Переход в ЛК
    driver.find_element(By.CSS_SELECTOR, locators.button_logotype).click()  # Переход по клику на логотип Stellar Burgers.
    assert 'Соберите бургер' in driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1').text


def test_logout(driver):
    driver.get(configuration.URL)

    driver.find_element(By.XPATH, locators.button_login).click()
    driver.find_element(By.XPATH, locators.input_name).send_keys(configuration.EMAIL)
    driver.find_element(By.XPATH, locators.input_password_in_enter_page).send_keys(configuration.PASSWORD)
    driver.find_element(By.XPATH, locators.button_login_in_chapter).click()
    driver.find_element(By.XPATH, locators.button_personal_account).click()
    driver.find_element(By.XPATH, locators.button_log_out).click()
    successful_registrations = driver.find_element(By.XPATH, locators.text_entrance_on_the_login_page).text
    assert "Вход" in successful_registrations


def test_constructor_navigation(driver):
    driver.get(configuration.URL)
    driver.find_element(By.XPATH, locators.link_sauces).click()
    assert 'Соусы' in driver.find_element(By.XPATH, locators.text_sauces).text
    driver.find_element(By.XPATH, locators.link_buns).click()
    assert 'Булки' in driver.find_element(By.XPATH, locators.text_buns).text
    driver.find_element(By.XPATH, locators.link_fillings).click()
    assert "Начинки" in driver.find_element(By.XPATH, locators.text_fillings).text
