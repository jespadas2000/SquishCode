Feature: Correct launch of the Qt deck

    Scenario: Launch program to be tested in Squish

        Given the program is launched
 		And the program is ready for testing
 		And the deletion of the tmp directory with the aim of emptying the previous contents
 	    And the creation of a new tmp directory
 	    And the creation of a new info path directory
