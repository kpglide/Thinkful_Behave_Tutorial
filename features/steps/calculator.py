@when(u'I go to the tip calculator')
def step_impl(context):
	context.browser.get('http://localhost:5000')

@then(u'I should see the calculator form')
def step_impl(context):
	assert context.browser.title == "Tip Calculator"

@when(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("30")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("20")
	br.find_element_by_id("submit").click()

@then(u'I should see the results page')
def step_impl(context):
	br = context.browser
	assert br.find_element_by_id('results')	

@when(u'I enter a meal cost of $50 and a tip percentage of 20%')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("50")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("20")
	br.find_element_by_id("submit").click()

@then(u'I should see a tip amount of $10 displayed on the results page')
def step_impl(context):
	br = context.browser
	result = br.find_element_by_id("results")
	assert result == 10.0

@when(u'I enter a negative tip amount')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("50")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("-1")
	br.find_element_by_id("submit").click()

@then(u'the app should display an error message')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id("error_message")

@then(u'return the calculator form')
def step_impl(context):
	assert context.browser.title == "Tip Calculator"

@when(u'I enter a non integer for meal cost')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("kevin")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("10")
	br.find_element_by_id("submit").click()

	context.execute_steps(u'''
		then the app should display an error message
		and return the calculator form
		''')

@when(u'I enter a non integer for tip percentage')
def step_impl(context):
	br = context.browser
	br.get('http://localhost:5000')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("50")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("kevin")
	br.find_element_by_id("submit").click()

	context.execute_steps(u'''
		then the app should display an error message
		and return the calculator form
		''')
