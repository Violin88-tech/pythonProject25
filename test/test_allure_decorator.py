import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Viktoria Islentyeva")
@allure.feature("Issues")
@allure.story("Searching issues")
def test_selene(open_browser):
    open()
    search()
    go()
    open_issue()
    found()


@allure.step("Open general window")
def open():
    browser.open('/')


@allure.step("Find repository")
def search():
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("allure-framework/allure2")
    browser.element("#query-builder-test").submit()


@allure.step("Go to repository")
def go():
    browser.element(by.link_text("allure-framework/allure2")).click()


@allure.step("Open repository")
def open_issue():
    browser.element("#issues-tab").click()


@allure.step("Find to Issue")
def found():
    browser.element(by.partial_text("#1")).should(be.visible)
