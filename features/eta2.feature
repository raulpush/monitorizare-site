#h:\sourse\python\behave.example-master\features>behave site.feature
@tags @tag
Feature: testing www.magazin.eta2u.ro.net

  Scenario: visit eta2 b2b  and check title
    When we visit "http://magazin.eta2u.ro/users/login"
    Then it should have a title "Login"

  Scenario: visit eta2 b2b and check title
    When we visit "http://magazin.eta2u.ro/users/login"
    Then we should see "www.fonduri-ue.ro"
    Then we should find a hyperlink "www.fonduri-ue.ro" and click
    Then wait until element by id "ja-wrapper" is visible
    Then new site is opening with title "Ministerul Fondurilor Europene"

#  Scenario: visit artmatch and search for an unknown object
#    When we visit "http://www.artmatch.net/ro"
#    Then we fill the field by id "edit-search-block-form--2" with text "xxxyyy"
#    Then we click on button with class "btn-warning"
#    Then we should see "nu a generat nici un rezultat"
#
#  Scenario: visit artmatch and search for an known object
#    When we visit "http://www.artmatch.net/ro"
#    Then we fill the field by id "edit-search-block-form--2" with text "mobila"
#    Then we click on button with class "btn-warning"
#    Then we should see "Rezultatele cautarii"