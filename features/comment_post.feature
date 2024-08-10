Feature: Comment on a post

  Scenario: User comments on a post
    Given I am viewing the post titled "My First Post"
    When I submit a comment "Great post!"
    Then the comment should be visible under the post
