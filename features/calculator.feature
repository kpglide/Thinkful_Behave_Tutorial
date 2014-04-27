Feature: Confirming that the tip calculator form works

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

	Scenario: check that the form submits successfully
		When I go to the tip calculator
		And I submit the form with a valid total and tip percentage
		Then I should see the results page

	Scenario: check that the calculator correctly calculates the tip
		When I enter a meal cost of $50 and a tip percentage of 20%
		Then I should see a tip amount of $10 displayed on the results page

	Scenario: check that the calculator catches entry of a negative tip amount
		When I enter a negative tip amount
		Then the app should display an error message
		And return the calculator form

	Scenario: check that the calculator catches entry of non-integer meal cost
		When I enter a non integer for meal cost
		Then the app should display an error message
		And return the calculator form

	Scenario: check that the calculator catches entry of non-integer tip percentage
		When I enter a non integer for tip percentage
		Then the app should display an error message
		And return the calculator form