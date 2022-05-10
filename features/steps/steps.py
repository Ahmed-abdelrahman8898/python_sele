from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@given(u'mememe')
def step_impl(context):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver=webdriver.Chrome (r"C:\Users\ahmedhussienalwany.a\Documents\techem\chromedriver.exe")
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(10000)


@when(u'momomom')
def step_impl(context):
    assert 2==2


@then(u'tototototo')
def step_impl(context):
    pass


@given(u'ttttttttttttttttttttt "{tot}" "{user}"')
def step_impl(context,tot,user):
    pass


@when(u'sssssssssssssssss')
def step_impl(context):
    pass


@then(u'cccccccccccccccccc')
def step_impl(context):
    assert 2==3