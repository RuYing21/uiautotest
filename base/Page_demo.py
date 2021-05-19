from base.Browser import *


class PageDemo():

    url =  None
    driver = None

    def element(self, loc: tuple):
        """
        寻找元素的方法

        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)

    def elements(self, loc: tuple):
        """
        定位一组元素或多个元素

        :param loc:
        :return:
        """
        return self.driver.find_elements(*loc)


class CommonLogin(PageDemo):

    url = ''
    driver = Chrome.browser
    username =('id','eid')
    password = ('id', ''),
    yuchooseBtn = ('id', ''),
    loginBtn = ('id', '')

    def get(self):
        """
        打开地址
        :return:
        """
        self.driver.get(self.url)

    def login(self, username: str = 'hr003',password: str = ''):
        self.element(self.username).send_key(username)
        self.element(self.password).send_key(password)
        self.element(self.yuchooseBtn).click
        self.element(self.loginBtn).click


class Change(CommonLogin):

    changeBtn = ('id','')
    changeInput = ('id', 'loginInput')
    confirm = ('id', '')
    module_lable = ('id', '')

    def change(self, module: str = '11744'):
        self.element(self.changeInput).send_key(module)
        self.element(self.confirm).click()


class TestChange(Change):

    def test_login(self):
        self.get()
        self.login()
        assert self.element(self.username).text == 'hr003'

    def test_change(self):
        self.change()
        assert self.element(self.module_lable) == '11744'


obj = TestChange()
obj.test_login()
obj.test_change()