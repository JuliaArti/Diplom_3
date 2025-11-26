from selenium.webdriver.common.by import By

class LocatorsMain:

    # Флюоресцентная булка
    fluorescent_bun = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]")

    # Счетчик флюоресцентных булок
    fluorescent_bun_counter = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]//p[contains(@class, 'counter_counter__num__3nue1')]")

    # Попап ингредиента
    ingredient_popup = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]")
    
    # Крестик на попапе ингредиента
    ingredient_popup_cross = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")

    # Корзина конструктора
    constructor_basket = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")

    # Кнопка "Оформить заказ"
    place_order_button = (By.XPATH, "//button[text()='Оформить заказ']")

    # Лоадер страницы
    main_loader = (By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]")

    # Поле номера заказа
    order_num_field = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")

    # Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")