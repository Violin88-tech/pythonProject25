import allure
from selene.support import by
from selene import browser, by, be
from selene.support.shared import browser


def test_selene():
    with allure.step("Open general window"):
        browser.open('/')

    with allure.step("Find repository"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("allure-framework/allure2")
        browser.element("#query-builder-test").submit()

    with allure.step("Go to repository"):
        browser.element(by.link_text("allure-framework/allure2")).click()

    with allure.step("Open repository"):
        browser.element("#issues-tab").click()

    with allure.step("Find to Issue"):
        browser.element(by.partial_text("#2242")).should(be.visible)
