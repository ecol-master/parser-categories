from aiohttp import ClientSession
from bs4 import BeautifulSoup
import requests
import datetime, json

async def __parse_headphones_info(session: ClientSession):
    _headers = {
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "brand":"26303219,100195335,32686750,26303000,26303399",
        "type":"149190",
        "wire":"32735"
    }
    _url = "https://www.ozon.ru/category/audiotehnika-15543/"

    response = requests.get(url=_url, headers=_headers)
    soup = BeautifulSoup(response.text, "lxml")
    headphones_links = [tag_a["href"] for tag_a in soup.find_all("a", class_="tile-hover-target")]
    print('\n'.join(headphones_links))
    print(len(headphones_links))


async def get_headphones(session: ClientSession):
    headphones_info = await __parse_headphones_info(session=session)

    format_date = datetime.datetime.now().strftime("%d_%m_%Y")
    
    filename = "headphones_{}".format(format_date) 
    with open("data/{}.json".format(filename), "w") as jsonfile:
        json.dump(headphones_info, jsonfile)
        
    print("Информация о наушниках получена")

"https://www.ozon.ru/category/audiotehnika-15543/?brand=26303219%2C100195335%2C32686750%2C26303399%2C26303000&type=149190"