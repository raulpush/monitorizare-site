from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@when('we visit "{site}"')
def step(context, site):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(3)
    context.browser.get(site)


@then('it should have a title "{title}"')
def step(context, title):
    assert title in context.browser.title

@then('we click on button with class "{elem}"')
def step(context, elem):
    context.btn = context.browser.find_element_by_class_name(elem)
    context.btn.click()

@then('we click on button with id "{elem}"')
def step(context, elem):
    context.btn = context.browser.find_element_by_id(elem)
    context.btn.click()

@then('we click on button with name "{elem}"')
def step(context, elem):
    context.btn = context.browser.find_element_by_name(elem)
    context.btn.click()

@then('we fill the field by id "{elem}" with text "{text}"')
def step(context, elem, text):
    context.elem = context.browser.find_element_by_id(elem)
    context.elem.send_keys(text)

@then('we fill the field by class "{elem}" with text "{text}"')
def step(context, elem, text):
    context.elem = context.browser.find_element_by_class_name(elem)
    context.elem.send_keys(text)

@then('we fill the field by name "{elem}" with text "{text}"')
def step(context, elem, text):
    context.elem = context.browser.find_element_by_name(elem)
    context.elem.send_keys(text)
    # context.elem.send_keys(text + Keys.RETURN)


@then('we should see "{text}"')
def step(context, text):
    src = context.browser.page_source
    assert text in src