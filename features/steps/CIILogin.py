# first to run the test with behave and second to see the reports in allure
# behave -f allure_behave.formatter:AllureFormatter -o reports/ ./PythonBehaveBdd/features
# allure serve reports/

from behave import *
from PythonBehaveBdd.features.pages.home import *
from PythonBehaveBdd.features.pages.login import *
from PythonBehaveBdd.features.pages.dashboard import *


@given("I am at the CII page")
def step(context):
    clickelement(context)


@given("I am ozgur")
def step(context):
    print('this is ozgur')


@when("I login with my {pin} and {password}")
def step(context, pin, password):
    login(context, pin, password)


@then("I should see my PIN on the dashboard")
def step(context):
    checkDashboardPin(context)




