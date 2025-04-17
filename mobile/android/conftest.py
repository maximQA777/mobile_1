
import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
import os
from mobile.android.config import config
import utils
from appium import webdriver


def init_app_session(options):
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'https://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )


def tear_down_session():
    utils.attach.attach_screenshot(browser)
    utils.attach.attach_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)


@pytest.fixture(scope='function')
def android_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # 'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',

        # Set URL of the application under test
        'app': config.app,
        "appWaitActivity": "org.wikipedia.*",

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': config.user_Name,
            'accessKey': config.access_Api,
        }
    })

    init_app_session(options)
    yield
    tear_down_session()

@pytest.fixture(scope='function')
def ios_management():
    options = XCUITestOptions().load_capabilities({
        # Set URL of the application under test
        "app": "bs://sample.app",

        # Specify device and os_version for testing
        "deviceName": "iPhone 11",
        "platformName": "ios",
        "platformVersion": "13",

        # Set other BrowserStack capabilities
        "bstack:options": {
            "userName": config.bstack_userName,
            "accessKey": config.bstack_accessKey,
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test"
        }
    })

    init_app_session(options)
    yield
    tear_down_session()