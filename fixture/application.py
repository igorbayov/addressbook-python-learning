from selenium import webdriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path="C:/selenium_chromedriver_win32/chromedriver.exe")
        self.wd.maximize_window()
        # self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url # Any questions are interesting here, so do not put parentheses
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.wd
        wd.quit()
