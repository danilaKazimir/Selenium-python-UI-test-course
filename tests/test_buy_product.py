from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.smartphones_page import SmartphonesPage


def test_buy_product(set_up, user_data):
    """Тест по покупке товара Samsung Galaxy A55 8GB 128GB Awesome Lemon"""
    # Product constant
    product_name = "Samsung Galaxy A55 8GB 128GB Awesome Lemon"
    product_price = "₾999.00"
    product_sku_number = "I31295"

    driver = set_up
    print("Start Test")

    mp = MainPage(driver)
    mp.main_page_is_opened()
    mp.navigate_to_smartphone_page()

    sp = SmartphonesPage(driver)
    sp.smartphones_page_is_opened()
    sp.filter_products()
    sp.check_product(expected_number=1, expected_name=product_name, expected_price=product_price)
    sp.check_result_count_values()
    sp.open_product_page()

    pp = ProductPage(driver)
    pp.product_page_is_opened()
    pp.check_product_information(expected_sku=product_sku_number, expected_name=product_name,
                                 expected_price=product_price)
    pp.add_product_to_cart()
    pp.assert_product_was_added_to_cart(expected_name=product_name, expected_price=product_price, expected_quantity="1")
    pp.open_cart()

    cp = CartPage(driver)
    cp.cart_page_is_opened()
    cp.check_item_in_cart_information(expected_name=product_name, expected_price=product_price, expected_quantity="1",
                                      expected_subtotal=product_price)
    cp.open_checkout_page()

    chp = CheckoutPage(driver)
    chp.checkout_page_is_opened()
    chp.login_into_account(name=user_data["user_email"], password=user_data["user_password"])
    chp.check_billing_details_autocomplete_after_login(exp_firstname=user_data["user_firstname"],
                                                       exp_lastname=user_data["user_lastname"],
                                                       exp_id_number=user_data["user_id_number"],
                                                       exp_town=user_data["user_town"],
                                                       exp_user_address=user_data["user_address"],
                                                       exp_user_phone=user_data["user_phone"],
                                                       exp_user_email=user_data["user_email"])
    chp.check_cart_icon_status_information(expected_quantity="1", expected_price=product_price)
    chp.check_order_details(expected_name=product_name, expected_quantity="1", expected_price=product_price)
