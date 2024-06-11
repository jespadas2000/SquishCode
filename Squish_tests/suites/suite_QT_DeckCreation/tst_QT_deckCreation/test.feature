Feature: Correct creation of decks


    Scenario: Set all configurations

		Given the attachment of the program in Squish

		When the library 'DEFAULT_LIB' is selected

		Then the file tree is visible

	Scenario: Creation of the GUI deck

	    Given the attachment of the program in Squish

		When the tab 'item' is selected
		And the action 'Compile' in the file 'bouncingBall>default2>exp1' is selected
		And the action 'Simulate' in the file 'bouncingBall>default2>exp1' is selected
		And the action 'New Deck ...' in the file 'bouncingBall>default2>exp1' is selected

		Then the type of the deck 'deck1' is 'Deck GUI Program'
		And the name of the deck is 'Deck_GUI'

		When the tab 'Variable Selection' is selected in deck creator
		Then the variable 'h' is 'Deck-In'
		And the variable 'h' is 'Deck-Out'
		And press the Generate button
		And press the Finish button

	Scenario: Creation of the xml deck

	    Given the attachment of the program in Squish

	    When the action 'New Deck ...' in the file 'bouncingBall>default2>exp1' is selected

		Then the type of the deck 'deck2' is 'Deck Binary + MS Excel Spreadsheet + EA Toolbar Installer'
		And the name of the deck is 'Deck_Excell'

		When the tab 'Variable Selection' is selected in deck creator
		Then the variable 'h' is 'Deck-In'
		And the variable 'h' is 'Deck-Out'
		And press the Generate button
		And press the Finish button