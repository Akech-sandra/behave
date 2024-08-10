from behave import given, when, then

@given('I am viewing the post titled "{title}"')
def step_impl(context, title):
    context.post_title = title

@when('I submit a comment "{comment}"')
def step_impl(context, comment):
    context.comment = comment
    context.comment_posted = True

@then('the comment should be visible under the post')
def step_impl(context):
    assert context.comment_posted == True
    assert context.comment == "Great post!"
