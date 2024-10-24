# ссылка на то как Как найти CSS селектор нужного элемента на странице товара
# https://allrival.com/post/articles/kak-nayti-css-selektor-nuzhnogo-elementa-na-stranice-tovara

import time

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = "https://xn--b1ag8ag.xn--80asehdb/catalog/potolochnie-lyustry/"
# Открываем веб-страницу
driver.get(url)
time.sleep(3)
vacancies = driver.find_elements(By.CLASS_NAME, 'product-item')
parsed_data = []
for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'div.product-item-title').text
        # bx_3966226736_686347_7e1b8e3524755c391129a9d7e6f2d206 > div > div.product-item-title > a
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.product-item-price-current').text
    # bx_3966226736_686347_7e1b8e3524755c391129a9d7e6f2d206_price > span.product-item-price-current
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue
    parsed_data.append([title, company])
    print(title, company)
driver.quit()

with open("hh_svet.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование', 'цена'])
    writer.writerows(parsed_data)
    print("Файл создан")