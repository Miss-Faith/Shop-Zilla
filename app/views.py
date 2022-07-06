from django.shortcuts import render, HttpResponse

from bs4 import BeautifulSoup
import requests

# Create your views here.
# def get_results(request):
#     if 'searchitem' in request.GET and request.GET["searchitem"]:
#         global search
#         search = request.GET.get("searchitem").replace(" ", "%20")

#     url_jiji = "https://jiji.co.ke/search?query=johnie+walker"
#     jiji_results = requests.get(url_jiji)
#     jiji_soup = BeautifulSoup(jiji_results.text, 'html.parser')
#     jiji_items = jiji_soup.find_all('div', class_="qa-advert-list-item")

#     name = []
#     price= []
#     image= []
#     location= []
#     all_items = []
#     for item in jiji_items:
#         jiji_item_name = item.find('h4',class_="qa-advert-title").text
#         jiji_item_price = item.find('p',class_="b-list-advert__item-price").text
#         jiji_item_image = item.find('img').get('src')
#         jiji_item_location = item.find('div', class_="b-list-advert__item-info").text

#         name.append(jiji_item_name)
#         price.append(jiji_item_price)
#         image.append(jiji_item_image)
#         location.append(jiji_item_location)

#     for (a, b ,c ,d) in zip(name, price,image,location):
        
#         names = {
#             'name': a,
#             'price': b,
#             'image': c,
#             'location': d
#         } 
        
#         all_items.append(names)
#         print(names)

#     context={
#         'title': 'Results',
#         'price': price,
#         'names': all_items,
#         'search': search,
#     }

#     return render(request, 'results.html', context)

def home(request):
    return render(request, 'home.html')

def search(request):
    if 'searchitem' in request.GET and request.GET["searchitem"]:
        global search
        search = request.GET.get("searchitem").replace(" ", "%20")

    store = 'Jiji'
    url_jiji_search = "https://jiji.co.ke/search?query="
    url_jiji = "%s%s"%(url_jiji_search,search)
    jiji_results = requests.get(url_jiji)
    jiji_soup = BeautifulSoup(jiji_results.text, 'html.parser')
    jiji_items = jiji_soup.find_all('div', class_="qa-advert-list-item")

    name = []
    price= []
    image= []
    location= []
    total_items = []
    for item in jiji_items:
        jiji_item_name = item.find('h4',class_="qa-advert-title").text
        jiji_item_price = int(item.find('p',class_="b-list-advert__item-price").text.replace('KSh ', '').replace('\n ', '').replace(' ', '').replace(',', ''))
        jiji_item_image = item.find('img').get('src')
        jiji_item_location = item.find('div', class_="b-list-advert__item-info").text.split(',')[0]

        name.append(jiji_item_name)
        price.append(jiji_item_price)
        image.append(jiji_item_image)
        location.append(jiji_item_location)

    for (a, b ,c ,d) in zip(name,price,image,location):
        
        items = {
            'name': a,
            'price': b,
            'image': c,
            'location': d
        } 
        
        total_items.append(items)
        all_items = sorted(total_items, key=lambda k: k['price'])
        min_item = all_items[0]

    context={
        'all_items': all_items,
        'min_item': min_item,
        'store': store,
    }

    return render(request, 'search.html', context)

