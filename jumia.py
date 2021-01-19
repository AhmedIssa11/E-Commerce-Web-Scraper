"""

@author: Ahmed Issa
"""

# Jumia
from bs4 import BeautifulSoup
import requests
import csv


def get_data(pageNo):  

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    source = requests.get('https://www.jumia.com.eg/ar/catalog/?q=' + product +'&page=' + str(pageNo) + '#catalog-listing', headers=headers).text

    soup = BeautifulSoup(source, 'lxml')

    # print(soup.prettify())

    containers = soup.find_all('article', class_='prd _fb col c-prd')

    for container in containers:

        product_info = []

        product_info.append(pageNo)

        name = container.find('h3', class_='name').text
        product_info.append(name)

        price = container.find('div', class_='prc').text
        product_info.append(price)

        img = container.find('img', class_='img')['src']
        product_info.append(img)

        if container.find('div', class_='old'):
          old_price = container.find('div', class_='old').text
        else:
          old_price = "null"
        product_info.append(old_price)

        if container.find('div', class_='tag _dsct _sm'):
          tag = container.find('div', class_='tag _dsct _sm').text
        else:
          tag = "null"
        product_info.append(tag)

        if container.find('div', class_='rev'):
          orders = container.find('div', class_='rev').text
        else:
          orders = "null"
        product_info.append(orders)

        link = container.find('a', class_='core')['href']
        product_info.append("https://www.jumia.com.eg"+link)
        
        products.append(product_info)


no_pages = 3
products = []

product = str(input("Enter Product Name :")) 

for i in range(1, no_pages + 1):
    get_data(i)

#for row in products:
#    print(row)

file_name = 'jumia.csv'


with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Page Number','Product Name', 'Price', 'Old Price','Tag','Orders','Image','Link'])

    for r in range(len(products)):
        writer.writerow([products[r][0], products[r][1], products[r][2], products[r][4], products[r][5], products[r][6], products[r][3],products[r][7]])



