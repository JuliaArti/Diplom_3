import allure
from data.urls import Urls
from pages.base_page import BasePageBurger
from locators.main_page_locators import LocatorsMain

class MainPageBurgers(BasePageBurger):
    
    @allure.step('Вызов стартовой страницы')    
    def open_main_page(self):
        self.open_url(Urls.main_site)
        self.wait_css_value((LocatorsMain.main_loader), 'visibility', 'hidden')

    @allure.step('Кликаем на ингредиент - Флюоресцентная булка')
    def click_fluorescent_bun(self):
        self.wait_visibility_of_element((LocatorsMain.fluorescent_bun))
        self.click_on_element((LocatorsMain.fluorescent_bun))

    @allure.step('Проверяем что попап с деталями ингредиента открылся')
    def check_ingredient_popup_visible(self):
        return self.wait_visibility_of_element((LocatorsMain.ingredient_popup))
    
    @allure.step('Проверяем что попап с деталями ингредиента закрыт')
    def check_ingredient_popup_hidden(self):
        return self.check_element_missing((LocatorsMain.ingredient_popup))

    @allure.step('Кликаем на крестик в попапе ингредиента')
    def click_ingredient_popup_cross(self):
        self.wait_visibility_of_element((LocatorsMain.ingredient_popup_cross))
        self.click_on_element((LocatorsMain.ingredient_popup_cross))

    @allure.step('Перетаскиваем булочку в конструктор')
    def drag_bun_to_constructor(self):
        self.drag_element((LocatorsMain.fluorescent_bun), (LocatorsMain.constructor_basket))

    @allure.step('Получаем количество булочек')
    def get_fluorescent_bun_counter_text(self):
        return self.get_text_on_element((LocatorsMain.fluorescent_bun_counter))
    
    @allure.step('Отправляем заказ')
    def place_order(self):
        self.wait_visibility_of_element(LocatorsMain.place_order_button)
        return self.click_on_element((LocatorsMain.place_order_button))
    
    @allure.step('Дождаться ответа на отпралвенный заказ')
    def wait_order_result(self):
        self.wait_visibility_of_element((LocatorsMain.main_loader))
        return self.wait_css_value((LocatorsMain.main_loader), 'visibility', 'hidden')
    
    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_visibility_of_element((LocatorsMain.order_num_field))
        return self.get_text_on_element((LocatorsMain.order_num_field))