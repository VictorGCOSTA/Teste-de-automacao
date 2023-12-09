from selenium import webdriver
from selenium.webdriver.common.by import By
import xmltodict
import random

#Função para ler o arquivo XML
def get_user():
    with open('user.xml') as fd:
        doc = xmltodict.parse(fd.read())
        return doc['user']

#Função para listar os produtos disponíveis
def list_items(browser):
    items = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    print(f'Lista de produtos disponíveis:')
    for index, item in enumerate(items):
        print(f'{index}: {item.text}')

#Função para selecionar 3 produtos aleatórios
def select_products(browser):
    print('Selecionando produtos aleatórios...')
    items = browser.find_elements(By.CLASS_NAME, 'inventory_item')
    random_items = random.sample(items, 3)
    for item in random_items:
        item_add = item.find_element(By.CLASS_NAME, 'btn_inventory')
        item_add.click()

# Configurações do navegador para evitar erros de certificado
opt = webdriver.ChromeOptions()
opt.add_argument('--ignore-certificate-errors')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# Instancia o driver do navegador
browser = webdriver.Chrome(options=opt)
browser.get('https://www.saucedemo.com/')

#Pega os dados do usuário
user = get_user()

#Login no site
username = browser.find_element(By.ID,'user-name')
username.send_keys(user['username'])
password = browser.find_element(By.ID,'password')
password.send_keys(user['password'])
login = browser.find_element(By.ID, 'login-button')
login.click()
print('Login realizado com sucesso!')

#Listar produtos
list_items(browser)

#Selecionar produtos
select_products(browser)

#Visualizar o carrinho
cart = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
cart.click()
items_cart = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
print(f'Lista de produtos no carrinho:')
for index, item in enumerate(items_cart):
    print(f'{index}: {item.text}')

#Finalizar compra
checkout = browser.find_element(By.CLASS_NAME, 'checkout_button')
checkout.click()
first_name = browser.find_element(By.ID, 'first-name')
first_name.send_keys(user['firstname'])
last_name = browser.find_element(By.ID, 'last-name')
last_name.send_keys(user['lastname'])
postal_code = browser.find_element(By.ID, 'postal-code')
postal_code.send_keys(user['postalcode'])
ctn = browser.find_element(By.ID, 'continue')
ctn.click()

#Ver valor total da compra
total = browser.find_element(By.CLASS_NAME, 'summary_total_label')
print(f'Valor total da compra: {total.text}')

#Finalizar compra
finish = browser.find_element(By.CLASS_NAME, 'cart_button')
finish.click()
print('Compra finalizada com sucesso!')




