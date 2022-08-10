# imbeeQAtest


``` 
├── Test_case.py
│
├── Test_execution.py (for running test case)
│
├── chromedriver.exe
│
├── geckodriver.exe
│
├── page_object
│   └── question_page_elements.py
│
├── test_function
│   └── question_page_function.py (store test function to be used in test case )
│
└── utility.py
``` 

After clone the repo, please do the following:


1. Download chromedriver.exe and geckodriver.exe sync with your local chrome and firefox version
``` 
https://chromedriver.chromium.org/downloads
https://github.com/mozilla/geckodriver/releases
``` 
Please run cmd in project folder in administrator mode 
2. Create vitual env (run below command in project folder)
``` 
py -m venv venv
.\venv\Scripts\activate.bat 
``` 

3. install the required libs in vitual env (run below command)
``` 
pip install --upgrade pip
pip install -r requirements.txt
``` 
if install requirements.txt is failed, please help to install below one by one
``` 
pip install requests
pip install selenium
pip install setuptools-rust
pip install selenium-wire
pip install pytest
pip install pytest-html
``` 

4. Start the test (run below command)

``` 
python Test_execution.py
``` 
or
```
pytest -s -v Test_case.py --html=result.html --capture=tee-sys --disable-pytest-warnings --self-contained-html
```
