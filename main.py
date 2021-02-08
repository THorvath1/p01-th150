from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup
import requests
import os, os.path, csv

my_url = 'https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tid=17489'

# loading connection/grabbing page
xClient = ureq(my_url)
p_html = xClient.read()

# html parsing
page_soup = BeautifulSoup(p_html, "html.parser")

#grabs each laptop
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "laptops.csv"
f = open(filename, "w")
headers = "brand", "product_name", "shipping\n"
f.write("headers")

# for loop that extracts titles of laptops
for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class" : "price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)

	f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")


 
