__author__ = 'andrei.muresan'
from behave import when, then
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


@then('custom ariesul - we click on search button')
def step5(context):
    context.btn = context.browser.find_
    context.btn.click()
