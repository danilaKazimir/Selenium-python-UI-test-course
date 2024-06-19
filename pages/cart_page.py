from selenium.webdriver.common.by import By

from base.base_class import Base


class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы Cart"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Page url
    url = "https://pcshop.ge/cart/"

    # Locators
    PRODUCT_NAME_FIELD = (By.XPATH, "//td[@data-title='Product']")
    PRICE_FIELD = (By.XPATH, "//td[@data-title='Price']")
    QUANTITY_FIELD = (By.XPATH, "//td[@data-title='Quantity']//input")
    SUBTOTAL_FIELD = (By.XPATH, "//td[@data-title='Subtotal']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "(//a[@class='checkout-button button alt wc-forward'])[1]")

    # Getters
    def get_product_name_field(self):
        return self.wait_for_element_is_visible(self.PRODUCT_NAME_FIELD)

    def get_price_field(self):
        return self.wait_for_element_is_visible(self.PRICE_FIELD)

    def get_quantity_field(self):
        return self.wait_for_element_is_visible(self.QUANTITY_FIELD)

    def get_subtotal_field(self):
        return self.wait_for_element_is_visible(self.SUBTOTAL_FIELD)

    def get_proceed_to_checkout_button(self):
        return self.wait_for_element_is_clickable(self.PROCEED_TO_CHECKOUT_BUTTON)

    # Actions
    def click_proceed_to_checkout_button(self):
        self.get_proceed_to_checkout_button().click()
        print("Click on proceed to checkout button")

    # Methods
    def cart_page_is_opened(self):
        self.page_is_opened(self.url)

    def check_item_in_cart_information(self, expected_name, expected_price, expected_quantity, expected_subtotal):
        self.assert_value(self.get_product_name_field().text, expected_name)
        self.assert_value(self.get_price_field().text, expected_price)
        quantity = self.get_attribute_value(self.get_quantity_field(), "value")
        self.assert_value(quantity, expected_quantity)
        self.assert_value(self.get_subtotal_field().text, expected_subtotal)
        self.check_cart_icon_status_information(expected_quantity=expected_quantity, expected_price=expected_price)
        print("Info about product in cart is correct")

    def open_checkout_page(self):
        self.click_proceed_to_checkout_button()
