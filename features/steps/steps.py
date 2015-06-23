from behave import when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

@when('we visit "{site}"')
def step1(context, site):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(3)
    context.browser.get(site)


@then('it should have a title "{title}"')
def step2(context, title):
    assert title in context.browser.title

@then('new site is opening with title "{title}"')
def step3(context, title):
    assert title in context.browser.title

@then('we click on button with class "{elem}"')
def step4(context, elem):
    context.btn = context.browser.find_element_by_class_name(elem)
    context.btn.click()

@then('we click on button with id "{elem}"')
def step5(context, elem):
    context.btn = context.browser.find_element_by_id(elem)
    context.btn.click()

@then('we click on button with name "{elem}"')
def step6(context, elem):
    context.btn = context.browser.find_element_by_name(elem)
    context.btn.click()

@then('we should find a hyperlink "{link}" and click')
def step7(context, link):
    context.link = context.browser.find_element_by_link_text(link)
    assert context.link
    context.link.click()

@then('we fill the field by id "{elem}" with text "{text}"')
def step8(context, elem, text):
    context.elem = context.browser.find_element_by_id(elem)
    context.elem.send_keys(text)

@then('wait until element by id "{elem}" is visible')
def step8(context, elem):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, elem))
    )

@then('we fill the field by class "{elem}" with text "{text}"')
def step9(context, elem, text):
    context.elem = context.browser.find_element_by_class_name(elem)
    context.elem.send_keys(text)

@then('we fill the field by class "{elem}" with text "{text}" and enter')
def step9(context, elem, text):
    context.elem = context.browser.find_element_by_class_name(elem)
    context.elem.send_keys(text + Keys.ENTER)

@then('we fill the field by name "{elem}" with text "{text}"')
def step10(context, elem, text):
    context.elem = context.browser.find_element_by_name(elem)
    context.elem.send_keys(text)


@then('we should see "{text}"')
def step11(context, text):
    src = context.browser.page_source
    assert text in src