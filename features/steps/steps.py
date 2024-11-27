from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_element_by_placeholder(context, placeholder):
    return context.browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{placeholder}"]')

def get_element_by_text(context, text):
    return context.browser.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")


@given('Eu estou na página inicial "{url}"')
def step_open_home_page(context, url):
    context.browser = webdriver.Chrome()
    context.browser.get(url)

@when('Eu espero que o overlay de carregamento desapareça')
def step_wait_for_overlay_to_disappear(context):
    WebDriverWait(context.browser, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay"))
    )

@when('Eu clico no campo "{field}"')
def step_click_field(context, field):
    element = get_element_by_placeholder(context, field)
    element.click()

@when('Eu insiro "{value}" no campo "{field}"')
def step_insert_into_field(context, value, field):
    element = get_element_by_placeholder(context, field)
    element.send_keys(value)

@when('Eu clico no botão "{button}"')
def step_click_button(context, button):
    element = get_element_by_text(context, button)
    element.click()

@then('Eu vejo a mensagem "{message}"')
def step_see_message(context, message):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), message)
    )

# Finalizar o browser após o cenário
def after_scenario(context, scenario):
    context.browser.quit()
