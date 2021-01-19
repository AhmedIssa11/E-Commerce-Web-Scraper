"""

@author: Ahmed Issa
"""

# Amazon
from bs4 import BeautifulSoup
import requests
import csv


def get_data(pageNo):  

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    source = requests.get('https://www.amazon.in/s?k=' + product +'&page=' + str(pageNo), headers=headers).text

    soup = BeautifulSoup(source, 'lxml')

    # print(soup.prettify())

    containers = soup.find_all('div', class_='s-include-content-margin s-border-bottom s-latency-cf-section')

    for container in containers:

        product_info = []

        product_info.append(pageNo)

        name = container.find('a', class_='a-link-normal a-text-normal').text
        product_info.append(name)

        if container.find('span', class_='a-price-whole'):
            price = container.find('span', class_='a-price-whole').text
        else:
            price = "null"
        product_info.append(price)

        if container.find('span', class_='a-size-base'):
            orders = container.find('span', class_='a-size-base').text
        else:
            orders = "null"
        product_info.append(orders)

        img = container.find('div', class_='a-section aok-relative s-image-fixed-height').img['src']  
        product_info.append(img)
        
        link = container.find('a', class_='a-link-normal s-no-outline')['href']
        product_info.append("https://www.amazon.in"+link)
        
        products.append(product_info)


no_pages = 4
products = []

product = str(input("Enter Product Name :")) 

for i in range(1, no_pages + 1):
    get_data(i)

#for row in products:
#    print(row)

file_name = 'amazon.csv'

# create csv file on colab files
with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Page Number','Product Name', 'Price', 'Orders', 'Image','Link'])

    for r in range(len(products)):
        writer.writerow([products[r][0], products[r][1], products[r][2], products[r][3], products[r][4], products[r][5]])