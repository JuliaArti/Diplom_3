from selenium.webdriver.common.by import By

class LocatorsHeader:

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    # Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(),'Личный кабинет')]")

    # Лого
    LOGO = (By.XPATH, "//div[contains(@class,'logo')]")