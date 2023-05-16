import allure
from selene import browser
from qaguru_11_DK.pages.registration_page import RegistrationPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.tag('web')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешная регистрация')
def test_fill_registration_form(browser_configuration):
    registration_page = RegistrationPage()

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": False},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    browser.config.driver = driver

    with allure.step('Открытие страницы регистрации'):
        browser.open("/automation-practice-form")
        registration_page.take_out_ads()

    # WHEN
    with allure.step('Заполнение полей имени'):
        registration_page.fill_first_name('Maria')
        registration_page.fill_last_name('Ivanova')

    with allure.step('Ввод почты'):
        registration_page.fill_user_email('examplemail@mail.com')

    with allure.step('Выбор пола'):
        registration_page.choose_gender('Female')

    with allure.step('Ввод номера телефона'):
        registration_page.fill_user_number('8987654321')

    with allure.step('Указание даты рождения'):
        registration_page.fill_date_of_birth('1996', 'January', '01')

    with allure.step('Выбор предметов'):
        registration_page.fill_subjects('English', 'Chemistry')

    with allure.step('Выбор хобби'):
        registration_page.choose_hobbies('Sports', 'Reading')

    with allure.step('Прикрепление картинки'):
        registration_page.upload_picture('example.png')

    with allure.step('Указание адреса'):
        registration_page.fill_address('Sport Street, 140')

    with allure.step('Выбор штата и города'):
        registration_page.choose_state('NCR')
        registration_page.choose_city('Delhi')

    with allure.step('Отправление заполненных данных'):
        registration_page.submit_form()

    # THEN
    with allure.step('Проверка соответствия данных'):
        registration_page.should_have_register_info(
            "Maria Ivanova",
            "examplemail@mail.com",
            "Female",
            "8987654321",
            "01 January,1996",
            "English, Chemistry",
            "Sports, Reading",
            "example.png",
            "Sport Street, 140",
            "NCR Delhi",
        )
