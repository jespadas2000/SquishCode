Feature: Close the program

  Scenario: Prepare EcosimPro/PROOSIS to finish the tests and leave everything as in the initial state.

		Given the attachment of the program in Squish
 	    And the deletion of the tmp directory with the aim of emptying the previous contents
 	    Then close the program

