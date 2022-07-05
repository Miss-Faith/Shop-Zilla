from django.shortcuts import render, HttpResponse

from bs4 import BeautifulSoup
import requests



# Create your views here.
def get_results(request):
    
    url_jumia = ""

    jumia_results = requests.get(url_jumia)

    jumia_soup = BeautifulSoup(jumia_results.text, 'html.parser')

    jumia_items = jumia_soup.find_all('div', class_="qa-advert-list-item")

    name = []
    price= []
    image= []
    location= []
    all_items = []
    for item in jumia_items:
        jumia_item_name = item.find('h4',class_="qa-advert-title").text
        jumia_item_price = item.find('p',class_="b-list-advert__item-price").text
        jumia_item_image = item.find('img').get('src')
        jumia_item_location = item.find('div', class_="b-list-advert__item-info").text

        name.append(jumia_item_name)
        price.append(jumia_item_price)
        image.append(jumia_item_image)
        location.append(jumia_item_location)

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

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

