Feature: Test the add person dialog

    Scenario: Open the add person dialog

    	Given the attachment of the program in Squish
    	Then step test

		Then open the new person dialog

	Scenario: Press the addPerson button with incomplete information

	    Given the attachment of the program in Squish

	    Then the ok button is pressed
	    And a QMessage appears

	    When 'Maria' has been written in the name parameter
	    Then the ok button is pressed
	    And a QMessage appears

	    When 'Blanco' has been written in the surname parameter
	    Then the ok button is pressed
	    And a QMessage appears

	    When '65' has been written in the age parameter
	    Then the ok button is pressed
	    And a QMessage appears

	    When 'Woman' has been written in the sex parameter
	    Then the ok button is pressed
	    And 'Maria Blanco' with age '65' sex 'W' and 'No parent' as parent

	Scenario: Write the correct information

	    Given the attachment of the program in Squish

	    Then open the new person dialog

	    When '1234' has been written in the name parameter
	    Then the name parameter contains 'NO TEXT'

	    When '1234' has been written in the surname parameter
	    Then the surname parameter contains 'NO TEXT'

	    When 'abcd' has been written in the age parameter
	    Then the age parameter contains 'NO TEXT'

	    When '__a' has been written in the name parameter
	    Then the name parameter contains 'a'

	    When '__b' has been written in the surname parameter
	    Then the surname parameter contains 'b'

	    When '__1' has been written in the age parameter
	    Then the age parameter contains '1'

	    When '[]{}+*`^:.;,<>!$%&/()=?¿¡' has been written in the name parameter
	    Then the name parameter contains 'NO TEXT'

	    When '[]{}+*`^:.;,<>!$%&/()=?¿¡' has been written in the surname parameter
	    Then the surname parameter contains 'NO TEXT'

	    When '[]{}+*`^:.;,<>!$%&/()=?¿¡' has been written in the age parameter
	    Then the age parameter contains 'NO TEXT'

	    Then the cancel button is pressed