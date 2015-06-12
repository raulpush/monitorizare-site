#h:\sourse\python\behave.example-master\features>behave site.feature
@tags @tag
Feature: testing www.artmatch.net

  Scenario: visit artmatch and check title
    When we visit "http://www.artmatch.net/ro"
    Then it should have a title "Art Match"

  Scenario: visit artmatch and search for an unknown object
    When we visit "http://www.artmatch.net/ro"
    Then we fill the field by id "edit-search-block-form--2" with text "xxxyyy"
    Then we click on button with class "btn-warning"
    Then we should see "nu a generat nici un rezultat"

  Scenario: visit artmatch and search for an known object
    When we visit "http://www.artmatch.net/ro"
    Then we fill the field by id "edit-search-block-form--2" with text "mobila"
    Then we click on button with class "btn-warning"
    Then we should see "Rezultatele cautarii"