Feature: Correct launch of the Excel deck

    Scenario: Launch program to be tested in Squish

        Given the program is launched

        When the doc is open

        Then select the EcosimPro tab
        And open the model
        And add report sheet
    	And create the sheet report with h parameter
		And play the model

		When the recommended graph options is selected
		And create the default graph
		Then the graph is correctly created

		Then the '215' data values of the column '1' are the same that in 'TIME(s)_BouncingBall_excelDeck.txt'
		And the '215' data values of the column '2' are the same that in 'h_BouncingBall_excelDeck.txt'