from selenium import webdriver
import time

_headers = {
        "brand":"26303219,100195335,32686750,26303000,26303399",
        "type":"149190",
        "wire":"32735"
    }
_url = "https://www.ozon.ru/category/audiotehnika-15543/"
try:
    driver = webdriver.Firefox(executable_path="C:\information\ProjectsCode\ParserCategories\drivers\geckodriver.exe")
    driver.get(url=_url, headers=_headers)
    time.sleep(5)
except Exception:
    pass
finally:
    pass