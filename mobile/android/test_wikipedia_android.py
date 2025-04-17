from time import sleep

from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search_and_click(android_management):
    with step('Поиск "Appium"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).should(be.visible)

    with step('Проверка найденных результатов'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with step('Открытие страницы "Appium"'):
        results.first.click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_page_title_text")).should(have.text('Appium'))