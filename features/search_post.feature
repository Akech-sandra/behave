Feature: Search for a post

  Scenario: Search for an existing post
    Given I am on the WordPress homepage
    When I search for the post titled "My First Post"
    Then I should see the post in the search results
