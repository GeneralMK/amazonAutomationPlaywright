Feature: Amazon Product Shopping

Scenario: Search for a product, add to cart, view cart, and increase quantity

  Given I am on the Amazon homepage
  When I search for "Laptop Stand"
  Then I click the "Amazon Basics Laptop Stand Riser" product to view it and add to my cart 
  Then I increase the quantity to "2"