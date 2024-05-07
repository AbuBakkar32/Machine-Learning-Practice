from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number


@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0


@then("verify the logo on the page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then verify the logo on the page')


@given("launch the chrome browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given launch the chrome browser')


@when("open the OrangeHRM Home Page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When open the OrangeHRM Home Page')