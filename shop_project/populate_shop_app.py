import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
import django
django.setup()

import random
from faker import Faker
from shop_app.models import Client, Product, Maillot

# CONSIGNE
# creez 2 fonctions :
#   1. cree 1000 faux clients
#   2. cree 50 faux produits

fakegen = Faker()


def generate_brand():
    brands = ['Nike', 'Adidas','Reebook', 'Jordan', 'Geox', 'Balenciaga', 'Timberland', 'Asics', 'Puma','New Balance']
    index= random.randint(0,9)
    return brands[index]


def generate_maillot_brand():
    maillotbrands = ['Chelsea', 'Paris Saint Germain','Juventus de Turin', 'Manchester United', 'Liverpool FC', 'Bayern Munich', 'Borussia Dortmund', 'Real Madrid ', 'Monaco','Celtic']
    index= random.randint(0,9)
    return maillotbrands[index]

def generate_clients():
    for client in range(0,1000):
        client = Client.objects.get_or_create(first_name=fakegen.first_name(), last_name=fakegen.last_name(), password=fakegen.password(), email=fakegen.email())[0]
        

def generate_products():
    for product in range(0,50):
        price = random.randint(79,399)
        brand = generate_brand()
        product = Product.objects.get_or_create(name=brand, price=price, description =fakegen.text(max_nb_chars=400))
        

def generate_maillots():
    for maillot in range(0,150):
        maillotprice = random.randint(79,499)
        maillot_brand = generate_maillot_brand()
        maillot = Maillot.objects.get_or_create(name=maillot_brand, description =fakegen.text(max_nb_chars=400),price=maillotprice)[0]

            

def populate():
    generate_products()
    generate_clients()
    generate_maillots()






if __name__ == '__main__':
    print('starting populate...')
    populate()
    print('done populating')