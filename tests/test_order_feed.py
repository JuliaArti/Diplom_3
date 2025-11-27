import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.login_page import LoginPageBurgers
from pages.main_page import MainPageBurgers
from pages.feed_page import FeedPageBurgers
from data.user import User

class TestOrderFeed:
    
    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    @allure.description('Авторизуемся, создаем заказ и проверяем счетчик')
    def test_counter_all_time(self, driver: WebDriver):
        login_page = LoginPageBurgers(driver)
        main_page = MainPageBurgers(driver)
        feed_page = FeedPageBurgers(driver)
        
        # Авторизуемся
        login_page.open_login_page()
        login_page.login(User.email, User.password)

        # Получаем текущее количество заказов за все время
        feed_page.open_feed_page()
        old_value = int(feed_page.get_completed_all_time())

        # Отправляем заказ
        main_page.open_main_page()
        main_page.drag_bun_to_constructor()
        main_page.place_order()
        main_page.wait_order_result()

        # Получаем новое количество заказов за все время
        feed_page.open_feed_page()
        new_value = int(feed_page.get_completed_all_time())
        assert new_value > old_value, "Количество заказов не увеличелось"

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    @allure.description('Авторизуемся, создаем заказ и проверяем счетчик')
    def test_counter_today(self, driver: WebDriver):
        login_page = LoginPageBurgers(driver)
        main_page = MainPageBurgers(driver)
        feed_page = FeedPageBurgers(driver)
        
        # Авторизуемся
        login_page.open_login_page()
        login_page.login(User.email, User.password)

        # Получаем текущее количество заказов за все время
        feed_page.open_feed_page()
        old_value = int(feed_page.get_completed_today())

        # Отправляем заказ
        main_page.open_main_page()
        main_page.drag_bun_to_constructor()
        main_page.place_order()
        main_page.wait_order_result()

        # Получаем новое количество заказов за все время
        feed_page.open_feed_page()
        new_value = int(feed_page.get_completed_today())
        assert new_value > old_value, "Количество заказов не увеличелось"

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('Авторизуемся, создаем заказ, получаем номер заказа ипроверяем его в списке заказов в работе')
    def test_orders_in_progress(self, driver: WebDriver):
        login_page = LoginPageBurgers(driver)
        main_page = MainPageBurgers(driver)
        feed_page = FeedPageBurgers(driver)
        
        # Авторизуемся
        login_page.open_login_page()
        login_page.login(User.email, User.password)

        # Отправляем заказ
        main_page.open_main_page()
        main_page.drag_bun_to_constructor()
        main_page.place_order()
        main_page.wait_order_result()
        order_num = main_page.get_order_number()

        # Проверяем отображение заказа по номеру в разделе "В Работе"
        feed_page.open_feed_page()
        assert feed_page.find_order_in_progress(order_num), "Заказ не отображается в разделе 'В работе'"
