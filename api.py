import requests
import json
import os
from dotenv import load_dotenv


def get_image_of_the_day(date=None):

    load_dotenv()
    key = os.getenv('KEY')
    if date is None: get = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    else: get = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}&date={date}')
    return get.json()


def creating_files(data):        
    with open('explanation.txt', 'w') as f:
        f.write(data["explanation"])

    media_url = data["url"]
    media_url_response = requests.get(media_url)

        
    if data["media_type"] == "image":
        with open('nasa_image.jpg', 'wb') as f:
            f.write(media_url_response.content)
            return data["media_type"]
        
    else: return media_url

def open_files(type):
    if type == "image":
        os.system(".\\nasa_image.jpg")
    else:
        os.startfile(type)
    os.system(f".\\explanation.txt")

if __name__=="__main__":
    
    date = input("if u want to get the image of the day press just wrie YYYY-MM-DD or press enter to get the image of the day: ")
    data = get_image_of_the_day(date)    
    print(f'{data["date"]}\n{data["title"]}')
    type = creating_files(data)
    open_files(type)
