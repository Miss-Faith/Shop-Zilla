from django.shortcuts import render, HttpResponse

from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'django_registration/registration_form.html')

def search(request):
    if 'searchitem' in request.GET and request.GET["searchitem"]:
        global search_jiji, search_copia, search_jumia

        search_jiji = request.GET.get("searchitem").replace(" ", "%20")
        search_copia = request.GET.get("searchitem").replace(" ", "+")
        search_jumia = request.GET.get("searchitem").replace(" ", "+")

    else:
        search_jiji = "chair"
        search_copia = "chair"
        search_jumia = "chair"

    store_jiji = 'Jiji'
    url_jiji_search = "https://jiji.co.ke/search?query="
    url_jiji = "%s%s"%(url_jiji_search, search_jiji)
    jiji_results = requests.get(url_jiji)
    jiji_soup = BeautifulSoup(jiji_results.text, 'html.parser')
    jiji_items = jiji_soup.find_all('div', class_="qa-advert-list-item")


    name = []
    price= []
    image= []
    location= []
    link= []
    total_items = []
    for item in jiji_items:
        
        jiji_item_name = item.find('h4',class_="qa-advert-title").text

        # jiji_item_price = int(item.find('p',class_="b-list-advert__item-price").text.replace('KSh ', '').replace('\n ', '').replace(' ', '').replace(',', ''))

        jiji_item_price = item.find('p',class_="b-list-advert__item-price").text.replace('KSh ', '').replace('\n ', '').replace(' ', '').replace(',', '')

        jiji_item_image = item.find('img').get('src')
        jiji_item_location = item.find('div', class_="b-list-advert__item-info").text.split(',')[0]
        jiji_item_link = item.find('a').get('href')

        name.append(jiji_item_name)
        price.append(jiji_item_price)
        image.append(jiji_item_image)
        location.append(jiji_item_location)
        link.append(jiji_item_link)

    for (a, b ,c ,d,e) in zip(name,price,image,location,link):
        
        items = {
            'name': a,
            'price': b,
            'image': c,
            'location': d,
            'link': e,
        } 
        
        total_items.append(items)
    all_jiji_items = sorted(total_items, key=lambda k: k['price'])
    if all_jiji_items:
        min_jiji_item = all_jiji_items[0]
    else:
        min_jiji_item = ""

    store_copia = 'Copia'
    url_copia = 'https://copia.co.ke/?s=replace_search_text&post_type=product&title=1&excerpt=0&content=0&categories=0&attributes=0&tags=0&sku=1&orderby=date-DESC&ixwps=1'.replace("replace_search_text", search_copia)
    copia_results = requests.get(url_copia)
    copia_soup = BeautifulSoup(copia_results.text, 'html.parser')
    copia_items = copia_soup.find_all('div', class_='product-small')

    copia_product_name = []
    copia_product_price = []
    copia_product_image = []
    copia_product_link = []
    all_copia_products = []
    sorted_copia_products = []

    for item in copia_items:
        copia_item_name = item.find('p', class_="woocommerce-loop-product__title").text
        copia_item_price = int(item.find('bdi').text.replace('KSh', '').replace(',', ''))
        copia_item_image = item.find('img').get('data-src')
        copia_item_link = item.find('a').get('href')

        copia_product_name.append(copia_item_name)
        copia_product_price.append(copia_item_price)
        copia_product_image.append(copia_item_image) 
        copia_product_link.append( copia_item_link)

    for (a, b ,c ,d ) in zip(copia_product_name, copia_product_price,copia_product_image,copia_product_link):
        
        copia_product = {
            'name': a,
            'price': b,
            'image': c,
            'link': d
        } 
    
        all_copia_products.append(copia_product)
    for item in range(0,len(all_copia_products),2):
        sorted_copia_products.append(all_copia_products[item])

    

    sorted_copia_products = sorted(sorted_copia_products, key=lambda k: k['price'])
    
    if sorted_copia_products:
        min_copia_item = sorted_copia_products[0]
    else:
        min_copia_item = ""

    store_jumia = 'Jumia'
    url_jumia_search =  "https://www.jumia.co.ke/catalog/?q="
    url_jumia = "%s%s"%(url_jumia_search,search_jumia)
    jumia_results = requests.get(url_jumia)
    jumia_soup = BeautifulSoup(jumia_results.text, 'html.parser')
    jumia_items = jumia_soup.find_all('article')

    jumia_product_name = []
    jumia_product_price = []
    jumia_product_image = []
    jumia_product_rating = []
    jumia_product_link = []
    all_jumia_products = []
    
    for item in jumia_items:
        if item.find('a').get('href') and item.find('h3', class_='name') and item.find('div', class_='prc')and item.find('img',class_='img') and item.find('div', class_='_s'):
            jumia_item_name = item.find('h3', class_="name").text
            jumia_item_price = item.find('div', class_="prc").text
            jumia_item_image = item.find('img').get('data-src')
            jumia_item_rating = item.find('div', class_="_s").text
            jumia_item_link = 'https://jumia.co.ke'+item.find('a').get('href')

            jumia_product_link.append(jumia_item_link)
            jumia_product_name.append(jumia_item_name)
            jumia_product_price.append(jumia_item_price)
            jumia_product_image.append(jumia_item_image)
            jumia_product_rating.append(jumia_item_rating)

        for (a, b ,c ,d,e) in zip(jumia_product_name, jumia_product_price,jumia_product_image,jumia_product_rating,jumia_product_link):
            
            jumia_product = {
                'name': a,
                'price': b,
                'image': c,
                'rating': d,
                'link': e
            } 
            
            all_jumia_products.append(jumia_product)
        all_jumia_items = sorted(all_jumia_products, key=lambda k: k['price'])
        if all_jumia_items:
            min_jumia_item = all_jumia_items[0]
        else:
            min_jumia_item = "" 

    context={
        'all_jiji_items': all_jiji_items,
        'min_jiji_item': min_jiji_item,
        'store_jiji': store_jiji,
        'copia_products': sorted_copia_products,
        'min_copia_item': min_copia_item,
        'store_copia': store_copia,
        'all_jumia_items': all_jumia_items,
        'min_jumia_item': min_jumia_item,
        'store_jumia': store_jumia,
    }

    return render(request, 'search.html', context)

