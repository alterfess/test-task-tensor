### Installation and execution

- In this project **webdriver_manager** is used. You don't need install webdrivers separately

- Installation of the all nedeed plugins in the virtual environment:
```
pip install -r requirements.txt
```
- Start of the all autotest scenarios
```
cd .\tests\
pytest -s -v
```
- You can start scenarios separately:
```
pytest .\test_yandex_pictures.py -s -v
pytest .\test_homepage_yandex.py -s -v
```

### Report generation
All reports are generated in **tests\reports** folder:

For yandex home page test:
```
test_home_page_yandex_report.txt
```
For yandex pictures page test:
```
test_home_page_yandex_report.txt
```
