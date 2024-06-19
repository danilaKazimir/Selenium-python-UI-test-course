from selenium.webdriver.common.by import By

from base.base_class import Base


class MainPage(Base):
    """ Класс содержащий локаторы и методы для главной страницы сайта"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # PAGE URL
    URL = "https://pcshop.ge/"

    # Locators
    HAMBURGER_MENU = (By.XPATH, "(//button[@class='navbar-toggler navbar-toggle-hamburger '])[1]")
    SMARTPHONES_AND_TABLETS_DROPDOWN_ITEM = (By.XPATH, "(//a[@title='Smartphones & Tablets'])[1]")
    SMARTPHONES_DROPDOWN_ITEM = (By.XPATH, "(//a[@title='Smartphones'])[1]")

    # Getters
    def get_hamburger_menu(self):
        return self.wait_for_element_is_clickable(self.HAMBURGER_MENU)

    def get_smartphones_and_tablets_dropdown_item(self):
        return self.wait_for_element_is_clickable(self.SMARTPHONES_AND_TABLETS_DROPDOWN_ITEM)

    def get_smartphones_dropdown_item(self):
        return self.wait_for_element_is_clickable(self.SMARTPHONES_DROPDOWN_ITEM)

    # Actions
    def click_hamburger_menu(self):
        self.get_hamburger_menu().click()
        print("Click on hamburger menu")

    def click_smartphones_and_tablets_dropdown_item(self):
        self.get_smartphones_and_tablets_dropdown_item().click()
        print("Click on Smartphones & Tablets dropdown item")

    def click_smartphones_dropdown_item(self):
        self.get_smartphones_dropdown_item().click()
        print("Click on Smartphones dropdown item")

    # Methods
    def main_page_is_opened(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.page_is_opened(self.URL)

    def navigate_to_smartphone_page(self):
        self.click_hamburger_menu()
        self.click_smartphones_and_tablets_dropdown_item()
        self.click_smartphones_dropdown_item()
