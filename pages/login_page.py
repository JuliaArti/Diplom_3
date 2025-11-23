import allure
from data.urls import Urls
from pages.base_page import BasePageBurger
from locators.login_page_locators import LocatorsLogin

class LoginPageBurgers(BasePageBurger):

    @allure.step('Вызов страницы авторизации')    
    def open_login_page(self):
        self.open_url(Urls.login_page)

    @allure.step('Авторизация')
    def login(self, email, password):
        self.wait_visibility_of_element(LocatorsLogin.input_field_email)
        self.send_keys_to_input(LocatorsLogin.input_field_email, email)
        self.wait_visibility_of_element(LocatorsLogin.input_field_password)
        self.send_keys_to_input(LocatorsLogin.input_field_password, password)
        self.wait_visibility_of_element(LocatorsLogin.button_entrance)
        self.click_on_element(LocatorsLogin.button_entrance)
        self.wait_loading_of_url(Urls.main_site)