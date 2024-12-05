import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('KEY')
date = input("if u want to get the image of the day press just wrie YYYY-MM-DD or press enter to get the image of the day: ")

get = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}&date={date}')
    
data = get.json()

print(f'{data["date"]}\n{data["title"]}')

with open('explanation.txt', 'w') as f:
    f.write(data["explanation"])


media_url = data["url"]
media_url_response = requests.get(media_url)
media_path = 'nasa_image.jpg'

    
if data["media_type"] == "image":
    image_response = requests.get(media_url)
    with open('picture.jpg', 'wb') as f:
        f.write(media_url_response.content)
    os.system('.\\picture.jpg')    
    
else:
    os.startfile(media_url)

os.system(f".\\explanation.txt")