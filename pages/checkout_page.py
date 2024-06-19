from selenium.webdriver.common.by import By

from base.base_class import Base


class CheckoutPage(Base):
    """ Класс содержащий локаторы и методы для страницы Checkout"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://pcshop.ge/checkout/"  # url checkout

    # Locators
    click_here_to_login_link = (By.XPATH, "//a[@class='showlogin']")
    login_username_field = (By.XPATH, "//input[@id='username']")
    login_password_field = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//button[@name='login']")
    first_name_field = (By.XPATH, "//input[@id='billing_first_name']")
    last_name_field = (By.XPATH, "//input[@id='billing_last_name']")
    id_number_field = (By.XPATH, "//input[@id='billing_id']")
    town_field = (By.XPATH, "//input[@id='billing_city']")
    address_field = (By.XPATH, "//input[@id='billing_address_1']")
    phone_field = (By.XPATH, "//input[@id='billing_phone']")
    email_address_field = (By.XPATH, "//input[@id='billing_email']")
    order_product_name = (By.XPATH, "//td[@class='product-name']")
    order_total_price = (By.XPATH, "//tr[@class='order-total']//td//bdi")
    login_suggestion = (By.XPATH, "//div[@class='woocommerce-info']")

    # Getters
    def get_click_here_to_login_link(self):
        return self.wait_for_element_is_clickable(self.click_here_to_login_link)

    def get_login_username_field(self):
        return self.wait_for_element_is_clickable(self.login_username_field)

    def get_login_password_field(self):
        return self.wait_for_element_is_clickable(self.login_password_field)

    def get_login_button(self):
        return self.wait_for_element_is_clickable(self.login_button)

    def get_first_name_field(self):
        return self.wait_for_element_is_clickable(self.first_name_field)

    def get_last_name_field(self):
        return self.wait_for_element_is_clickable(self.last_name_field)

    def get_id_number_field(self):
        return self.wait_for_element_is_clickable(self.id_number_field)

    def get_town_field(self):
        return self.wait_for_element_is_clickable(self.town_field)

    def get_address_field(self):
        return self.wait_for_element_is_clickable(self.address_field)

    def get_phone_field(self):
        return self.wait_for_element_is_clickable(self.phone_field)

    def get_email_address_field(self):
        return self.wait_for_element_is_clickable(self.email_address_field)

    def get_login_suggestion(self):
        return self.wait_for_element_is_visible(self.login_suggestion)

    def get_order_product_name(self):
        return self.wait_for_element_is_visible(self.order_product_name)

    def get_order_total_price(self):
        return self.wait_for_element_is_visible(self.order_total_price)

    # Actions
    def click_on_click_here_to_login_link(self):
        self.get_click_here_to_login_link().click()

    def insert_login_username_field(self, email):
        self.get_login_username_field().send_keys(email)

    def insert_login_password_field(self, password):
        self.get_login_password_field().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    # Methods
    def checkout_page_is_opened(self):
        self.page_is_opened(self.url)

    def login_into_account(self, name, password):
        login_suggestion = self.get_login_suggestion()
        self.click_on_click_here_to_login_link()
        self.insert_login_username_field(name)
        self.insert_login_password_field(password)
        self.click_login_button()
        self.wait_for_element_is_invisible(login_suggestion)
        print("Login into account is success!")

    def check_billing_details_autocomplete_after_login(self, exp_firstname, exp_lastname, exp_id_number, exp_town,
                                                       exp_user_address, exp_user_phone, exp_user_email):
        first_name_value = self.get_attribute_value(self.get_first_name_field(), "value")
        self.assert_value(first_name_value, exp_firstname)
        last_name_value = self.get_attribute_value(self.get_last_name_field(), "value")
        self.assert_value(last_name_value, exp_lastname)
        id_number_value = self.get_attribute_value(self.get_id_number_field(), "value")
        self.assert_value(id_number_value, exp_id_number)
        town_value = self.get_attribute_value(self.get_town_field(), "value")
        self.assert_value(town_value, exp_town)
        address_value = self.get_attribute_value(self.get_address_field(), "value")
        self.assert_value(address_value, exp_user_address)
        phone_value = self.get_attribute_value(self.get_phone_field(), "value")
        self.assert_value(phone_value, exp_user_phone)
        email_value = self.get_attribute_value(self.get_email_address_field(), "value")
        self.assert_value(email_value, exp_user_email)
        print("Account values is filled correctly!")

    def check_order_details(self, expected_name, expected_quantity, expected_price):
        self.assert_value(self.get_order_product_name().text, f"{expected_name}   × {expected_quantity}")
        self.assert_value(self.get_order_total_price().text, expected_price)
        print("Order details is correct!")
