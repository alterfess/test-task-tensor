### Instalation and execution

- In this project webdriver_manager is used. You don't need install webdrivers separately
- pip install -r requirements.txt: Installation of the all nedeed plugins in the virtual environment
- cd .\tests\ -> pytest -s -v: Start of the all autotest scenarios


You can start scenarios separately:
- pytest .\test_yandex_pictures.py -s -v
- pytest .\test_homepage_yandex.py -s -v

### Report generation
All reports are generated in test\reports folder
- test_home_page_yandex_report.txt - for yandex home page test
- test_yandex_pictures_report.txt - for yandex pictures page test
