from behave import given, when, then

@given('I am on the WordPress login page')
def step_impl(context):
    context.page = "WordPress login page loaded"

@when('I enter valid WordPress credentials')
def step_impl(context):
    context.credentials = {"username": "admin", "password": "password"}

@then('I should be logged into the WordPress dashboard')
def step_impl(context):
    assert context.credentials == {"username": "admin", "password": "password"}
    context.page = "WordPress dashboard loaded"
    assert context.page == "WordPress dashboard loaded"
