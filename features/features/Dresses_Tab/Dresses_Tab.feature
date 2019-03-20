Feature: The Dresses tab 

@dress
  Scenario: User can navigate to Dresses page

    Given I have navigated to the main page
     When I click on the DRESSES button
     Then The page titled "Dresses - My Store" has loaded


  Scenario: User can navigate to Casual Dresses page
    Given I have navigated to the main page
     When I click on the DRESSES button
      And I click on the CASUAL_DRESSES button
     Then The page titled "Casual Dresses - My Store" has loaded

  Scenario: User can navigate to Evening Dresses page
    Given I have navigated to the main page
     When I click on the DRESSES button
      And I click on the EVENING_DRESSES button
     Then The page titled "Evening Dresses - My Store" has loaded

