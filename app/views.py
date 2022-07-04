from django.shortcuts import render

from bs4 import BeautifulSoup
import requests


# Create your views here.
def get_results(request):
    
    url_jiji = "https://jiji.co.ke/search?query=johnie"

    jiji_results = requests.get(url_jiji)

    jiji_soup = BeautifulSoup(jiji_results.text, 'html.parser')
    
    jiji_items = jiji_soup.find_all('div', class_="qa-advert-list-item")

    for item in jiji_items:
    # print(item.prettify())
        jiji_item_name = item.find('h4',class_="qa-advert-title").text
        jiji_item_price = item.find('p',class_="b-list-advert__item-price").text
        

    context={
        'title': 'Results',
        'jiji_items': jiji_item_name,
        'jiji_prices': jiji_item_price,
    }

    return render(request, 'app/results.html',context)
