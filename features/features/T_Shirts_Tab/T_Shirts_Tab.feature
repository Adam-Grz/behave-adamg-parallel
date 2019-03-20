Feature: The T-Shirts tab 

  Scenario: User can navigate to T-Shirts page

    Given I have navigated to the main page
     When I click on the T_SHIRTS button
     Then The page titled "T-shirts - My Store" has loaded


  Scenario: User can navigate to Faded T-Shirt page

    Given I have navigated to the main page
     When I click on the T_SHIRTS button
     Then The page titled "T-shirts - My Store" has loaded
     When I click on the FADED T_SHIRT button
     Then The page titled "Faded Short Sleeve T-shirts - My Store" has loaded
