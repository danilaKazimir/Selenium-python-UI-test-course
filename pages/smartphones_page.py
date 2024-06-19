from selenium.webdriver.common.by import By

from base.base_class import Base


class SmartphonesPage(Base):
    """ Класс содержащий локаторы и методы для страницы Smartphones"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Page url
    URL = "https://pcshop.ge/product-category/smartphones-tablets/smartphones/"

    # Query value in url after filter
    QUERY_IN_URL_AFTER_FILTER_BY_BRAND = "brand=samsung"
    QUERY_IN_URL_AFTER_FILTER_BY_MEMORY_CAPACITY = "memory-capacity=8gb"
    QUERY_IN_URL_AFTER_FILTER_BY_OPERATING_SYSTEM = "operating-system=android-14"
    QUERY_IN_URL_AFTER_FILTER_BY_COLOR = "color=awsome-lemon"

    # Locators
    BRAND_SAMSUNG_CHECKBOX = (By.XPATH, "//div[@data-item-key='samsung']")
    MEMORY_CAPACITY_FILTER = (By.XPATH, "//span[text()='Memory Capacity']")
    MEMORY_CAPACITY_8GB_CHECKBOX = (By.XPATH, "//div[@data-item-key='8gb']")
    OPERATING_SYSTEM_FILTER = (By.XPATH, "//span[text()='Operating System']")
    OPERATING_SYSTEM_ANDROID14_CHECKBOX = (By.XPATH, "//div[@data-item-key='android-14']")
    COLOR_FILTER = (By.XPATH, "//span[text()='Color']")
    COLOR_AWESOME_LEMON_CHECKBOX = (By.XPATH, "//div[@data-item-key='awsome-lemon']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".product-outer.product-item__outer")
    PRODUCT_NAME_GRID_VIEW = (By.XPATH, "(//h2[text()='Samsung Galaxy A55 8GB 128GB Awesome Lemon'])[1]")
    PRODUCT_PRICE_GRID_VIEW = (By.CSS_SELECTOR, ".price .electro-price bdi")
    RESULT_COUNT_PAGE_HEADER = (By.XPATH, "//header//p[@class='woocommerce-result-count']")
    RESULT_COUNT_PAGE_BAR_BOTTOM = (
        By.XPATH, "//div[@class='shop-control-bar-bottom']//p[@class='woocommerce-result-count']")

    # Getters
    def get_brand_samsung_checkbox(self):
        return self.wait_for_element_is_clickable(self.BRAND_SAMSUNG_CHECKBOX)

    def get_memory_capacity_filter(self):
        return self.wait_for_element_is_clickable(self.MEMORY_CAPACITY_FILTER)

    def get_memory_capacity_8gb_checkbox(self):
        return self.wait_for_element_is_clickable(self.MEMORY_CAPACITY_8GB_CHECKBOX)

    def get_operating_system_filter(self):
        return self.wait_for_element_is_clickable(self.OPERATING_SYSTEM_FILTER)

    def get_operating_system_android14_checkbox(self):
        return self.wait_for_element_is_clickable(self.OPERATING_SYSTEM_ANDROID14_CHECKBOX)

    def get_color_filter(self):
        return self.wait_for_element_is_clickable(self.COLOR_FILTER)

    def get_color_awesome_lemon_checkbox(self):
        return self.wait_for_element_is_clickable(self.COLOR_AWESOME_LEMON_CHECKBOX)

    def get_products_list(self):
        return self.wait_for_elements_is_visible(self.PRODUCTS_LIST)

    def get_product_name(self):
        return self.wait_for_element_is_visible(self.PRODUCT_NAME_GRID_VIEW)

    def get_product_price(self):
        return self.wait_for_element_is_visible(self.PRODUCT_PRICE_GRID_VIEW)

    def get_result_count_page_header(self):
        return self.wait_for_element_is_visible(self.RESULT_COUNT_PAGE_HEADER)

    def get_result_count_page_bar_bottom(self):
        return self.wait_for_element_is_visible(self.RESULT_COUNT_PAGE_BAR_BOTTOM)

    # Actions
    def click_brand_samsung_checkbox(self):
        self.scroll_and_click_on_element(self.get_brand_samsung_checkbox())
        print("Click on samsung checkbox")
        self.wait_for_element_is_disappeared(self.loader)
        self.assert_url(f"{self.URL}?{self.QUERY_IN_URL_AFTER_FILTER_BY_BRAND}")

    def click_memory_capacity_filter(self):
        self.scroll_and_click_on_element(self.get_memory_capacity_filter())
        print("Click on memory capacity filter")

    def click_memory_capacity_8gb_checkbox(self):
        self.scroll_and_click_on_element(self.get_memory_capacity_8gb_checkbox())
        print("Click on 8gb checkbox")
        self.wait_for_element_is_disappeared(self.loader)
        self.assert_url(
            f"{self.URL}?{self.QUERY_IN_URL_AFTER_FILTER_BY_BRAND}&{self.QUERY_IN_URL_AFTER_FILTER_BY_MEMORY_CAPACITY}")

    def click_operating_system_filter(self):
        self.scroll_and_click_on_element(self.get_operating_system_filter())
        print("Click on operating system filter")

    def click_operating_system_android14_checkbox(self):
        self.scroll_and_click_on_element(self.get_operating_system_android14_checkbox())
        print("Click on android 14 checkbox")
        self.wait_for_element_is_disappeared(self.loader)
        self.assert_url(
            f"{self.URL}?{self.QUERY_IN_URL_AFTER_FILTER_BY_BRAND}&{self.QUERY_IN_URL_AFTER_FILTER_BY_MEMORY_CAPACITY}"
            f"&{self.QUERY_IN_URL_AFTER_FILTER_BY_OPERATING_SYSTEM}")

    def click_color_filter(self):
        self.get_color_filter().click()
        print("Click on color filter")

    def click_color_awesome_lemon_checkbox(self):
        self.get_color_awesome_lemon_checkbox().click()
        print("Click on awesome navy checkbox")
        self.wait_for_element_is_disappeared(self.loader)
        self.assert_url(
            f"{self.URL}?{self.QUERY_IN_URL_AFTER_FILTER_BY_BRAND}&{self.QUERY_IN_URL_AFTER_FILTER_BY_MEMORY_CAPACITY}"
            f"&{self.QUERY_IN_URL_AFTER_FILTER_BY_OPERATING_SYSTEM}&{self.QUERY_IN_URL_AFTER_FILTER_BY_COLOR}")

    # Methods
    def smartphones_page_is_opened(self):
        self.page_is_opened(self.URL)

    def filter_products(self):
        self.click_brand_samsung_checkbox()
        self.click_memory_capacity_filter()
        self.click_memory_capacity_8gb_checkbox()
        self.click_operating_system_filter()
        self.click_operating_system_android14_checkbox()
        self.click_color_filter()
        self.click_color_awesome_lemon_checkbox()
        print("Product is filtered correctly!")

    def check_product(self, expected_number, expected_name, expected_price):
        self.assert_elements_count(self.get_products_list(), expected_number)
        self.assert_value(self.get_product_name().text, expected_name)
        self.assert_value(self.get_product_price().text, expected_price)
        print("Product parameters are correct!")

    def check_result_count_values(self):
        self.assert_value(self.get_result_count_page_header().text, "Showing the single result")
        self.assert_value(self.get_result_count_page_bar_bottom().text, "Showing the single result")
        print("Result count values are correct!")

    def open_product_page(self):
        self.get_products_list()[0].click()
        print("Click on product item")
