The framework represents a BDD (Behavior-Driven Development) testing plan for the price comparison platform, Compari.ro.

Language used: Python – ver. 3.11 | IDE: PyCharm ver. 2023.2

Libraries used:

PyCharm standard libraries (pre-installed);
Selenium ver. 4.14.0 (used for automating actions in a browser);
Webdriver-manager ver. 4.0.1 (used to facilitate automated management of drivers needed for Selenium);
Behave ver. 1.2.6. (BDD-specific library used for writing tests in natural language, along with Gherkin);
Behave-html-formatter ver. 0.9.10 (used for formatting behave.ini files into HTML files);
Gherkin Language (used for writing tests in natural language - alongside Behave - understandable to individuals without technical knowledge).
Methods used:

Random Module (imported from Python; provides functionalities for generating random numbers);
Re Module (imported from Python; provides functionalities for searching, manipulating, and processing text);
Sleep Function (imported from the Time module in Python; used to introduce a delay in the code execution for a specified period of time).
Installation and project execution:

Access the GitHub link related to the project;
Click the button "<> Code" and download by accessing the button "Download ZIP" ;
Unzip the downloaded file;
Open the project in PyCharm IDE;
Install the Selenium library using the command "pip install selenium" in the PyCharm IDE terminal;
Install the Webdriver_manager library using the command "pip install webdriver_manager" in the PyCharm IDE terminal;
Install the Behave-html-formatter library using the command "pip install behave-html-formatter" in the PyCharm IDE terminal;
Execute the command "behave -f html -o report-testing_final_16.16.2023.html" and wait for the test to run;
Open the generated report "report-testing_final_16.16.2023.html" in a desired browser to view the test results.