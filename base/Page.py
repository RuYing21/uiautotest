from base.Browser import Chrome


class Page:

    url = None
    locator = {}
    browser = Chrome

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browser

    def __getattr__(self, loc):
        """
        判断函数属性是否是定位器的键
        :param loc:
        :return:
        """
        if loc not in self.locator.keys():
            raise Exception

        by, val = self.locator[loc]

        return self.driver.find_element(by, val)


class CommonLoginPage(Page):
    url = 'www.baidu.com'
    locator = {
        'username': ('id', 'kw'),
        'password': ('id', ''),
        'yuchooseBtn':('id',''),
        'loginBtn':('id','')

    }

    def get(self):
        """
        打开页面
        :return:
        """
        return self.driver.get(self.url)

    def login(self, username: str = 'hr003', password: str = ''):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.yuchooseBtn.click()
        self.loginBtn.click()


class BusinessPage(CommonLoginPage):
    CommonLoginPage.locator.update({
        'changeBtn': ('id', 'kw'),
        'input': ('id', ''),
        'confim': ('id', '')
    })

    def change_module(self, module_id: str = '11744'):
        self.locator.click()
        self.input.send_key(input)
        self.confirm.click()


class TestBussinessPage():
    def test_login(self):
        page = BusinessPage()
        page.get()
        page.login()
        assert page.user_name.text == 'hr003'
        print('login success')
        page.driver.quit()

    def test_change_module(self):
        page = BusinessPage()
        page.get()
        page.login()
        assert page.user_name.text == 'hr003'
        print('login success')
        page.driver.quit()


if __name__ == '__main__':
    obj = TestBussinessPage()
    obj.test_login()
    obj.test_change_module()
