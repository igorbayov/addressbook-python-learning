from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddGroup():
    def setup_method(self, method):
        self.wd = webdriver.Firefox()
        self.wd.maximize_window()
        self.open_home_page()

    def teardown_method(self, method):
        self.wd.quit()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.wd.find_element(By.NAME, "user").click()
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").click()
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def open_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, name, header, footer):
        self.wd.find_element(By.NAME, "new").click()
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(name)
        self.wd.find_element(By.NAME, "group_header").click()
        self.wd.find_element(By.NAME, "group_header").send_keys(header)
        self.wd.find_element(By.NAME, "group_footer").click()
        self.wd.find_element(By.NAME, "group_footer").send_keys(footer)
        self.wd.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        self.wd.find_element(By.NAME, "submit").click()

    def return_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group("First group name", "Header value for first group", "Footer value for first group")
        self.return_groups_page()
        self.logout()










