"""
浏览器三个必要的属性：
1. 浏览器类型  chrome firefox ie
2. 浏览器的启动参数 无头化  最大化 尺寸化
3. 浏览器的属性：显示尺寸，隐式等待、页面加载、js执行时间
"""
from selenium.webdriver import *
from typing import Type,Union
from time import sleep


class BrowserTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return 'unsupport browser type : {self._type}'


class Browser:
    CHROME_DRIVER_PATH = '../driver/chromedriver.exe'
    FIREFFOX_DRIVER_PATH = '../driver/geckodriver.exe'
    IE_DRIVER_PATH = '../driver/iedriver.exe'
    EDGE_DRIVER_PATH = '../driver/edgedriver.exe'
    IE_DRIVER_PATH = '../driver/IEDdriverServer.exe'
    OPERA_DRIVER_PATH = '../driver/opera_driver.exe'

    WINOWS_SIZE = (1024, 768)

    TMP_TIME = 30  # 隐式等待时间

    PAGE_LOAD_TIME = 20  # 页面加载时间

    SCRIPT_TIME_OUT = 20   # js执行超时时间

    HEADLESS = True   # 默认浏览器无头启动

    def __init__(self, browser_type: Type[Union[Firefox, Chrome, Ie, Edge, Opera, Safari]] = Chrome,
                 option_type: Type[Union[FirefoxOptions, ChromeOptions, IeOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH ):
        """
        浏览器三个必要的参数
        :param browser_type:
        :param option_type:
        :param driver_path:
        """
        # if not issubclass(browser_type, (Firefox, Chrome, Ie, Edge, Opera, Safari)):
        #     raise BrowserTypeError(browser_type)
        #
        # if not issubclass(option_type, (FirefoxOptions, ChromeOptions, IeOptions)):
        #     raise BrowserTypeError(option_type)

        # if not issubclass(driver_path, str):
        #     raise TypeError

        self._path = driver_path
        self._browser = browser_type
        self._option = option_type

    @property
    def options(self):
        """
        浏览器特定的操作，在子类中实现
        :return:
        """
        return

    @property
    def browser(self):
        """
        启动浏览器，返回浏览器实例
        :return:
        """
        return


class Chrome(Browser):
    WINOWS_SIZE = (1920, 900)

    TMP_TIME = 30  # 隐式等待时间

    PAGE_LOAD_TIME = 30  # 页面加载时间

    SCRIPT_TIME_OUT = 30  # js执行超时时间

    HEADLESS = False  # 默认浏览器无头启动

    START_MAX = '--start-maximized'

    EXP = {
        # 关闭chrome正在受到自动化。。。。的提示
        'excludeSwitches':['enable-automtion']
        # 移动模拟  可做h5测试
        # 'mobileEmulation':{'deviceName':'iPhone6'}
    }


    @property
    def options(self):
        chrome_option = self._option()
        chrome_option.add_argument(self.START_MAX)  #最大化启动
        # 添加 EXP参数
        for k,v in self.EXP.items():
            chrome_option.add_experimental_option(k, v)
        chrome_option.headless = self.HEADLESS
        return chrome_option

    @property
    def browser(self):
        # 启动chrome  带有启动参数
        chrome = self._browser(self._path, options=self.options)
        # 设置浏览器
        chrome.implicitly_wait(self.TMP_TIME)
        chrome.set_script_timeout(self.SCRIPT_TIME_OUT)
        chrome.set_page_load_timeout(self.SCRIPT_TIME_OUT)
        chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
        chrome.set_window_size(*self.WINOWS_SIZE)

        return chrome


class IE(Browser):
    CLEAN_SESSION = True

    def __init__(self):
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH
        )

    @property
    def options(self):
        ie_option = self._option()
        ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        # 启动ie  带有启动参数
        ie = self._browser(self._path, options=self.options)
        # 设置浏览器
        ie.implicitly_wait(self.TMP_TIME)
        ie.set_script_timeout(self.SCRIPT_TIME_OUT)
        ie.set_page_load_timeout(self.SCRIPT_TIME_OUT)
        ie.set_page_load_timeout(self.PAGE_LOAD_TIME)
        ie.maximize_window()

        return ie


if __name__ == '__main__':
    with Chrome().browser as _chrome:
        _chrome.get("https://www.baidu.com/")
        sleep(3)
