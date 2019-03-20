Feature: The Women tab 

  Scenario: User can navigate to Women page

    Given I have navigated to the main page
     When I click on the WOMEN button
     Then The page titled "Women - My Store" has loaded

@test
  Scenario: User can navigate to Women/Tops page

    Given I have navigated to the main page
     When I hover over the WOMEN button
      And I click on the TOPS header
     Then The page titled "Tops - My Store" has loaded

