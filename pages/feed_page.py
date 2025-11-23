import allure
from data.urls import Urls
from pages.base_page import BasePageBurger
from locators.feed_page_locators import LocatorsFeed

class FeedPageBurgers(BasePageBurger):

    @allure.step('Вызов страницы авторизации')    
    def open_feed_page(self):
        self.open_url(Urls.feed_page)

    @allure.step('Получаем количество заказов за сегодня')
    def get_completed_today(self):
        self.wait_visibility_of_element(LocatorsFeed.today_value)
        return self.get_text_on_element(LocatorsFeed.today_value)

    @allure.step('Получаем количество заказов за сегодня')
    def get_completed_all_time(self):
        self.wait_visibility_of_element(LocatorsFeed.all_time_value)
        return self.get_text_on_element(LocatorsFeed.all_time_value)
    
    def find_order_in_progress(self, order_num):
        order_locator = LocatorsFeed.get_order_in_progress_locator(order_num)
        return self.wait_visibility_of_element(order_locator)
        