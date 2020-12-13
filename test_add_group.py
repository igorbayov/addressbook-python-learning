from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group


class TestAddGroup():
    def setup_method(self, method):
        self.wd = webdriver.Firefox()
        self.wd.maximize_window()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        self.wd.find_element(By.NAME, "user").click()
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").click()
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def open_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def return_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, group):
        self.open_groups_page()
        self.wd.find_element(By.NAME, "new").click()
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").click()
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").click()
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.wd.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        self.wd.find_element(By.NAME, "submit").click()
        self.return_groups_page()

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="Group name", header="Header value", footer="Footer value"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def teardown_method(self, method):
        self.wd.quit()
