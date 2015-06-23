Feature: testing www.electroserv.net

  Scenario: visit electroserv and check the link and icons of http://www.fonduri-ue.ro/
    When we visit "http://electroserv-ariesul.com/"
    Then we should see "www.fonduri-ue.ro"
    Then we should find a hyperlink "www.fonduri-ue.ro" and click
    Then wait until element by id "ja-wrapper" is visible
    Then new site is opening with title "Ministerul Fondurilor Europene"


  Scenario: visit electroserv e-commerce and login
    When we visit "http://www.electroserv-ariesul.com/ecommerce/login/"
    Then we fill the field by name "email" with text "raulpush@yahoo.com"
    Then we fill the field by name "password" with text "test1234"
    Then we click on button with name "bsubmit"
    Then wait until element by id "basketDiv" is visible
    Then we should see "Ilie"

#  Scenario: visit electroserv and search for an unknown object
#    When we visit "http://www.electroserv-ariesul.com/ecommerce"
#    Then we fill the field by class "text-box" with text "xxxyyy"
#    Then custom ariesul - we click on search button
#    Then wait until element by id "contentDiv" is visible
#    Then we should see "Nu exista nici un produs"
