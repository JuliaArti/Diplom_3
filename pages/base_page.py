import allure
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

class BasePageBurger:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    @staticmethod
    def css_property_equals(locator, css_property, expected_value):
        # Ожидание конкретного значения CSS-свойства
        def _predicate(driver):
            try:
                element = driver.find_element(*locator)
                actual_value = element.value_of_css_property(css_property)
                return actual_value == expected_value
            except:
                return False
        return _predicate

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))  

    @allure.step('Подождать определенного значения CSS свойства')
    def wait_css_value(self, locator, property, value):
        return WebDriverWait(self.driver, 6).until(BasePageBurger.css_property_equals(locator, property, value))  

    @allure.step('Кликнуть элемент')  
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()        

    @allure.step('Ввести назначение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys) 

    @allure.step('Получить текст на элемент')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text            

    @allure.step('Ожидание загрузки URL')
    def wait_loading_of_url(self, url):
        return WebDriverWait(self.driver, 6).until(expected_conditions.url_to_be(url))  
    
    @allure.step('Открытие страницы')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Проверка, что элемента нет на странице')  
    def check_element_missing(self, locator):
        return len(self.driver.find_elements(*locator)) == 0
    
    @allure.step('Перетаскивание одного элемента на другой')  
    def drag_element(self, source_element_locator, target_element_locator):
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(source_element_locator))
        source_element = self.driver.find_element(*source_element_locator)
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(target_element_locator))
        target_element = self.driver.find_element(*target_element_locator)

        js_script = """
        function simulateDragDrop(sourceNode, targetNode) {
            var event = document.createEvent('CustomEvent');
            event.initCustomEvent('dragstart', true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(type, val) {
                    this.data[type] = val;
                },
                getData: function(type) {
                    return this.data[type];
                },
                files: [],
                items: [],
                types: [],
                setDragImage: function() {}
            };
            sourceNode.dispatchEvent(event);
            
            var dropEvent = document.createEvent('CustomEvent');
            dropEvent.initCustomEvent('drop', true, true, null);
            dropEvent.dataTransfer = event.dataTransfer;
            targetNode.dispatchEvent(dropEvent);
            
            var dragEndEvent = document.createEvent('CustomEvent');
            dragEndEvent.initCustomEvent('dragend', true, true, null);
            dragEndEvent.dataTransfer = event.dataTransfer;
            sourceNode.dispatchEvent(dragEndEvent);
        }
        
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_script, source_element, target_element)

