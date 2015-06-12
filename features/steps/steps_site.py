from lettuce import *
from selenium import webdriver

@after.each_feature
def teardown_some_feature(feature):
    world.browser.quit()

@step('we visit "(.*)"')
def step1(step, site):
    world.browser = webdriver.Firefox()
    world.browser.implicitly_wait(3)
    world.browser.get(site)


@step('it should have a title "(.*)"')
def step2(step, title):
    assert title in world.browser.title

@step('we click on button with class "(.*)"')
def step3(step, elem):
    world.btn = world.browser.find_element_by_class_name(elem)
    world.btn.click()

@step('we click on button with id "(.*)"')
def step4(step, elem):
    world.btn = world.browser.find_element_by_id(elem)
    world.btn.click()

@step('we click on button with name "(.*)"')
def step5(step, elem):
    world.btn = world.browser.find_element_by_name(elem)
    world.btn.click()

@step('we fill the field by id "(.*)" with text "(.*)"')
def step6(step, elem, text):
    world.elem = world.browser.find_element_by_id(elem)
    world.elem.send_keys(text)

@step('we fill the field by class "(.*)" with text "(.*)"')
def step7(step, elem, text):
    world.elem = world.browser.find_element_by_class_name(elem)
    world.elem.send_keys(text)

@step('we fill the field by name "(.*)" with text "(.*)"')
def step8(step, elem, text):
    world.elem = world.browser.find_element_by_name(elem)
    world.elem.send_keys(text)
    # world.elem.send_keys(text + Keys.RETURN)


@step('we should see "(.*)"')
def step9(step, text):
    src = world.browser.page_source
    assert text in src