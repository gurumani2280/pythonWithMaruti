class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url