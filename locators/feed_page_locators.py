from selenium.webdriver.common.by import By

class LocatorsFeed:

    # Значение поля "Выполнено за все время"
    all_time_value = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    # Значение поля "Выполнено за сегодня"
    today_value = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    @staticmethod
    def get_order_in_progress_locator(order_num):
        return (By.XPATH, f'//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]//li[contains(., "{order_num}")]')