from django.shortcuts import render, HttpResponse

from bs4 import BeautifulSoup
import requests

# Create your views here.
# def get_results(request):
    
def get_jumia_data():

    url_jumia =  "https://www.jumia.co.ke/catalog/?q=johnie+walker"
    jumia_results = requests.get(url_jumia)
    jumia_soup = BeautifulSoup(jumia_results.text, 'html.parser')
    jumia_items = jumia_soup.find_all('a', class_="core")

    jumia_product_name = []
    jumia_product_price = []
    jumia_product_image = []
    jumia_product_rating = []
    all_jumia_products = []

    for item in jumia_items:
        
        jumia_item_name = item.find('h3', class_="name").text
        jumia_item_price = item.find('div', class_="prc").text
        jumia_item_image = item.find('img').get('data-src')
        jumia_item_rating = item.find('div', class_="_s")
        
        
        if jumia_item_rating != None:
            jumia_item_rating = jumia_item_rating.text

            jumia_product_name.append(jumia_item_name)
            jumia_product_price.append(jumia_item_price)
            jumia_product_image.append(jumia_item_image)
            jumia_product_rating.append(jumia_item_rating)

        for (a, b ,c ,d) in zip(jumia_product_name, jumia_product_price,jumia_product_image,jumia_product_rating):
            
                jumia_product = {
                    'name': a,
                    'price': b,
                    'image': c,
                    'rating': d
                } 
                
                all_jumia_products.append(jumia_product)
                # print(all_jumia_products)

    return all_jumia_products

def get_copia_data():




    all_jumia_products = get_jumia_data()
    print(len(all_copia_products))
    context={
        'title': 'Results',
        'all_jumia_items': all_jumia_products,
        'names': all_items,
        'all_copia_items': all_copia_products
    }

    return render(request, 'results.html',context)


def home(request):
    return render(request, 'home.html')

def search(request):
    if 'searchitem' in request.GET and request.GET["searchitem"]:
        global search_jiji
        global search_copia
        global search_jumia

        search_jiji = request.GET.get("searchitem").replace(" ", "%20")
        search_copia = request.GET.get("searchitem").replace(" ", "+")
        search_jumia = request.GET.get("searchitem").replace(" ", "+")


    store_jiji = 'Jiji'
    url_jiji_search = "https://jiji.co.ke/search?query="
    url_jiji = "%s%s"%(url_jiji_search,search_jiji)
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
        all_jiji_items = sorted(total_items, key=lambda k: k['price'])
        min_jiji_item = all_jiji_items[0]

    store_copia = 'Copia'
    url_copia = 'https://copia.co.ke/?s=replace_search_text&post_type=product&title=1&excerpt=0&content=0&categories=0&attributes=0&tags=0&sku=1&orderby=date-DESC&ixwps=1'.replace("replace_search_text ", search_copia)
    copia_results = requests.get(url_copia)
    copia_soup = BeautifulSoup(copia_results.text, 'html.parser')
    copia_items = copia_soup.find_all('div', class_='product-small')

    copia_product_name = []
    copia_product_price = []
    copia_product_image = []
    
    all_copia_products = []

    for item in copia_items:
        
        copia_item_name = item.find('p', class_="woocommerce-loop-product__title").text
        copia_item_price = item.find('bdi').text
        copia_item_image = item.find('img').get('data-src')
        

        copia_product_name.append(copia_item_name)
        copia_product_price.append(copia_item_price)
        copia_product_image.append(copia_item_image)
            

        for (a, b ,c ) in zip(copia_product_name, copia_product_price,copia_product_image):
            
            copia_product = {
                'name': a,
                'price': b,
                'image': c,
            } 
            
            all_copia_products.append(copia_product)
            all_copia_items = sorted(all_copia_products, key=lambda k: k['price'])
            min_copia_item = all_copia_items[0]

    
    all_items.append(names)
        
    all_copia_products = get_copia_data()

    context={
        'all_jiji_items': all_jiji_items,
        'min_jiji_item': min_jiji_item,
        'all_copia_items': all_copia_items,
        'min_copia_item': min_copia_item,
        'store_jiji': store_jiji,
        'store_copia': store_copia,
    }

    return render(request, 'search.html', context)

