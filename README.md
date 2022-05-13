Project ini Menggunakan Selenium Python Behave BDD dengan pendekatan POM (Page Object Model) pada Stockbit


# Requirement


- Install Python dan Pip
- Sudah memiliki chromedriver
- lalu ketik di terminal pada folder tersebut

>pip install -r requirements.txt

# Run 

Run biasa

> behave features/

Run dengan report allure framework

> behave -f allure_behave.formatter:AllureFormatter -o reports/ features/

untuk membuka report dengan cara

> allure serve reports/


