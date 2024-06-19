import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_up():
    print("\nTest is started!")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver

    print("\nTest is successfully passed!")
    driver.quit()


@pytest.fixture()
def user_data():
    return {
        "user_email": "annieviolet123@outlook.com",
        "user_password": "va2Xaih1eif",
        "user_firstname": "Test First Name",
        "user_lastname": "Test Last Name",
        "user_id_number": "123123123",
        "user_town": "Tbilisi",
        "user_address": "Navtlughi 10/2",
        "user_phone": "+995 111 111 111"
    }
