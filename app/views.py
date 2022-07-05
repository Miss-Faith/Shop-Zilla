
from django.shortcuts import render

from bs4 import BeautifulSoup
import requests



# Create your views here.
def get_results(request):
    
    url_jiji = "https://jiji.co.ke/search?query=johnie"

    jiji_results = requests.get(url_jiji)

    jiji_soup = BeautifulSoup(jiji_results.text, 'html.parser')

    jiji_items = jiji_soup.find_all('div', class_="qa-advert-list-item")

    name = []
    price= []
    image= []
    location= []
    all_items = []
    for item in jiji_items:
        jiji_item_name = item.find('h4',class_="qa-advert-title").text
        jiji_item_price = item.find('p',class_="b-list-advert__item-price").text
        jiji_item_image = item.find('img').get('src')
        jiji_item_location = item.find('div', class_="b-list-advert__item-info").text

        name.append(jiji_item_name)
        price.append(jiji_item_price)
        image.append(jiji_item_image)
        location.append(jiji_item_location)

    for (a, b ,c ,d) in zip(name, price,image,location):
        
        names = {
            'name': a,
            'price': b,
            'image': c,
            'location': d
        } 
        
        all_items.append(names)
        print(names)

    context={
        'title': 'Results',
        'price': price,
        'names': all_items,
    }

    return render(request, 'results.html',context)
