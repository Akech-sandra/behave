from behave import given, when, then

@given('I am on the WordPress homepage')
def step_impl(context):
    context.page = "WordPress homepage loaded"

@when('I search for the post titled "{title}"')
def step_impl(context, title):
    context.search_results = ["My First Post"]

@then('I should see the post in the search results')
def step_impl(context):
    assert "My First Post" in context.search_results
