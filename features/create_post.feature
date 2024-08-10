Feature: Create a post

  Scenario: User creates a new post
    Given I am logged into the WordPress dashboard
    When I create a new post with title "My First Post" and content "Hello World!"
    Then the post should be published successfully
