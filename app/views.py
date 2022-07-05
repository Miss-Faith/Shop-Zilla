
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
    all_items = []
    for item in jiji_items:
        jiji_item_name = item.find('h4',class_="qa-advert-title").text
        jiji_item_price = item.find('p',class_="b-list-advert__item-price").text
        
        

        name.append(jiji_item_name)
        price.append(jiji_item_price)

    for (a, b) in zip(name, price):
        
        names = {
            'name': a,
            'price': b
        } 
        
        all_items.append(names)
        print(names)

    context={
        'title': 'Results',
        'price': price,
        'names': all_items,
    }

    return render(request, 'results.html',context)
