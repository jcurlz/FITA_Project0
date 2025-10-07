# Automation Practise Website #
https://practice.expandtesting.com/



## Behave Project Structure ##
ProjRootFolder
|_features
    |_file.feature
    |_steps
      |_ file_steps.py
    |_ environment.py
|_utility
    |_ excel.xslx
|_runner.py
|_requirements.txt
|_README.md

## Virtual Env setup ##
Create an interpreter or python -m venv .venv
.venv\Scripts\activate

## Requirement installation ##
```bash
pip install behave==1.3.3
pip install cucumber-expressions==18.0.1
pip install cucumber-tag-expressions==6.2.0
pip install openpyxl==3.1.5
pip install selenium==4.35.0
pip install behave_html_formatter==0.9.10

pip list
Pick out the required libs from the list and add to your requirements.txt
pip install -r requirements.txt
```

## To execute the py files ##
```bash
python runner.py
```