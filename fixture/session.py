class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login_name, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, login_name):
        return self.get_logged_user() == login_name

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("/html/body/div/div[1]/form/b").text[1:-1]

    def ensure_login(self, login_name, password):
        if self.is_logged_in():
            if self.is_logged_in_as(login_name):
                return
            else:
                self.logout()
        self.login(login_name, password)