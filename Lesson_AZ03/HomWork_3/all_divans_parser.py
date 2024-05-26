from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

class DivanDriver:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")  # Открыть браузер в фоновом режиме
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)  # Увеличенное время ожидания

    def parse_page(self, url):
        self.driver.get(url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Прокрутка страницы вниз
        time.sleep(10)  # Увеличенное время ожидания для загрузки элементов
        list = []
        items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_Ud0k.U4KZV')))
        for item in items:
            try:
                link_element = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct')
                name = link_element.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
                price_str = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
                price = int(price_str.replace(' ', ''))  # Преобразование строки в число
                list.append([name, price])
            except Exception as e:
                print(f'Ошибка при парсинге элемента: {e}')
        return list

    def parse_all_pages(self, base_url, total_pages):
        all_list = []
        for page in range(1, total_pages + 1):
            url = f'{base_url}/page-{page}'
            print(f'Парсинг страницы: {url}')
            list = self.parse_page(url)
            all_list.extend(list)
        return all_list

    def save_to_csv(self, filename, all_list):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price'])
            for item in all_list:
                writer.writerow(item)

    def average_price(self, all_list): # вычисление средней цены
        prices = [item[1] for item in all_list]
        average_price = np.mean(prices)
        print(f'Средняя цена всех {len(prices)} диванов - {average_price} рублей.')

        return prices

    def plt_hist(self, prices):  # построение гистограммы
        plt.hist(prices, bins=20, edgecolor='black')
        plt.title('Гистограмма цен на диваны')
        plt.xlabel('Цена')
        plt.ylabel('Частота')
        plt.show()

def main():
    # в url отфильтрованы только дианы (без кресел)
    base_url = 'https://www.divan.ru/sankt-peterburg/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54'
    total_pages = 20
    driver = DivanDriver()
    all_list = driver.parse_all_pages(base_url, total_pages)
    driver.save_to_csv('all_divans_prices.csv', all_list)
    prices = driver.average_price(all_list)
    driver.plt_hist(prices)

    driver.driver.quit()

if __name__ == "__main__":
    main()