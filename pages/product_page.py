from selenium.webdriver.common.by import By

from base.base_class import Base


class ProductPage(Base):
    """ Класс содержащий локаторы и методы для страницы товара"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Page url
    URL = "https://pcshop.ge/product/samsung-galaxy-a55-8gb-128gb-awesome-lemon/"

    # Locators
    SKU_NUMBER = (By.XPATH, "//div[@class='example']")
    PRODUCT_TITLE = (By.XPATH, "//h1[@class='product_title entry-title']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".single-product-wrapper .price bdi")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@name='add-to-cart']")
    ITEM_ADDED_TO_CART_MESSAGE = (By.XPATH, "//div[@class='woocommerce-message']")
    VIEW_CART_BUTTON = (By.XPATH, "//div[@class='woocommerce-message']//a")

    # Getters
    def get_sku_number(self):
        return self.wait_for_element_is_visible(self.SKU_NUMBER)

    def get_product_title(self):
        return self.wait_for_element_is_visible(self.PRODUCT_TITLE)

    def get_product_price(self):
        return self.wait_for_element_is_visible(self.PRODUCT_PRICE)

    def get_add_to_cart_button(self):
        return self.wait_for_element_is_clickable(self.ADD_TO_CART_BUTTON)

    def get_item_added_to_cart_message(self):
        return self.wait_for_element_is_visible(self.ITEM_ADDED_TO_CART_MESSAGE)

    def get_view_cart_button(self):
        return self.wait_for_element_is_clickable(self.VIEW_CART_BUTTON)

    # Actions
    def click_view_cart_button(self):
        self.get_view_cart_button().click()
        print("Click to view cart button")

    # Methods
    def product_page_is_opened(self):
        self.page_is_opened(self.URL)

    def add_product_to_cart(self):
        self.get_add_to_cart_button().click()

    def assert_product_was_added_to_cart(self, expected_name, expected_price, expected_quantity):
        message = self.get_item_added_to_cart_message().text
        message = message[message.find("“"):]
        self.assert_value(message, f'“{expected_name}” has been added to your cart.')
        self.check_cart_icon_status_information(expected_quantity=expected_quantity, expected_price=expected_price)
        print("Product was successfully added to cart")

    def check_product_information(self, expected_sku, expected_name, expected_price):
        self.assert_value(self.get_sku_number().text, f"SKU: {expected_sku}")
        self.assert_value(self.get_product_title().text, expected_name)
        self.assert_value(self.get_product_price().text, expected_price)
        print("Product information is correct!")

    def open_cart(self):
        self.click_view_cart_button()
