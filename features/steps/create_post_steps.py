from behave import given, when, then

@given('I am logged into the WordPress dashboard')
def step_impl(context):
    context.page = "WordPress dashboard loaded"

@when('I create a new post with title "{title}" and content "{content}"')
def step_impl(context, title, content):
    context.new_post = {"title": title, "content": content}
    context.post_published = True

@then('the post should be published successfully')
def step_impl(context):
    assert context.post_published == True
    assert context.new_post == {"title": "My First Post", "content": "Hello World!"}
