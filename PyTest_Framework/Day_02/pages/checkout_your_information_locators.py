from selenium.webdriver.common.by import By

class CheckoutYourInformationLocators:
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.XPATH, "//input[@class='btn_primary cart_button']")