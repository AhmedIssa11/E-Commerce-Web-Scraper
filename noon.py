"""

@author: Ahmed Issa
"""

# Noon
from bs4 import BeautifulSoup
import requests
import csv


def get_data(pageNo):  

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    source = requests.get('https://www.noon.com/egypt-en/search?q=' + product +'&page=' + str(pageNo), headers=headers).text

    soup = BeautifulSoup(source, 'lxml')

    # print(soup.prettify())

    containers = soup.find_all('div', class_='kcs0h5-0 diNcmV grid')

    for container in containers:

        product_info = []

        product_info.append(pageNo)

        name = container.find('div', class_='e3js0d-10 cyUANN').text
        product_info.append(name)

        price = container.find('div', class_='sc-3751lm-1 eUJkVt large').strong.text
        product_info.append(price)

        img = container.find('div', class_='puv25r-2 cwZEwU').img['src']
        product_info.append(img)
        
        link = container.find('a', class_='sc-7vj7do-0 ftlAjW')
        product_info.append(link)

        products.append(product_info)
     


no_pages = 3
products = []

product = str(input("Enter Product Name :")) 

for i in range(1, no_pages + 1):
    get_data(i)

#for row in products:
#    print(row)

file_name = 'noon.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Page Number','Product Name', 'Price', 'Image','link'])

    for r in range(len(products)):
        writer.writerow([products[r][0], products[r][1], products[r][2], products[r][3],products[r][4]])
