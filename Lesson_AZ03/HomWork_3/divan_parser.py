from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

driver = webdriver.Chrome()
# в url отфильтрованы только дианы (без кресел)
url = 'https://www.divan.ru/sankt-peterburg/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54'
driver.get(url)
time.sleep(5)

divans = []

items = driver.find_elements(By.CLASS_NAME, '_Ud0k.U4KZV')
for item in items:
    try:
        link_element = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct')
        name = link_element.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price_str = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        price = int(price_str.replace(' ', ''))  # Преобразование строки в число
        divans.append([name, price])
    except Exception as e:
        print(f'Ошибка при парсинге элемента: {e}')

prices = [divan[1] for divan in divans]
average_price = np.mean(prices)
print(f'Средняя цена на диваны - {average_price} рублей')

plt.hist(prices, bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()


with open('divans_prices.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])
    for divan in divans:
       writer.writerow(divan)

driver.quit()
