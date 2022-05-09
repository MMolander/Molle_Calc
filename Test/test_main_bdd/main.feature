Feature: Main UI for the calculator
    Scenario: User inputs the expression 1+1
      Given A calculator
      When A user inputs the expression 1+1
      Then The response should be 2

    Scenario: User inputs the expression 12+20
      Given A calculator
      When A user inputs the expression 12+20
      Then The response should be 32

    Scenario: User inputs expression 1.5+2.5
      Given A calculator
      When A user inputs the expression 1.5+2.5
      Then The response should be 4.0

    Scenario: User inputs expression 1/1
      Given A calculator
      When A user inputs the expression 1/1
      Then The response should be 1

    Scenario: User inputs expression 1/0
      Given A calculator
      When A user inputs the expression 1/0
      Then A zero division error should appear