from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    """ Методы с использованием WebDriverWait
    Вынес их в базовый класс, чтобы не дублировать использование на каждой странице сайта"""
    # Method to wait until element is clickable
    def wait_for_element_is_clickable(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator '{locator}' isn't clickable within {timeout} seconds")

    # Method to wait until element is visible
    def wait_for_element_is_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator '{locator}' isn't visible within {timeout} seconds")

    # Method to wait until elements is visible
    def wait_for_elements_is_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Elements with locator '{locator}' isn't visible within {timeout} seconds")

    # Method to wait until element is invisible
    def wait_for_element_is_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator '{locator}' still displayed after {timeout} seconds")

    # Method to wait until element is disappeared from DOM
    def wait_for_element_is_disappeared(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator '{locator} still in DOM after {timeout} seconds'")

    """ Базовые методы для проверок"""
    # Method to get element attribute value
    def get_attribute_value(self, element, attribute):
        return (WebDriverWait(self.driver, 10).until
                (lambda driver: element.get_attribute(attribute) is not None and element.get_attribute(attribute)))

    # Method to get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url is {get_url}")

    # Method assert url
    def assert_url(self, expected_result):
        get_url = self.driver.current_url
        assert expected_result == get_url, f"URL isn't correct, expected url - {expected_result}, but is - {get_url}"
        print("URL is correct!")

    # Assert element count
    def assert_elements_count(self, locator, expected_count):
        assert expected_count == len(
            locator), f"Expected count of elements is {expected_count}, but instead is {len(locator)}"
        print(f"Elements count is correct - {expected_count}")

    # Method to assert text values
    def assert_value(self, actual_result, expected_result):
        assert expected_result == actual_result, f"Expected value is {expected_result}, but is {actual_result}"

    """ Ниже другие вспомогательные методы, которые актуальны для всех страниц сайта """
    """ Добавил этот метод, т.к. без него некоторые фильтры нельзя было кликнуть (была ошибка клик по элементу не 
    доступен в этом состоянии или что-то такое), решилось этой реализацией, вынес в отдельный метод в базовом классе"""
    # Method to scroll and click on element
    def scroll_and_click_on_element(self, get_element):
        actions = ActionChains(self.driver)
        actions.move_to_element(get_element).click().perform()

    """ Селектор лоадера который перекрывает страницу при применении фильтров и вероятно при каких то других действиях"""
    loader = (By.CSS_SELECTOR, ".blockUI")

    """ На каждой странице сайта есть логотип, который также является кликабельным. Использую отображение этого элемента
    для проверки того, что каждая страница прогрузилась до конца"""
    # Pc shop image locator
    PC_SHOP_IMAGE = (By.XPATH, "//img[@class='img-header-logo lazyloaded']")

    # Pc shop image is visible and clickable
    def assert_logo_is_displayed_and_opened(self):
        self.wait_for_element_is_visible(self.PC_SHOP_IMAGE)
        self.wait_for_element_is_clickable(self.PC_SHOP_IMAGE)
        print("PC Shop logo is displayed and clickable!")

    # Method to assert page is opened
    def page_is_opened(self, url):
        self.get_current_url()
        self.assert_url(url)
        self.assert_logo_is_displayed_and_opened()
        print("Page is correctly opened!")

    """ Значок корзины отображается на каждой странице, соответственно на каждой странице можно проверять ее значения, 
    вынес локаторы и методы для проверки в базовый класс"""
    CART_ICON_ITEM_COUNT = (By.CSS_SELECTOR, ".dropdown-toggle .cart-items-count.count.header-icon-counter")
    CART_ICON_ITEM_PRICE = (By.CSS_SELECTOR, ".dropdown-toggle .cart-items-total-price.total-price")

    def get_cart_icon_item_count(self):
        return self.wait_for_element_is_clickable(self.CART_ICON_ITEM_COUNT)

    def get_cart_icon_item_price(self):
        return self.wait_for_element_is_clickable(self.CART_ICON_ITEM_PRICE)

    def check_cart_icon_status_information(self, expected_quantity, expected_price):
        self.assert_value(self.get_cart_icon_item_count().text, expected_quantity)
        self.assert_value(self.get_cart_icon_item_price().text, expected_price)
        print("Cart icon information is correct!")
