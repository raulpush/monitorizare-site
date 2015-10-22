from behave import when, then, given
import converter
from hamcrest import assert_that, has_items

@given('"{file}" as input file')
def read_input(context, file):
    context.sourceFile = file
    context.source=converter.line(file)
    assert_that(len(context.source)>0)

@given('"{file}" as comparison file')
def read_compare(context, file):
    context.compare=converter.line(file)
    context.compareFile=file
    assert_that(len(context.compare)>0)

@when('call ValidationTool')
def  execute(context):
    context.myExecution={}


@then('a new file is created "{file}"')
def step1(context, file):
    context.result=converter.line(file)
    context.resultFile=file
    assert_that(len(context.result)>0)


@then('we have new specific headers "{mylist}"')
def step1(context, mylist):
    list = mylist.split(",")
    assert_that(len(list)>0)
    for it in list:
        assert_that(len(context.compare["1"][it])>0)