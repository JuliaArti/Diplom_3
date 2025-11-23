from selenium.webdriver.common.by import By

class LocatorsLogin:

    # Поле "Email"
    input_field_email = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")

    # Поле "Пароль"
    input_field_password = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")

    # Кнопка "Войти"
    button_entrance = (By.XPATH, "//button[text()='Войти']")