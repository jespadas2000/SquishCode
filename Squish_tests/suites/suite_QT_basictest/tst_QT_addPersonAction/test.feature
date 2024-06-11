Feature: Test the add person action

    Scenario: Add a new person

    	Given the attachment of the program in Squish

		Then open the new person dialog

		When 'Tomas' has been written in the name parameter
	    And 'Martin' has been written in the surname parameter
	    And '27' has been written in the age parameter
	    And 'Male' has been written in the sex parameter
	    And 'No parent' has been written in the parent parameter
	    Then the ok button is pressed
	    And 'Tomas Martin' with age '27' sex 'M' and 'No parent' as parent

	Scenario: Add a new person with a parent

    	Given the attachment of the program in Squish

		Then open the new person dialog

		When 'Victor' has been written in the name parameter
	    And 'Martin' has been written in the surname parameter
	    And '2' has been written in the age parameter
	    And 'Male' has been written in the sex parameter
	    And 'Tomas Martin' has been written in the parent parameter
	    Then the ok button is pressed
	    And 'Tomas Martin>Victor Martin' with age '2' sex 'M' and 'Tomas Martin' as parent

	Scenario: Try to add a person with the same name

	    Given the attachment of the program in Squish

		Then open the new person dialog

		When 'Victor' has been written in the name parameter
	    And 'Martin' has been written in the surname parameter
	    And '2' has been written in the age parameter
	    And 'Male' has been written in the sex parameter
	    And 'Tomas Martin' has been written in the parent parameter
	    Then the ok button is pressed
	    And a QMessage appears
	    And the cancel button is pressed

    Scenario: Try to add a person with a parent with less age

	    Given the attachment of the program in Squish

		Then open the new person dialog

		When 'Ramon' has been written in the name parameter
	    And 'Samuel' has been written in the surname parameter
	    And '56' has been written in the age parameter
	    And 'Male' has been written in the sex parameter
	    And 'Tomas Martin' has been written in the parent parameter
	    Then the ok button is pressed
	    And a QMessage appears
	    And the cancel button is pressed