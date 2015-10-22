Feature: testing file csv1


  Scenario: create processed csv file
    Given "Ebola.csv" as input file
    Given "result_Processed_Ebola.csv" as comparison file
    When call ValidationTool
    Then a new file is created "1445437249_Processed_Ebola.csv"
    Then we have new specific headers "event,source_URL,disease,pathogen"
