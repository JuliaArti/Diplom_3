import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_page import MainPageBurgers
from pages.feed_page import FeedPageBurgers
from data.urls import Urls

class TestBurgersSmoke:
    
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Переход с главной страницы на ленту заказов, клик на кнопку Конструктор')
    def test_constructor(self, driver: WebDriver):
        main_page = MainPageBurgers(driver)
        feed_page = FeedPageBurgers(driver)
        main_page.open_main_page()
        main_page.go_to_order_feed()
        main_page.wait_loading_of_url(Urls.feed_page)
        feed_page.go_to_constructor()
        assert feed_page.wait_loading_of_url(Urls.main_site)

    @allure.title('Переход по клику на раздел «Лента заказов»')
    @allure.description('Переход с главной страницы на ленту заказов')
    def test_orders_feed(self, driver: WebDriver):
        main_page = MainPageBurgers(driver)
        main_page.open_main_page()
        main_page.go_to_order_feed()
        assert main_page.wait_loading_of_url(Urls.feed_page)

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('При клике на ингредиент должно появится всплывающее окно')
    def test_ingredient_popup(self, driver: WebDriver):
        main_page = MainPageBurgers(driver)
        main_page.open_main_page()
        main_page.click_fluorescent_bun()
        assert main_page.check_ingredient_popup_visible()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Отрываем попап и закрываем по крестику')
    def test_ingredient_popup_cross(self, driver: WebDriver):
        main_page = MainPageBurgers(driver)
        main_page.open_main_page()
        main_page.click_fluorescent_bun()
        main_page.check_ingredient_popup_visible()
        main_page.click_ingredient_popup_cross()
        assert main_page.check_ingredient_popup_hidden()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('Перетаскиваем булочку в конструктор и проверяем счетчик')
    def test_ingredient_counter(self, driver: WebDriver):
        main_page = MainPageBurgers(driver)
        main_page.open_main_page()
        main_page.drag_bun_to_constructor()
        assert main_page.get_fluorescent_bun_counter_text() == "2" # потому что в бургере 2 булки
