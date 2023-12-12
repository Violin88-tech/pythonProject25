
from selene.support import by
from selene import browser, by, be
from selene.support.shared import browser



def test_selene():
    browser.open("https://github.com")

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("allure-framework/allure2")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("allure-framework/allure2")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#2242")).should(be.visible)

