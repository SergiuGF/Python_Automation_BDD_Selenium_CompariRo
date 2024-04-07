Confirguration steps:
- instalam Google Chrome 
https://www.google.com/chrome/what-you-make-of-it/
    - juct click next



For Selenium project:
- install Pycharm - Atention!!! - Community Edition -https://www.jetbrains.com/pycharm/download/?section=windows
    - when install check "Update PATH Variable" and 'Create Association .py' 

- install python  https://www.python.org/downloads/
	- just click next

- add Python to environment variables PATH
    - click on Windows search bar and write 'environment variables' 
        - should look something like that: 
            (C:\Users\vboxuser\AppData\Local\Programs\Python\Python312) and
            (C:\Users\vboxuser\AppData\Local\Programs\Python\Python312\Scripts)

- download project from https://github.com/SergiuGF/Python_Automation_BDD_Selenium_CompariRo

- open project in Pycharm 
    - write the following commands in the terminal:
        - pip install selenium
        - pip install webdriver_manager
        - pip install behave-html-formatter
    - install Gherkin plugin
    - for run the test write the following commands in the terminal:
        - behave -f html -o all-tests.html - to run all tests
        - behave --tags=scenario_tag_name -f html -o scenario_tag_name.html –  - to run just on test (selected by tag "ex. @Login1")



For Cypress project:
- install VS Code (https://code.visualstudio.com/)
    - just click next
- instal Node.js (https://nodejs.org/en/download)
    - when install check Automatically install the neccesary tools
- download project from https://github.com/SergiuGF/Automation_BDD_Cypress_CompariRo.git
- open project in VSCode
    - install Cucumber extension
    - write the following commands in the terminal:
        - npm init
        - npm install cypress
        - npm install --save-dev cypress-cucumber-preprocessor
        - npm install @cucumber/cucumber
        - npm i --save-dev cypress-mochawesome-reporter
    - for run the test write the following commands in the terminal:    
        - npx cypress run - to run all tests
        - npx cypress run --browser chrome  - to run all tests in Chrome
        - npx cypress run --headed --browser chrome  -  to run all tests in Chrome in headed mode
        - npx cypress run --spec test_path - to run just one test file 
        - npx cypress open - to run tests in headed mode