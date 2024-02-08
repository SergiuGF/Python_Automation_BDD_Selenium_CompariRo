Framework-ul reprezinta un plan de testare de tip BDD (behavior-driven development), a platformei de comparare a preturilor, Compari.ro.
Limbaj folosit: Python – vers. 3.11 | IDE: PyCharm vers. 2023.2
Librarii folosite:  
- Librariile standard PyCharm (preinstalate);
- Selenium vers. 4.14.0 (folosita pentru automatizarea unor actiuni intr-un browser);
- Webdriver-manager vers. 4.0.1 (folosita pentru facilitarea gestionarii automate a drive-relor necesare pentru Selenium); 
- Behave vers. 1.2.6. (librarie specifica BDD folosita pentru scrierea testelor intr-un limbaj natural, alaturi de Gherkin);
- Behave-html-formatter vers. 0.9.10 (folosita pentru formatarea fisierelor behave.ini in fisiere HTML);
- Gherkin Language (folosita pentru scrierea testelor intr-un limbaj natural - alaturi de Behave - pe intelesul persoanelor care nu au cunostinte tehnice).
Medote folosite: 
- Modulul Random (importat din Python; ofera functionalitati pentru generarea de numere aleatoare);
- Modul Re (importat din Python; ofera functionalitati pentru cautarea, manipularea si procesarea textului)
- Functia Sleep (importat din modul Time – Python; utilizata pentru a introduce o intarziere in executia codului pentru o perioada specificata de timp).
Instalare si rulare proiect: 
- se acceseaza link-ul de github aferent proiectului;
- se acceseaza butonul                 si se descarca prin accesarea butonului                   ;
- se dezarhiveaza fisierul descarcat                            ;
- se deschide proiectul in IDE-ului Pycharm;
- se instaleaza libraria Selenium utilizand comada ”pip install selenium” in terminalul IDE-ului Pycharm;
- se instaleaza libraria Webdriver_manager utilizand comada ”pip install webdriver_manager” in terminalul IDE-ului Pycharm;
 - se instaleaza libraria Behave-html-formatter utilizand comada ”pip install behave-html-formatter” in terminalul IDE-ului Pycharm;
- se excuta comanda ”behave -f html -o raport-testare_finala_16.16.2023.html” si se asteapta rularea testului;
- se deschide rapotul generat ”raport-testare_finala_16.16.2023.html”
 intr-un browser dorit pentru a vizualiza rezultatelor testelor.
