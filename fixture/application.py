from selenium import webdriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path="C:/selenium_chromedriver_win32/chromedriver.exe")
        self.wd.maximize_window()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.wd
        wd.quit()
