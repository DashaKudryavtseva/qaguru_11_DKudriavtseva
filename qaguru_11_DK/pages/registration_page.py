from pathlib import Path
from selene import browser, have, command
import tests


class RegistrationPage:
    def __init__(self):
        self.google_adds = browser.all("[id^=google_ads][id$=container__]")
        self.submit = browser.element("#submit")

    def take_out_ads(self):
        self.google_adds.with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.google_adds.perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element("#firstName").type(value).press_enter()

    def fill_last_name(self, value):
        browser.element("#lastName").type(value).press_enter()

    def fill_user_email(self, value):
        browser.element("#userEmail").type(value).press_enter()

    def choose_gender(self, value):
        browser.all("[for^=gender-radio]").element_by(have.text(value)).click()

    def fill_user_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").send_keys(month)
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, *names):
        for name in names:
            browser.element("#subjectsInput").set_value(name).press_enter()

    def choose_hobbies(self, *values):
        for value in values:
            browser.all(".custom-checkbox").element_by(have.exact_text(value)).click()

    def upload_picture(self, file_name):
        browser.element("#uploadPicture").set_value(
            str(
                Path(tests.__file__)
                .parent.joinpath(f'resources/{file_name}')
                .absolute()
            )
        )

    def fill_address(self, value):
        browser.element("#currentAddress").type(value).press_enter()

    def choose_state(self, value):
        browser.element("#state").perform(command.js.scroll_into_view)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.text(value)
        ).click()

    def choose_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.text(value)
        ).click()

    def submit_form(self):
        self.submit.perform(command.js.scroll_into_view)
        self.submit.click()

    def should_have_register_info(
        self,
        user_name,
        email,
        gender,
        telephone_number,
        date_of_birth,
        subjects,
        hobbies,
        picture,
        address,
        state_city,
    ):
        browser.element(".table").all("td").even.should(
            have.texts(
                user_name,
                email,
                gender,
                telephone_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_city,
            )
        )
