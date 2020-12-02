Feature: Search product & country in personalisation

 Scenario Outline: User should be able to search I want to export products in country

    Given User is on home page
      When User searches for product to export <products>
      Then User searches for country to sell in <country> for already selected <products>
        Examples: Products and Countries
         | products                 | country   |
         | Vehicle                  | Germany |
         | Leather                  | Poland |
#   Then User should be on the - Search results page