Feature: The results of the deck are correct


    Scenario: Set all configurations

		Given the attachment of the program in Squish

		When no custom deck is created

		Then create a new custom deck
		And the h input is set to '13'

	Scenario: Corret output of the deck

	    Given the attachment of the program in Squish

	    When the deck is play
	    And the deck finish

	    Then the output data is the same of the file 'BouncingBall_guiDeck.txt'